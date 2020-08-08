#Descriptive Statistics With Pandas
import pandas as pd 
import numpy as np
import matplotlib
# matplotlib inline
 


animals = pd.read_csv('/Users/anielkaaslan/Downloads/animals.csv')
animals.boxplot()
# print(animals.dtypes)
# print(animals.head())
# print(animals.describe())
# print(animals.min())
# print(animals.max())
# print(animals.std())
# print(animals.mean())
# print(animals.median())
