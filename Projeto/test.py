import numpy as np
import pandas as pd


print(" \nTotal number of null values:" )
print(data.isnull().sum())


data = pd.read_csv('ficheiro_analise.csv')
numeric_data = data.select_dtypes(include=[np.number])
Q1 = numeric_data.quantile(0.25)
Q3 = numeric_data.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_count = ((numeric_data < lower_bound) | (numeric_data > upper_bound)).sum()
print('Outliers count:')
print(outliers_count)

data  = pd.read_csv('ficheiro_analise.csv')


print(" \nDescreption of the data:")
print(data.describe())
