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


#Loading in path

#Poverty Headcount data
path ='c:/Users/Danice/Desktop/clean_poverty_head.csv'
poverty_data = pd.read_csv(path,encoding="ISO-8859-1", index_col=0)

#Literacy Rate
path2 = r"C:\Users\Danice\Desktop\clean_literacy_rate.csv"
literacy_data = pd.read_csv(path2,encoding="ISO-8859-1", index_col=0)

#Secondary School Enrollment
path3 = r"C:\Users\Danice\Desktop\clean_school_enrol_sec.csv"
school2_data = pd.read_csv(path3,encoding="ISO-8859-1", index_col=0)

#Tertiary School Enrollment
path4 = r"C:\Users\Danice\Desktop\clean_school_enrol_tert.csv"
school3_data = pd.read_csv(path4,encoding="ISO-8859-1", index_col=0)

#GDP data
path5 = r"C:\Users\Danice\Desktop\clean_gdp_capita.csv"
gdp_data = pd.read_csv(path5,encoding="ISO-8859-1", index_col=0)

#Gini Index data
path6 = r"C:\Users\Danice\Desktop\clean_gini_index.csv"
gini_data = pd.read_csv(path6,encoding="ISO-8859-1", index_col=0)

#statisical summary .describe()

model = LinearRegression()
