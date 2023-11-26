#ref https://blog.stackademic.com/a-b-testing-step-by-step-guide-with-code-examples-4d626ec47536
import numpy as np
from scipy import stats

# Sample data: conversion rates of control and variant groups
control_group = np.array([0, 1, 1, 0, 0, 0, 0, 0, 1, 0])
variant_group = np.array([1, 1, 1, 0, 0, 1, 1, 0, 1, 0])

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(control_group, variant_group)

# Calculate effect size (Cohen's d)
mean_diff = np.mean(variant_group) - np.mean(control_group)
pooled_stddev = np.sqrt((np.var(control_group) + np.var(variant_group)) / 2) #to_review
effect_size = mean_diff / pooled_stddev

# Interpret results
alpha = 0.05
if p_value < alpha:
    print("Results are statistically significant.")
    if effect_size > 0.2:
        print("The effect size is practical.")
    else:
        print("Consider the practical significance of the effect.")
else:
    print("Results are not statistically significant.")
    
