
from Projeto import *

#Mostrar o numero de outliers em cada variavel:
def outliers():
    print('Numero de outliers em cada variavel:')
    print('Perth:')
    print('Price:', len(perth[perth['price'] > perth['price'].mean() + 3 * perth['price'].std()]))
    print('Bedrooms:', len(perth[perth['bedrooms'] > perth['bedrooms'].mean() + 3 * perth['bedrooms'].std()]))
    print('Bathrooms:', len(perth[perth['bathrooms'] > perth['bathrooms'].mean() + 3 * perth['bathrooms'].std()]))
    print('Landsize:', len(perth[perth['landsize'] > perth['landsize'].mean() + 3 * perth['landsize'].std()]))
    print('Melbourne:')
    print('Price:', len(melbourne[melbourne['price'] > melbourne['price'].mean() + 3 * melbourne['price'].std()]))
    print('Bedrooms:', len(melbourne[melbourne['bedrooms'] > melbourne['bedrooms'].mean() + 3 * melbourne['bedrooms'].std()]))
    print('Bathrooms:', len(melbourne[melbourne['bathrooms'] > melbourne['bathrooms'].mean() + 3 * melbourne['bathrooms'].std()]))
    print('Landsize:', len(melbourne[melbourne['landsize'] > melbourne['landsize'].mean() + 3 * melbourne['landsize'].std()]))
    print('Delhi:')
    print('Price:', len(delhi[delhi['price'] > delhi['price'].mean() + 3 * delhi['price'].std()]))
    print('Bedrooms:', len(delhi[delhi['bedrooms'] > delhi['bedrooms'].mean() + 3 * delhi['bedrooms'].std()]))
    print('Bathrooms:', len(delhi[delhi['bathrooms'] > delhi['bathrooms'].mean() + 3 * delhi['bathrooms'].std()]))
    print('Landsize:', len(delhi[delhi['landsize'] > delhi['landsize'].mean() + 3 * delhi['landsize'].std()]))
outliers()

#Tratamento dos outliers usando funcoes log:
def tratamento_outliers():
    print('Tratamento dos outliers:')
    print('Perth:')
    perth['price'] = np.log(perth['price'])
    perth['bedrooms'] = np.log(perth['bedrooms'])
    perth['bathrooms'] = np.log(perth['bathrooms'])
    perth['landsize'] = np.log(perth['landsize'])
    print('Melbourne:')
    melbourne['price'] = np.log(melbourne['price'])
    melbourne['bedrooms'] = np.log(melbourne['bedrooms'])
    melbourne['bathrooms'] = np.log(melbourne['bathrooms'])
    melbourne['landsize'] = np.log(melbourne['landsize'])
    print('Delhi:')
    delhi['price'] = np.log(delhi['price'])
    delhi['bedrooms'] = np.log(delhi['bedrooms'])
    delhi['bathrooms'] = np.log(delhi['bathrooms'])
    delhi['landsize'] = np.log(delhi['landsize'])
tratamento_outliers()