import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import statsmodels.api as sm
import math

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

from scipy import stats
from scipy.stats import kurtosis, skew
from functools import partial, reduce 

#Load all the data into seperate data frames

# GDP data
gdp_df = pd.read_csv("../clean_gdp_capita.csv", encoding="ISO-8859-1", index_col=0)
a = gdp_df.columns[3:]
gdp_df = pd.melt(gdp_df, id_vars=['Country.Name', 'Region', 'IncomeGroup'], value_vars=a,
        var_name='Year', value_name='GDP').sort_values(['Country.Name','Year']).reset_index()
gdp_df.drop('index', inplace=True, axis=1)

#Poverty Headcount data
poverty_df = pd.read_csv("../clean_poverty_head.csv", encoding="ISO-8859-1", index_col=0)
a = poverty_df.columns[3:]
poverty_df = pd.melt(poverty_df, id_vars=['Country.Name', 'Region', 'IncomeGroup'], value_vars=a,
        var_name='Year', value_name='Poverty Rate').sort_values(['Country.Name','Year']).reset_index()
poverty_df.drop('index', inplace=True, axis=1)

#Literacy Rate
literacy_df = pd.read_csv("../clean_literacy_rate.csv", encoding="ISO-8859-1", index_col=0)
a = literacy_df.columns[3:]
literacy_df = pd.melt(literacy_df, id_vars=['Country.Name', 'Region', 'IncomeGroup'], value_vars=a,
        var_name='Year', value_name='Literacy Rate').sort_values(['Country.Name','Year']).reset_index()
literacy_df.drop('index', inplace=True, axis=1)

#Secondary School Enrollment
second_school_df = pd.read_csv("../clean_school_enrol_sec.csv", encoding="ISO-8859-1", index_col=0)
a = second_school_df.columns[3:]
second_school_df = pd.melt(second_school_df, id_vars=['Country.Name', 'Region', 'IncomeGroup'], value_vars=a,
        var_name='Year', value_name='Secondary School Enrollment').sort_values(['Country.Name','Year']).reset_index()
second_school_df.drop('index', inplace=True, axis=1)

#Tertiary School Enrollment
third_school_df = pd.read_csv("../clean_school_enrol_tert.csv", encoding="ISO-8859-1", index_col=0)
a = third_school_df.columns[3:]
third_school_df = pd.melt(third_school_df, id_vars=['Country.Name', 'Region', 'IncomeGroup'], value_vars=a,
        var_name='Year', value_name='Tertinary School Enrollment').sort_values(['Country.Name','Year']).reset_index()
third_school_df.drop('index', inplace=True, axis=1)

#Gini Index data
gini_df = pd.read_csv("../clean_gini_index.csv", encoding="ISO-8859-1", index_col=0)
a = gini_df.columns[3:]
gini_df = pd.melt(gini_df, id_vars=['Country.Name', 'Region', 'IncomeGroup'], value_vars=a,
        var_name='Year', value_name='Gini Index').sort_values(['Country.Name','Year']).reset_index()
gini_df.drop('index', inplace=True, axis=1)

# Merge dataframes
dfs = [gdp_df, gini_df, literacy_df, second_school_df, third_school_df, poverty_df]
final_df = reduce(lambda x,y: pd.merge(x,y, on=['Country.Name', 'Region', 'IncomeGroup', 'Year'], how='outer'), dfs) 

# Only use the results for actual data
final_df.dropna(subset=['Poverty Rate','GDP','Gini Index', 'Literacy Rate', 'Secondary School Enrollment'
                        ,'Tertinary School Enrollment'], inplace=True)
final_df.index.name = 'Index'

# Create label for our result and seperate into train and test
# for maching learning if we want to create more models
y = final_df['Poverty Rate']
final_df.drop(['Poverty Rate'], axis=1, inplace = True)
X = final_df.select_dtypes(exclude=['object'])
count = 0
for i in y.index:
    if y.at[i] >= 75:
        y.at[i] = 3
    elif y.at[i] >= 50 and y.at[i] < 75 :
        y.at[i] = 2
    elif y.at[i] >= 25 and y.at[i] < 50 :
        y.at[i] = 1
    else:
        y.at[i] = 0

X_train, X_test, y_train, y_test = train_test_split(X,y, train_size = .75, test_size = 0.25 , random_state = 0)

#statisical summary .describe()

model = LinearRegression()
