
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df_max = pd.read_excel(r"E:\SelfStudy\datasets\ab_testing.xlsx", sheet_name="Control Group")
df_avr = pd.read_excel(r"E:\SelfStudy\datasets\ab_testing.xlsx", sheet_name="Test Group")
df_max.head()
df_avr.head()
# Task 1 : Define the hypothesis of the A/B test.

#H0= There is no statistically significant difference in conversion between the current bidding type and the new bidding type.
#H1= There is a significant difference.

df_max["Purchase"].mean() # --> 550.8940587702316
df_avr["Purchase"].mean() # --> 582.1060966484675

#Task 2 : Statistically the test results comment whether it is significant or not.


# The Assumptions of normality
# H0: Assumption of normal distribution is provided.
# H1: Assumption of normal distribution is not provided.

test_stat, pvalue = shapiro(df_max["Purchase"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value = 0.5891

test_stat, pvalue = shapiro(df_avr["Purchase"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
#p-value = 0.1541

#Because of the p-value is not less than 0.05 H0:Irrefutable

# Homogeneity of variance
# H0: Variances are homogeneous
# H1: Variances are not homogeneous

test_stat, pvalue = levene(df_max["Purchase"].dropna(),
                           df_avr["Purchase"].dropna())

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
#p-value = 0.1083

#Because of the p-value is not less than 0.05 H0:Irrefutable

#Due to the variance was provided, parametric tests will be applied
 
test_stat, pvalue = ttest_ind(df_max["Purchase"],
                              df_avr["Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#p-value = 0.3493

#Because of the p-value is not less than 0.05 H0:Irrefutable


#Task 3 Which tests did you use? Specify the reasons.

#In the application of two independent samples t-test, the assumptions of normal distribution and homogeneous distribution were tested first.
#We tested the assumptions of normal distribution with shapiro method and the homogeneous distribution with Levene methods.
#If the assumptions are met, the parametric method is used, if not, the nonparametric method is applied.
#Since we observed that the assumptions were met in our study, we applied the parametric method, the t-test.
# As a result, we observed that the H0 hypothesis is irrefutable.

#Task 4

#When the data examined between the old system and the new system, there was no statistically significant difference.
#If it is increasing based on clicks per impression, we may recommend that the customer continue the experiments and follow the process.


df_max["Conversion_Rate"]=df_max["Click"]/df_max["Impression"]
df_avr["Conversion_Rate"]=df_avr["Click"]/df_avr["Impression"]
df_max["Conversion_Rate"].mean() #--> 0.05361823086521901
df_avr["Conversion_Rate"].mean() #--> 0.03417599154362739



#Ho=There is no significant difference in conversion rates between the two systems.
#H1=There is significant difference in conversion rates between the two systems

#The Assumptions of normality

# H0: Assumption of normal distribution is provided.
# H1: Assumption of normal distribution is not provided

test_stat, pvalue = shapiro(df_max["Conversion_Rate"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value = 0.0000

test_stat, pvalue = shapiro(df_avr["Conversion_Rate"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value = 0.0001

#H0:Rejected. The normality assumption is rejected. Therefore, the Nonparametric method will be applied.

test_stat, pvalue = mannwhitneyu(df_max["Conversion_Rate"].dropna(),
                                 df_avr["Conversion_Rate"].dropna())

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
#p-value = 0.0000

#H0=Rejected. 
#Due to the conversion rate increase is statistically significant, we can recommend the customer to extend the experiments and follow the process.


