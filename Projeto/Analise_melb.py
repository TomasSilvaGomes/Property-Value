import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

melbourne = pd.read_csv('Ficheiros/melb_data.csv')
melbourne['landsize'] = melbourne['landsize'] / 10.76

def heatmap_v():
    melbourne = pd.read_csv('Ficheiros/melb_data.csv')
    melbourne = melbourne.drop(['address', 'suburb','type','councilarea','regionname','date_sold','method','sellerg'], axis=1)
    corr_matrix = melbourne.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='YlOrRd')
    plt.title('Correlação de variáves')
    plt.show()


def mean_median_mode():
    mean = melbourne['price'].mean()
    median = melbourne['price'].median()
    print('Média do preço:', mean)
    print('Mediana do preço:', median)



def mean_median_mode_bedrooms():
    mean = melbourne['bedrooms'].mean()
    median = melbourne['bedrooms'].median()
    print('\nMédia dos quartos:', mean)
    print('Mediana dos quartos:', median)

def mean_median_bathrooms():
    mean = melbourne['bathrooms'].mean()
    median = melbourne['bathrooms'].median()
    print('\nMédia das casas de banho:', mean)
    print('Mediana das casas de banho:', median)

def mean_median_car():
    mean = melbourne['car'].mean()
    median = melbourne['car'].median()
    print('\nMédia dos carros:', mean)
    print('Mediana dos carros:', median)


def count_type():
    type = melbourne['type'].value_counts()
    print(type)


def scatterplt_price_bedrooms():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='bedrooms', y='price', data=melbourne, color='skyblue')
    plt.title('Preço em relação ao número de Quartos')
    plt.xlabel('Número de Quartos')
    plt.ylabel('Preço(A$)')
    plt.show()



def scatterplt_price_bathrooms():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='bathrooms', y='price', data=melbourne, color='skyblue')
    plt.title('Preço em relação ao número de Casas de Banho')
    plt.xlabel('Número de Casas de Banho')
    plt.ylabel('Preço(A$)')
    plt.show()


def price_location():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='longitude', y='latitude', data=melbourne, hue='price', palette='coolwarm')
    plt.title('Preço em Relação à Localização Geográfica')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()
def table_bedrooms_buildyear():
    table = pd.crosstab(melbourne['bedrooms'], melbourne['yearbuilt'])
    print(table)

def frequency_table_bedrooms():
    table = melbourne['bedrooms'].value_counts()
    print(table)

def frequency_table_yearbuilt():
    table = melbourne['yearbuilt'].value_counts()
    print(table)

def number_suburbs():
    number = melbourne['suburb'].value_counts()
    print(number)


def circular_graphic():
    plt.figure(figsize=(10, 6))
    melbourne['type'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
    plt.title('Tipos de Edifícios')
    plt.ylabel('')
    plt.show()


def table_council_area():
    table = melbourne['councilarea'].value_counts()
    print(table)


def region_name():
    region = melbourne['regionname'].value_counts()
    print(region)



def disp_price_landsize():
    plt.figure(figsize=(10, 6))
    sns.regplot(x='landsize', y='price', data=melbourne)
    plt.xlim(0, 100000)
    plt.title('Preço em relação ao Tamanho do Terreno')
    plt.xlabel('Tamanho do terreno (m²)')
    plt.ylabel('Preço(A$)')
    plt.show()


def price_method():
    plt.figure(figsize=(12, 6))
    melbourne.groupby('method')['price'].mean().plot(kind='bar', color='skyblue')
    plt.title('Preço por método de venda')
    plt.xlabel('Método de Venda')
    plt.ylabel('Preço(A$)')
    plt.xticks(rotation=0)
    plt.show()

def disp_price_landsize_outlier():
    plt.figure(figsize=(10, 6))
    sns.regplot(x='landsize', y='price', data=melbourne)
    plt.xlim(0, 450000)
    plt.title('Preço em relação ao Tamanho do Terreno')
    plt.xlabel('Tamanho do terreno (m²)')
    plt.ylabel('Preço(A$)')
    plt.show()


''' Se necessário visualizar algum gráfico, basta descomentar a função correspondente. '''
# print(melbourne.isnull().sum())
# heatmap_v()
#mean_median_mode()
# mean_median_mode_bedrooms()
# mean_median_bathrooms()
# mean_median_car()
# count_type()
# price_location()
# scatterplt_price_bedrooms()
# scatterplt_price_bathrooms()
# table_bedrooms_buildyear()
# frequency_table_bedrooms()
# frequency_table_yearbuilt()
# number_suburbs()
# circular_graphic()
# table_council_area()
# disp_price_landsize()
# price_method()
#disp_price_landsize_outlier() #Em caso de querer ver o grafico inteiro com um unico outlier nitido.


