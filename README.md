# Team3_2020 - The Role of Education in Poverty Alleviation: A Cross Country Analysis

## 0. Hypothesis
  - Hypothesis 1: The income growth of an individual will negatively affect the incidence of poverty.
  - Hypothesis 2: The education level attained by an individual will negatively affect the incidence of poverty.
  - Hypothesis 3: The income growth will have a greater effect on the incidence of poverty than the education level attained by the individual.

## 1. Project Description
  - This project Rensselaer Polytechnic Institute (RPI) ITWS 6350 Final Project
  - The goal of our project was to go through the three hypothesis that we created and determine results that would help poverty eradication
  
## 2. Data Description
  - For our data we collected datasets from the world bank databank that we believed would help contribute to our hypothesis, the datasets were:
    - GDP per Capita
    - Gini Index
    - Literacy rate, adult total
    - Poverty headcount ratio at 1.90 dollar per day
    - School enrollment, secondary (% gross)
    - School enrollment, tertiary (% gross)
  - Datasets are seperated into Non-Clean data and Clean data
  
### 2.1 GDP per Capita
  - GDP per capita (current US$) is gross domestic product divided by midyear population. 
  - Source: https://data.worldbank.org/indicator/NY.GDP.PCAP.CD
  - Files associated: 
    - 2.1.1 gdp_per_capita.xls (raw data - Downloaded from the Web) 
    - 2.1.2 gdp_per_capita.csv (Changed format so we could work with it)
    - 2.1.3 _meta_gdp_per_capita.csv (Metadata of dataset)
    - 2.1.4 clean_gdp_capita.csv (cleased data)
   - data size: 264 x 64
   - Missing data is interpolated/extrapolated.
   - Region and IncomeGroup column are added in the dataset

### 2.2 Gini Index
   - Gini index measures the extent to which the distribution of income (or, in some cases, consumption expenditure) 
     among individuals or households within an economy deviates from a perfectly equal distribution. 
   - Source: https://data.worldbank.org/indicator/SI.POV.GINI
   - Files associated:
    - 2.2.1 gini_index_xls (raw data - Downloaded from the Web) 
    - 2.2.2 gini_index_csv Changed format so we could work with it)
    - 2.2.3 _meta_gini_index.csv (Metadata of dataset)
    - 2.2.4 clean_gini_index.csv (cleased data)
   - data size: 264 x 64
   - Missing data is interpolated/extrapolated.
   - Region and IncomeGroup column are added in the dataset

### 2.3 Literacy rate, adult total
   - Adult literacy rate is the percentage of people ages 15 and above who can both read and write with 
     understanding a short simple statement about their everyday life.
   - Source: https://data.worldbank.org/indicator/SE.ADT.LITR.ZS
   - Files associated:
     - 2.3.1 Literacy rate, adult total.xls (raw data - Downloaded from the Web) 
     - 2.3.2 literacy_rate_adult_total.csv (Changed format so we could work with it)
     - 2.3.3 _meta_literacy_rate_adult_total.csv (Metadata of dataset)
     - 2.3.4 clean_literacy_rate.csv (cleased data)
   - data size: 264 x 64
   - Missing data is interpolated/extrapolated.
   - Region and IncomeGroup column are added in the dataset

### 2.4 Poverty headcount ratio at 1.90 dollar per day
   - Poverty headcount ratio at $1.90 a day is the percentage of the population living on less than 
     $1.90 a day at 2011 international prices. 
   - Source: https://data.worldbank.org/indicator/SI.POV.DDAY
   - Files associated:
    - 2.4.1 poverty headcount ratio at 1.90 dollar per day.xls (raw data - Downloaded from the Web) 
    - 2.4.2 poverty_headcount_ratio_1.90.csv (Changed format so we could work with it)
    - 2.4.3 _meta_poverty_headcount_ratio_1.90.csv (Metadata of dataset)
    - 2.4.4 clean_poverty_head.csv (cleased data)
   - data size: 264 x 64
   - Missing data is interpolated/extrapolated.
   - Region and IncomeGroup column are added in the dataset

### 2.5 School enrollment, secondary (% gross)
   - Gross enrollment ratio is the ratio of total enrollment, regardless of age, to the population of the age group that 
    officially corresponds to the level of education shown.
   - Source: https://data.worldbank.org/indicator/SE.SEC.ENRR
   -Files associated:
    - 2.5.1 School enrollment, secondary (% gross).xls (raw data - Downloaded from the Web) 
    - 2.5.2 school enrollment_secondary.csv (Changed format so we could work with it)
    - 2.5.3 _meta_school enrollment_secondary.csv (Metadata of dataset)
    - 2.5.4 clean_school_enrol_sec.csv (cleased data)
  - data size: 264 x 64
  - Missing data is interpolated/extrapolated.
  - Region and IncomeGroup column are added in the dataset

### 2.6 School enrollment, tertiary (% gross)
  - Gross enrollment ratio is the ratio of total enrollment, regardless of age, to the population of the age group that 
    officially corresponds to the level of education shown. 
  - Source: https://data.worldbank.org/indicator/SE.TER.ENRR
  - Files accessed:
    - 2.6.1 School enrollment, tertiary (% gross).xls (raw data - Downloaded from the Web) 
    - 2.6.2 school_enrollment_tertiary.csv (Changed format so we could work with it)
    - 2.6.3 _meta_school enrollment_tertiary.csv (Metadata of dataset)
    - 2.6.4 clean_school_enrol_tert.csv (cleased data)
  - data size: 264 x 64
  - Missing data is interpolated/extrapolated.
  - Region and IncomeGroup column are added in the dataset

# 3. Data Cleasing
  - code is located in code folder under data_cleansing.R

## 3.1 Interpolation
  - Missing data is interpolated with linear interpolation between two values. 
  - R function, "na.fill" is used to interpolate missing values.

## 3.2 Extrapolation
  - Missing data is replaced with the first value/the last value. 
  - ex) na, na, na, 1, 3, 5, 7, na, na  ===> 1, 1, 1, 1, 3, 5, 7, 7, 7

# 4. Data Analytics
  - Code is located in code folder in two notebook files:
    - K-Means Clustering : Clustering - Poverty.ipynb
    - Linear Regression : Regression - Poverty.ipynb
