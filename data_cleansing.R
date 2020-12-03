#################################################################################################################################
######    DataScience Final Project    ##########################################################################################
#################################################################################################################################

####    Setting    ####

library(dplyr)
library(data.table)    
setwd("C:\\000. Class\\008. 2020 Fall_RPI\\DataScience_2020\\Assignment_4\\001. raw_data")


#### Data Cleasing ####

#### 1. Literacy rate, adult total % of People ####

meta_literacy_rate = read.csv("_meta_literacy_rate_adult_total.csv", header = TRUE)
colnames(meta_literacy_rate)[5] = c("Country.Name")

raw_literacy_rate = read.csv("literacy_rate_adult_total.csv", header = TRUE)
raw_literacy_rate = raw_literacy_rate[,c(-2,-3,-4)]

literacy_rate = melt(as.data.table(raw_literacy_rate), id.vars='Country.Name', variable.name='year')  
literacy_rate[, year := as.integer(sub('[[:alpha:]]', '', year))]                      
literacy_rate = literacy_rate %>% arrange(Country.Name, year)

country_name    = literacy_rate$Country.Name %>% unique
list_by_country = list()

for (i in 1: (country_name %>% length)  )
{
  list_by_country[[i]]   = literacy_rate[which(literacy_rate$Country.Name %in% country_name[i]),]
  
  # Interpolate/Extrapolate only if there are more than two vallues.
  if (sum(is.na(list_by_country[[i]]$value)) < 60)
  {
    list_by_country[[i]]   = list_by_country[[i]] %>% mutate_at(3, ~na.fill(.x,"extend")) 
  }
  if (i == 1)
  {
    literacy_rate.int = list_by_country[[i]]
  }else{
    literacy_rate.int = rbind(literacy_rate.int, list_by_country[[i]] )
  }
}

literacy_rate.int.vf = dcast(literacy_rate.int, Country.Name~year)
literacy_rate.int.vf = left_join(meta_literacy_rate[,c("Country.Name", "Region", "IncomeGroup")], literacy_rate.int.vf, by = "Country.Name")

write.csv(literacy_rate.int.vf, "clean_literacy_rate.csv")




#### 2. School Enrollment, Tertiary (% gross) ####

meta_school_enrol_tert = read.csv("_meta_school enrollment_tertiary.csv", header = TRUE)
colnames(meta_school_enrol_tert)[5] = c("Country.Name")

raw_school_enrol_tert = read.csv("school_enrollment_tertiary.csv", header = TRUE)
raw_school_enrol_tert = raw_school_enrol_tert[,c(-2,-3,-4)]

school_enrol_tert = melt(as.data.table(raw_school_enrol_tert), id.vars='Country.Name', variable.name='year')  
school_enrol_tert[, year := as.integer(sub('[[:alpha:]]', '', year))]                      
school_enrol_tert = school_enrol_tert %>% arrange(Country.Name, year)

country_name    = school_enrol_tert$Country.Name %>% unique
list_by_country = list()

for (i in 1: (country_name %>% length)  )
{
  list_by_country[[i]]   = school_enrol_tert[which(school_enrol_tert$Country.Name %in% country_name[i]),]
  
  # Interpolate/Extrapolate only if there are more than two vallues.
  if (sum(is.na(list_by_country[[i]]$value)) < 60)
  {
    list_by_country[[i]]   = list_by_country[[i]] %>% mutate_at(3, ~na.fill(.x,"extend")) 
  }
  if (i == 1)
  {
    school_enrol_tert.int = list_by_country[[i]]
  }else{
    school_enrol_tert.int = rbind(school_enrol_tert.int, list_by_country[[i]] )
  }
}

school_enrol_tert.int.vf = dcast(school_enrol_tert.int, Country.Name~year)
school_enrol_tert.int.vf = left_join(meta_school_enrol_tert[,c("Country.Name", "Region", "IncomeGroup")], school_enrol_tert.int.vf, by = "Country.Name")

write.csv(school_enrol_tert.int.vf, "clean_school_enrol_tert.csv")




#### 3. School Enrollment, Secondary (% gross) ####

meta_school_enrol_sec = read.csv("_meta_school enrollment_secondary.csv", header = TRUE)
colnames(meta_school_enrol_sec)[5] = c("Country.Name")

raw_school_enrol_sec = read.csv("school enrollment_secondary.csv", header = TRUE)
raw_school_enrol_sec = raw_school_enrol_sec[,c(-2,-3,-4)]

school_enrol_sec = melt(as.data.table(raw_school_enrol_sec), id.vars='Country.Name', variable.name='year')  
school_enrol_sec[, year := as.integer(sub('[[:alpha:]]', '', year))]                      
school_enrol_sec = school_enrol_sec %>% arrange(Country.Name, year)

country_name    = school_enrol_sec$Country.Name %>% unique
list_by_country = list()

for (i in 1: (country_name %>% length)  )
{
  list_by_country[[i]]   = school_enrol_sec[which(school_enrol_sec$Country.Name %in% country_name[i]),]
  
  # Interpolate/Extrapolate only if there are more than two vallues.
  if (sum(is.na(list_by_country[[i]]$value)) < 60)
  {
    list_by_country[[i]]   = list_by_country[[i]] %>% mutate_at(3, ~na.fill(.x,"extend")) 
  }
  if (i == 1)
  {
    school_enrol_sec.int = list_by_country[[i]]
  }else{
    school_enrol_sec.int = rbind(school_enrol_sec.int, list_by_country[[i]] )
  }
}

school_enrol_sec.int.vf = dcast(school_enrol_sec.int, Country.Name~year)
school_enrol_sec.int.vf = left_join(meta_school_enrol_sec[,c("Country.Name", "Region", "IncomeGroup")], school_enrol_sec.int.vf, by = "Country.Name")

write.csv(school_enrol_sec.int.vf, "clean_school_enrol_sec.csv")




#### 4. Poverty Headcount ratio_1.90 dollar per day ####

meta_poverty = read.csv("_meta_poverty_headcount_ratio_1.90.csv", header = TRUE)
colnames(meta_poverty)[5] = c("Country.Name")

raw_poverty_head = read.csv("poverty_headcount_ratio_1.90.csv", header = TRUE)
raw_poverty_head = raw_poverty_head[,c(-2,-3,-4)]

poverty_head = melt(as.data.table(raw_poverty_head), id.vars='Country.Name', variable.name='year')  
poverty_head[, year := as.integer(sub('[[:alpha:]]', '', year))]                      
poverty_head = poverty_head %>% arrange(Country.Name, year)

country_name    = poverty_head$Country.Name %>% unique
list_by_country = list()

for (i in 1: (country_name %>% length)  )
{
  list_by_country[[i]]   = poverty_head[which(poverty_head$Country.Name %in% country_name[i]),]
  
  # Interpolate/Extrapolate only if there are more than two vallues.
  if (sum(is.na(list_by_country[[i]]$value)) < 60)
  {
    list_by_country[[i]]   = list_by_country[[i]] %>% mutate_at(3, ~na.fill(.x,"extend")) 
  }
  if (i == 1)
  {
    poverty_head.int = list_by_country[[i]]
  }else{
    poverty_head.int = rbind(poverty_head.int, list_by_country[[i]] )
  }
}

poverty_head.int.vf = dcast(poverty_head.int, Country.Name~year)
poverty_head.int.vf = left_join(meta_poverty[,c("Country.Name", "Region", "IncomeGroup")], poverty_head.int.vf, by = "Country.Name")

write.csv(poverty_head.int.vf, "clean_poverty_head.csv")




#### 5. Gini Index ####

meta_gini = read.csv("_meta_gini_index.csv", header = TRUE)
colnames(meta_gini)[5] = c("Country.Name")

raw_gini_head = read.csv("gini_index.csv", header = TRUE)
raw_gini_head = raw_gini_head[,c(-2,-3,-4)]

gini_head = melt(as.data.table(raw_gini_head), id.vars='Country.Name', variable.name='year')  
gini_head[, year := as.integer(sub('[[:alpha:]]', '', year))]                      
gini_head = gini_head %>% arrange(Country.Name, year)

country_name    = gini_head$Country.Name %>% unique
list_by_country = list()

for (i in 1: (country_name %>% length)  )
{
  list_by_country[[i]]   = gini_head[which(gini_head$Country.Name %in% country_name[i]),]
  
  # Interpolate/Extrapolate only if there are more than two vallues.
  if (sum(is.na(list_by_country[[i]]$value)) < 60)
  {
    list_by_country[[i]]   = list_by_country[[i]] %>% mutate_at(3, ~na.fill(.x,"extend")) 
  }
  if (i == 1)
  {
    gini_head.int = list_by_country[[i]]
  }else{
    gini_head.int = rbind(gini_head.int, list_by_country[[i]] )
  }
}

gini_head.int.vf = dcast(gini_head.int, Country.Name~year)
gini_head.int.vf = left_join(meta_gini[,c("Country.Name", "Region", "IncomeGroup")], gini_head.int.vf, by = "Country.Name")

write.csv(gini_head.int.vf, "clean_gini_index.csv")




#### 6. GDP per capita ####

meta_gdp_capita = read.csv("_meta_gdp_per_capita.csv", header = TRUE)
colnames(meta_gdp_capita)[5] = c("Country.Name")

raw_gdp_capita = read.csv("gdp_per_capita.csv", header = TRUE)
raw_gdp_capita = raw_gdp_capita[,c(-2,-3,-4)]

gdp_capita = melt(as.data.table(raw_gdp_capita), id.vars='Country.Name', variable.name='year')  
gdp_capita[, year := as.integer(sub('[[:alpha:]]', '', year))]                      
gdp_capita = gdp_capita %>% arrange(Country.Name, year)

country_name    = gdp_capita$Country.Name %>% unique
list_by_country = list()

for (i in 1: (country_name %>% length)  )
{
  list_by_country[[i]]   = gdp_capita[which(gdp_capita$Country.Name %in% country_name[i]),]
  
  # Interpolate/Extrapolate only if there are more than two vallues.
  if (sum(is.na(list_by_country[[i]]$value)) < 60)
  {
    list_by_country[[i]]   = list_by_country[[i]] %>% mutate_at(3, ~na.fill(.x,"extend")) 
  }
  if (i == 1)
  {
    gdp_capita.int = list_by_country[[i]]
  }else{
    gdp_capita.int = rbind(gdp_capita.int, list_by_country[[i]] )
  }
}

gdp_capita.int.vf = dcast(gdp_capita.int, Country.Name~year)
gdp_capita.int.vf = left_join(meta_gini[,c("Country.Name", "Region", "IncomeGroup")], gdp_capita.int.vf, by = "Country.Name")

write.csv(gdp_capita.int.vf, "clean_gdp_capita.csv")















