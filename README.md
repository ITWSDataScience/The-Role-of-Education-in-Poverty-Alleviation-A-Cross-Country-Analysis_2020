# Team3_2020


###########################################################################################################
# 0. Hypothesis
###########################################################################################################
: Income growth affects more the incidence of poverty than education level.



###########################################################################################################
# 1. Data Description
###########################################################################################################
# 1.1 GDP per Capita
#  - GDP per capita (current US$) is gross domestic product divided by midyear population. 
#  - Source: https://data.worldbank.org/indicator/NY.GDP.PCAP.CD
# 1.1.1 gdp_per_capita.xls (raw data - Downloaded from the Web) 
# 1.1.2 gdp_per_capita.csv
# 1.1.3 _meta_gdp_per_capita.csv
# 1.1.4 clean_gdp_capita.csv (cleased data)
#  - data size: 264 x 64
#  - Missing data is interpolated/extrapolated.
#  - Region and IncomeGroup column are added in the dataset

# 1.2 Gini Index
#  - Gini index measures the extent to which the distribution of income (or, in some cases, consumption expenditure) 
#    among individuals or households within an economy deviates from a perfectly equal distribution. 
#  - Source: https://data.worldbank.org/indicator/SI.POV.GINI
# 1.2.1 gini_index_xls (raw data - Downloaded from the Web) 
# 1.2.2 gini_index_csv 
# 1.2.3 _meta_gini_index.csv 
# 1.2.4 clean_gini_index.csv (cleased data)
#  - data size: 264 x 64
#  - Missing data is interpolated/extrapolated.
#  - Region and IncomeGroup column are added in the dataset

# 1.3 Literacy rate, adult total
#  - Adult literacy rate is the percentage of people ages 15 and above who can both read and write with 
#    understanding a short simple statement about their everyday life.
#  - Source: https://data.worldbank.org/indicator/SE.ADT.LITR.ZS
# 1.3.1 Literacy rate, adult total.xls (raw data - Downloaded from the Web) 
# 1.3.2 literacy_rate_adult_total.csv 
# 1.3.3 _meta_literacy_rate_adult_total.csv 
# 1.3.4 clean_literacy_rate.csv (cleased data)
#  - data size: 264 x 64
#  - Missing data is interpolated/extrapolated.
#  - Region and IncomeGroup column are added in the dataset

# 1.4 Poverty headcount ratio at 1.90 dollar per day
#  - Poverty headcount ratio at $1.90 a day is the percentage of the population living on less than 
#    $1.90 a day at 2011 international prices. 
#  - Source: https://data.worldbank.org/indicator/SI.POV.DDAY
# 1.4.1 poverty headcount ratio at 1.90 dollar per day.xls (raw data - Downloaded from the Web) 
# 1.4.2 poverty_headcount_ratio_1.90.csv
# 1.4.3 _meta_poverty_headcount_ratio_1.90.csv
# 1.4.4 clean_poverty_head.csv (cleased data)
#  - data size: 264 x 64
#  - Missing data is interpolated/extrapolated.
#  - Region and IncomeGroup column are added in the dataset

# 1.5 School enrollment, secondary (% gross)
#  - Gross enrollment ratio is the ratio of total enrollment, regardless of age, to the population of the age group that 
#    officially corresponds to the level of education shown.
#  - Source: https://data.worldbank.org/indicator/SE.SEC.ENRR
# 1.5.1 School enrollment, secondary (% gross).xls (raw data - Downloaded from the Web) 
# 1.5.2 school enrollment_secondary.csv
# 1.5.3 _meta_school enrollment_secondary.csv
# 1.5.4 clean_school_enrol_sec.csv (cleased data)
#  - data size: 264 x 64
#  - Missing data is interpolated/extrapolated.
#  - Region and IncomeGroup column are added in the dataset

# 1.6 School enrollment, tertiary (% gross)
#  - Gross enrollment ratio is the ratio of total enrollment, regardless of age, to the population of the age group that 
#    officially corresponds to the level of education shown. 
#  - Source: https://data.worldbank.org/indicator/SE.TER.ENRR
# 1.6.1 School enrollment, tertiary (% gross).xls (raw data - Downloaded from the Web) 
# 1.6.2 school_enrollment_tertiary.csv
# 1.6.3 _meta_school enrollment_tertiary.csv
# 1.6.4 clean_school_enrol_tert.csv (cleased data)
#  - data size: 264 x 64
#  - Missing data is interpolated/extrapolated.
#  - Region and IncomeGroup column are added in the dataset

###########################################################################################################
# 2. Data Cleasing
###########################################################################################################

# 2.1 Interpolation
# - Missing data is interpolated with linear interpolation between two values. 
# - R function, "na.fill" is used to interpolate missing values.

# 2.2 Extrapolation
# - Missing data is replaced with the first value/the last value. 
# - ex) na, na, na, 1, 3, 5, 7, na, na  ===> 1, 1, 1, 1, 3, 5, 7, 7, 7



