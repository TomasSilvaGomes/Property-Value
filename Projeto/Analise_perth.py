import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from collections import Counter

perth = pd.read_csv('Ficheiros/perth_file.csv')

#fuction of the hist of the price showing the price on Y axis:
def hist_price():
    plt.hist(perth['price'], bins=50, color='blue', orientation='horizontal')
    plt.title('Histogram of the price')
    plt.xlabel('Frequency')
    plt.ylabel('Price')
    plt.show()

#função que mostra a média, mediana e moda do preço:
def mean_median_mode():
    mean = perth['price'].mean()
    median = perth['price'].median()
    mode = perth['price'].mode()
    print('Média do preço:', mean)
    print('Mediana do preço:', median)
    print('Moda do preço:', mode)

#função para mostrar grafico de dispersao entre o preço e a quantidade de quartos:
def scatter_price_bedrooms():
    plt.scatter(perth['bedrooms'], perth['price'], color='blue')
    plt.title('Scatter plot of price and bedrooms')
    plt.xlabel('bedrooms')
    plt.ylabel('price')
    plt.show()

def heatmap_price_bedrooms():
    relevant_cols = ['price', 'bedrooms']
    df_heatmap = perth[relevant_cols]
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_heatmap.corr(), annot=True, cmap='YlOrRd')
    plt.title('Heatmap of Price and Bedrooms')
    plt.show()


#funcao que mostre a media , mediana e moda dos quartos:
def mean_median_mode_bedrooms():
    mean = perth['bedrooms'].mean()
    median = perth['bedrooms'].median()
    mode = perth['bedrooms'].mode()
    print('Média dos quartos:', mean)
    print('Mediana dos quartos:', median)
    print('Moda dos quartos:', mode)

#funcao que mostre a media , mediana e moda dos banheiros:
def mean_median_mode_bathrooms():
    mean = perth['bathrooms'].mean()
    median = perth['bathrooms'].median()
    mode = perth['bathrooms'].mode()
    print('Média dos banheiros:', mean)
    print('Mediana dos banheiros:', median)
    print('Moda dos banheiros:', mode)

def house_sold_date():
    perth['date_sold'] = pd.to_datetime(perth['date_sold'], format='%m-%Y')

    date_counts = dict(Counter(perth['date_sold']))

    freq_table = pd.DataFrame(list(date_counts.items()), columns=['Date', 'Number of Houses Sold'])
    freq_table = freq_table.sort_values('Date').reset_index(drop=True)

#funcao que mostre uma tabela bedrooms x buildyear:
def table_bedrooms_buildyear():
    table = pd.crosstab(perth['bedrooms'], perth['yearbuilt'])
    print(table)

#funcao que mostre um grafico de dispersao price Vs land_size:
def scatter_price_landsize():
    plt.scatter(perth['price'], perth['land_size'], color='blue')
    plt.title('Scatter plot of price and land size')
    plt.xlabel('Price')
    plt.ylabel('Land size')
    plt.show()
#funcao que mostre tabela de frequencia bedrooms:
def frequency_table_bedrooms():
    table = perth['bedrooms'].value_counts()
    print(table)

#funcao que mostre tabela de frequencia yearbuilt:
def frequency_table_yearbuilt():
    table = perth['build_year'].value_counts()
    print(table)

#funcao que mostre um grafico circular sobre o suburbio:
def piechart_suburb():
    perth['suburb'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Pie chart of the suburb')
    plt.show()

#funcao que mostre grafico de dispersao entre o preço e a quantidade de garagens:
def scatter_price_garages():
    plt.scatter(perth['price'], perth['garage'], color='blue')
    plt.title('Scatter plot of price and garages')
    plt.xlabel('Price')
    plt.ylabel('Garagens')
    plt.show()

#funcao que mostre a media , mediana e moda dos garages:
def mean_median_mode_garages():
    mean = perth['garage'].mean()
    median = perth['garage'].median()
    mode = perth['garage'].mode()
    print('Média das garagens:', mean)
    print('Mediana das garagens:', median)
    print('Moda das garagens:', mode)

 hist_price()
# mean_median_mode()
#scatter_price_bedrooms()
heatmap_price_bedrooms()
# mean_median_mode_bedrooms()
# mean_median_mode_bathrooms()

#table_bedrooms_buildyear()
#
# scatter_price_landsize()
# frequency_table_bedrooms()
# frequency_table_yearbuilt()
# piechart_suburb()
# scatter_price_garages()
# mean_median_mode_garages()
