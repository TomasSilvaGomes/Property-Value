import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

perth = pd.read_csv('Ficheiros/perth_file.csv')


def heatmap_v():
    perth = pd.read_csv('Ficheiros/perth_file.csv')
    perth = perth.drop(['address', 'suburb','nearest_stn','nearest_sch','date_sold'], axis=1)
    corr_matrix = perth.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='YlOrRd')
    plt.title('Correlação de variáves')
    plt.show()



def hist_price():
    perth['price'] = perth['price'] / 1e6
    plt.hist(perth['price'], bins=100, color='purple')
    plt.title('Gráfico do preço')
    plt.xlabel('Preço (em Milhões)')
    plt.ylabel('Frequência')
    plt.show()


def mean_median_mode():
    mean = perth['price'].mean()
    median = perth['price'].median()
    mode = perth['price'].mode()
    print('Média do preço:', mean)
    print('Mediana do preço:', median)
    print('Moda do preço:', mode)



def plt_price_bedrooms():
    perth['price_millions'] = perth['price'] / 1e6
    # Create a bar plot of price (in millions) vs. bedrooms
    plt.figure(figsize=(12, 6))
    perth.groupby('bedrooms')['price_millions'].mean().plot(kind='bar', color='skyblue')
    plt.title('Average Price (in Millions) by Number of Bedrooms')
    plt.xlabel('Numero de Quartos')
    plt.ylabel('Average Price (Millions)')
    plt.xticks(rotation=0)
    plt.show()


def mean_median_mode_bedrooms():
    mean = perth['bedrooms'].mean()
    median = perth['bedrooms'].median()
    mode = perth['bedrooms'].mode()
    print('\nMédia dos quartos:', mean)
    print('Mediana dos quartos:', median)
    print('Moda dos quartos:', mode)

def mean_median_mode_bathrooms():
    mean = perth['bathrooms'].mean()
    median = perth['bathrooms'].median()
    mode = perth['bathrooms'].mode()
    print('\nMédia das casas de banho:', mean)
    print('Mediana das casas de banho:', median)
    print('Moda das casas de banho:', mode)

def sold_date():
    sold_date = perth['date_sold'].value_counts()
    print(sold_date)

def table_bedrooms_buildyear():
    table = pd.crosstab(perth['bedrooms'], perth['yearbuilt'])
    print(table)

def disp_price_landsize():
    perth['price_millions'] = perth['price'] / 1e6
    plt.figure(figsize=(10, 6))
    sns.regplot(x='landsize', y='price_millions', data=perth)
    plt.title('Preço em relação ao Tamanho do Terreno')
    plt.xlabel('Tamanho do terreno (m²)')
    plt.ylabel('Preço (Milhões)')
    plt.show()


def frequency_table_bedrooms():
    table = perth['bedrooms'].value_counts()
    print(table)

def frequency_table_yearbuilt():
    table = perth['yearbuilt'].value_counts()
    print(table)

def number_suburbs():
    number = perth['suburb'].value_counts()
    print(number)

def price_garages():
    perth['price_millions'] = perth['price'] / 1e6
    plt.figure(figsize=(10, 6))
    perth.groupby('garage')['price_millions'].mean().plot(kind='bar', color='blue')
    plt.title('Gráfico de Dispersão: Preço (em Milhões) vs. Quantidade de Garagens')
    plt.xlabel('Quantidade de Garagens (Máx: 20)')
    plt.ylabel('Preço (Milhões)')
    plt.xticks(rotation=0)
    plt.show()


def mean_median_mode_garages():
    mean = perth['garage'].mean()
    median = perth['garage'].median()
    mode = perth['garage'].mode()
    print('\nMédia das garagens:', mean)
    print('Mediana das garagens:', median)

    print('Moda das garagens:', mode)


def price_location():
    perth['price_millions'] = perth['price'] / 1e6
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='longitude', y='latitude', data=perth, hue='price_millions', palette='coolwarm')
    plt.title('Preço em Relação à Localização Geográfica')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()

#Preço em relação ao Ano de Construção:
def price_yearbuilt():
    perth['price_millions'] = perth['price'] / 1e6
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='yearbuilt', y='price_millions', data=perth, hue='price_millions', palette='coolwarm')
    plt.title('Preço em Relação ao Ano de Construção')
    plt.xlabel('Ano de Construção')
    plt.ylabel('Preço (Milhões)')
    plt.show()


# heatmap_v()
# hist_price()
# mean_median_mode()
# plt_price_bedrooms()
# mean_median_mode_bedrooms()
# mean_median_mode_bathrooms()
# sold_date()
# table_bedrooms_buildyear()
# disp_price_landsize()
# frequency_table_bedrooms()
# frequency_table_yearbuilt()
# number_suburbs()
# price_garages()
# mean_median_mode_garages()
# price_location()
# price_yearbuilt()
