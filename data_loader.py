import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

def load_suicides(filename):
    suicides = pd.read_csv(filename, sep='\t', na_values='Not Applicable')
    suicides = suicides.dropna(subset=['State']) # Remove trailing rows
    suicides = suicides.drop(columns=['Notes', 'Crude Rate', 'Population'])
    suicides['Month'] = suicides['Month Code'].str.slice(-2).astype(np.int64)
    return suicides

def load_suicides_pop(filename):
    suicides_pop = pd.read_csv(filename, sep='\t', na_values='Not Applicable')
    suicides_pop = suicides_pop.dropna(subset=['State'])
    suicides_pop = suicides_pop.drop(columns='Notes')
    return suicides_pop

def calculate_suicide_rate(suicides, suicides_pop):
    suicides['Population'] = suicides.merge(suicides_pop, on=['State', 'Year'])['Population']
    suicides['suicide_rate'] = suicides.Deaths / suicides.Population * 100_000
    return suicides

def load_heat(filename):
    heat = pd.read_csv('data/temps_by_state_month_1999_2011.txt', sep='\t', na_values='Missing')
    heat = heat.dropna(subset=['State'])
    heat['Month'] = heat['Month, Year Code'].str.slice(-2).astype(np.int64)
    heat['Year'] = heat['Month, Year Code'].str.slice(0, 4).astype(np.int64)
    heat = heat.drop(columns='Notes')
    heat = heat.rename(columns={'Avg Daily Max Air Temperature (F)':'avg_max_t',
                    'Avg Daily Min Air Temperature (F)':'avg_min_t',
                    'Avg Daily Max Heat Index (F)':'avg_max_heat_index',
                    'Month, Year Code' : 'Month Code'})
    return heat

def calc_mean_diff(data, var):
    return data['var'] - data.groupby(['State', 'Month'])['var'].transform('mean')

def add_heat_to_suicides(suicides, heat):
    suicides = suicides.merge(heat[['State',
                                'Month Code',
                                'avg_max_t',
                                'avg_min_t',
                                'avg_max_heat_index']],
                            on=['State', 'Month Code'])
    suicides['min_t_diff'] = calc_mean_diff(suicides, 'avg_min_t')
    suicides['max_t_diff'] = calc_mean_diff(suicides, 'avg_max_t')
    suicides['heat_index_diff'] = calc_mean_diff(suicides, 'avg_max_heat_index')
    return suicides


def parser(x):
	return pd.datetime.strptime(x, '%Y/%m')

def load_final(filename):
    return pd.read_csv(filename, parse_dates=['Month Code'], index_col=0, date_parser=parser)
