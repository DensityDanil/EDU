{
 control_group:np.array([0, 1, 1, 0, 0, 0, 0, 0, 1, 0])
,variant_group:np.array([1, 1, 1, 0, 0, 1, 1, 0, 1, 0])
,t_statistic:stats.ttest_ind(control_group, variant_group)[0]
,p_value:stats.ttest_ind(control_group, variant_group)[1]
,mean_diff:np.mean(variant_group) - np.mean(control_group)
,pooled_stddev:np.sqrt((np.var(control_group) + np.var(variant_group)) / 2)
,effect_size:mean_diff / pooled_stddev
}
