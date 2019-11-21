import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

def cohen_d(x, y):
    """Cohen's d for effect size.
Standard interpretation:
Effect size   d    Reference
Very small  0.01  Sawilowsky, 2009
Small       0.20  Cohen, 1988
Medium      0.50  Cohen, 1988
Large       0.80  Cohen, 1988
Very large  1.20  Sawilowsky, 2009
Huge        2.0   Sawilowsky, 2009
"""
    nx = len(x)
    ny = len(y)
    dof = nx + ny - 2
    s_squared = ((nx - 1) * np.std(x, ddof=1) ** 2 +
                 (ny - 1) * np.std(y, ddof=1) ** 2) / dof
    return np.abs((np.mean(x) - np.mean(y)) / np.sqrt(s_squared))

def summer_v_winter(data, target):
    """Compare target for April-August months v. November-March months"""
    summer = data.query('4 <= Month <= 8')
    winter = data.query('Month <= 3 or Month >= 11')
    sns.distplot(summer[target], label='April-August')
    sns.distplot(winter[target], label='November-March')
    target_name = target.replace("_"," ")
    plt.xlabel(target_name)
    plt.title(f'{target_name.capitalize()} distribution, summer v. winter months', size=24)
    plt.legend()
    t_stat, p_value = stats.ttest_ind(summer[target], winter[target], equal_var=False)
    print(f"One-tailed t-test: t-statistic: {t_stat:.03f}; p-value: {p_value / 2}")
    print(f"Cohen's D score: {cohen_d(winter[target], summer[target]):.03f}")

def top_v_bottom(percentile, data, var, target, var_name="unusual heat"):
    """Compare target for top percentile to bottom percentile of data var.
Percentile <= .5"""
    data = data.dropna()
    q_top = np.quantile(data[var], 1 - percentile)
    q_bottom = np.quantile(data[var], percentile)
    top_target = data[data[var] >= q_top][target]
    bottom_target = data[data[var] <= q_bottom][target]
    sns.distplot(top_target, label=f'{(1 - percentile) * 100:.0f}th percentile\n{var_name}')
    sns.distplot(bottom_target, label=f'{percentile * 100:.0f}th percentile\n{var_name}')
    plt.xlabel(target.replace("_"," "),size='xx-large')
    plt.legend()
    t_stat, p_value = stats.ttest_ind(top_target, bottom_target, equal_var=False)
    print(f"One-tailed t-test: t-statistic: {t_stat:.03f}; p-value: {p_value / 2:.06f}")
    print(f"Cohen's d: {cohen_d(bottom_target, top_target):.03f}")

def data_by_month(data, drop_columns=['Year',
                                      'Year Code',
                                      'min_t_diff',
                                      'max_t_diff',
                                      'heat_index_diff']):
    """Return mean values by state and month, dropping meaningless columns."""
    # mean out the years
    # observations are states
    # group by states mean of rate by month
    data_by_month = data.groupby(['Month', 'State']).agg('mean').reset_index() \
                .drop(columns=drop_columns)
    # drop states which have fewer than 12 months of data
    data_by_state_count = data_by_month.groupby('State').count()
    low_count_states = data_by_state_count.index[(data_by_state_count < 12).Month].to_list()
    return data_by_month[~data_by_month.State.isin(low_count_states)]
