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
gdp_df = pd.read_csv("clean_gdp_capita.csv", encoding="ISO-8859-1", index_col=0)
a = gdp_df.columns[3:]
gdp_df = pd.melt(gdp_df, id_vars=['Country.Name', 'Region', 'IncomeGroup'], value_vars=a,
        var_name='Year', value_name='GDP').sort_values(['Country.Name','Year']).reset_index()
gdp_df.drop('index', inplace=True, axis=1)

#Poverty Headcount data
poverty_df = pd.read_csv("clean_poverty_head.csv", encoding="ISO-8859-1", index_col=0)
a = poverty_df.columns[3:]
poverty_df = pd.melt(poverty_df, id_vars=['Country.Name', 'Region', 'IncomeGroup'], value_vars=a,
        var_name='Year', value_name='Poverty Rate').sort_values(['Country.Name','Year']).reset_index()
poverty_df.drop('index', inplace=True, axis=1)

#Literacy Rate
literacy_df = pd.read_csv("clean_literacy_rate.csv", encoding="ISO-8859-1", index_col=0)
a = literacy_df.columns[3:]
literacy_df = pd.melt(literacy_df, id_vars=['Country.Name', 'Region', 'IncomeGroup'], value_vars=a,
        var_name='Year', value_name='Literacy Rate').sort_values(['Country.Name','Year']).reset_index()
literacy_df.drop('index', inplace=True, axis=1)

#Secondary School Enrollment
second_school_df = pd.read_csv("clean_school_enrol_sec.csv", encoding="ISO-8859-1", index_col=0)
a = second_school_df.columns[3:]
second_school_df = pd.melt(second_school_df, id_vars=['Country.Name', 'Region', 'IncomeGroup'], value_vars=a,
        var_name='Year', value_name='Secondary School Enrollment').sort_values(['Country.Name','Year']).reset_index()
second_school_df.drop('index', inplace=True, axis=1)

#Tertiary School Enrollment
third_school_df = pd.read_csv("clean_school_enrol_tert.csv", encoding="ISO-8859-1", index_col=0)
a = third_school_df.columns[3:]
third_school_df = pd.melt(third_school_df, id_vars=['Country.Name', 'Region', 'IncomeGroup'], value_vars=a,
        var_name='Year', value_name='Tertinary School Enrollment').sort_values(['Country.Name','Year']).reset_index()
third_school_df.drop('index', inplace=True, axis=1)

#Gini Index data
gini_df = pd.read_csv("clean_gini_index.csv", encoding="ISO-8859-1", index_col=0)
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
X_gdp = X["GDP"]
X_gini = X["Gini Index"]
X_lit = X["Literacy Rate"]
X_sec = X["Secondary School Enrollment"] 
X_ter = X["Tertinary School Enrollment"]

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

model = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X_gdp,y, train_size = .75, test_size = 0.25 , random_state = 0)

#gdp
X_train = X_train.values
X_train = np.reshape(X_train, (-1,1))
X_test = X_test.values
X_test = np.reshape(X_test, (-1,1))
y_train = y_train.values
y_train = np.reshape(y_train, (-1,1))
y_test = y_test.values
y_test = np.reshape(y_test, (-1,1))
model.fit(X_train,y_train)

# Make predictions using the testing set
gdp_y_pred = model.predict(X_test)

# The coefficients
print('Coefficients: \n', model.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(y_test, gdp_y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(y_test, gdp_y_pred))

# Plot outputs
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, gdp_y_pred, color='blue', linewidth=3)

plt.title('GDP per capita vs Poverty Headcount')
plt.xlabel('GDP per capita')
plt.ylabel('Poverty Headcount (% of population)')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X_gini,y, train_size = .75, test_size = 0.25 , random_state = 0)

#gini
X_train = X_train.values
X_train = np.reshape(X_train, (-1,1))
X_test = X_test.values
X_test = np.reshape(X_test, (-1,1))
y_train = y_train.values
y_train = np.reshape(y_train, (-1,1))
y_test = y_test.values
y_test = np.reshape(y_test, (-1,1))
model.fit(X_train,y_train)

# Make predictions using the testing set
gini_y_pred = model.predict(X_test)

# The coefficients
print('Coefficients: \n', model.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(y_test, gini_y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(y_test, gini_y_pred))

# Plot outputs
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, gini_y_pred, color='blue', linewidth=3)

plt.title('Gini Index vs Poverty Headcount')
plt.xlabel('Gini Index')
plt.ylabel('Poverty Headcount (% of population)')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X_lit,y, train_size = .75, test_size = 0.25 , random_state = 0)

#lit
X_train = X_train.values
X_train = np.reshape(X_train, (-1,1))
X_test = X_test.values
X_test = np.reshape(X_test, (-1,1))
y_train = y_train.values
y_train = np.reshape(y_train, (-1,1))
y_test = y_test.values
y_test = np.reshape(y_test, (-1,1))
model.fit(X_train,y_train)

# Make predictions using the testing set
lit_y_pred = model.predict(X_test)

# The coefficients
print('Coefficients: \n', model.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(y_test, lit_y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(y_test, lit_y_pred))

# Plot outputs
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, lit_y_pred, color='blue', linewidth=3)

plt.title('Literacy Rate vs Poverty Headcount')
plt.xlabel('Literacy Rate (% of adults)')
plt.ylabel('Poverty Headcount (% of population)')

plt.show()
X_train, X_test, y_train, y_test = train_test_split(X_sec,y, train_size = .75, test_size = 0.25 , random_state = 0)

#Secondary School Data
X_train = X_train.values
X_train = np.reshape(X_train, (-1,1))
X_test = X_test.values
X_test = np.reshape(X_test, (-1,1))
y_train = y_train.values
y_train = np.reshape(y_train, (-1,1))
y_test = y_test.values
y_test = np.reshape(y_test, (-1,1))
model.fit(X_train,y_train)

# Make predictions using the testing set
sec_y_pred = model.predict(X_test)

# The coefficients
print('Coefficients: \n', model.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(y_test, sec_y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(y_test, sec_y_pred))

# Plot outputs
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, sec_y_pred, color='blue', linewidth=3)
plt.title('Secondary School Enrollment vs Poverty Headcount')
plt.xlabel('Secondary School Enrollment (% of gross)')
plt.ylabel('Poverty Headcount (% of population)')
plt.show()
X_train, X_test, y_train, y_test = train_test_split(X_ter,y, train_size = .75, test_size = 0.25 , random_state = 0)

#Tertiary School Data
X_train = X_train.values
X_train = np.reshape(X_train, (-1,1))
X_test = X_test.values
X_test = np.reshape(X_test, (-1,1))
y_train = y_train.values
y_train = np.reshape(y_train, (-1,1))
y_test = y_test.values
y_test = np.reshape(y_test, (-1,1))
model.fit(X_train,y_train)

# Make predictions using the testing set
ter_y_pred = model.predict(X_test)

# The coefficients
print('Coefficients: \n', model.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(y_test, ter_y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(y_test, ter_y_pred))

# Plot outputs
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, ter_y_pred, color='blue', linewidth=3)

plt.title('Tertiary School Enrollment vs Poverty Headcount')
plt.xlabel('Tertiary School Enrollment (% of gross)')
plt.ylabel('Poverty Headcount (% of population)')

plt.show()
