from __future__ import print_function

import pandas as pd
pd.__version__

a=pd.Series(['San Francisco', 'San Jose', 'Sacramento'])

#print(a.values)

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

#print(pd.DataFrame({ 'City name': city_names, 'Population': population }))

#california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
#print(california_housing_dataframe.describe())

#print(california_housing_dataframe.head())

cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print(type(cities['City name']))
print(cities['City name'])

print(type(cities['City name'][1]))
print(cities['City name'][1])

print(type(cities[0:2]))
print(cities[0:2])

print(population / 1000)

import numpy as np

np.log(population)

print (population.apply(lambda val: val > 1000000))

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])

cities['Population density'] = cities['Population'] / cities['Area square miles']
print(cities)