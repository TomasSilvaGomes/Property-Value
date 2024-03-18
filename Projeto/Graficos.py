import matplotlib.pyplot as plt

from Projeto import *

#funcao para mostrar grafico de cada variavel:

#funcao para motrar um grafico de dispersao do price e o landsize:
def scatter_price_landsize():
    plt.scatter(ficheiro_analise['landsize'], ficheiro_analise['price'])
    plt.title('Price x Landsize')
    plt.xlabel('Landsize')
    plt.ylabel('Price')
    plt.show()
scatter_price_landsize()

#funcao para mostrar grafico de dispersao de price em funcao de rooms:
def scatter_rooms_price():
    plt.scatter(ficheiro_analise['bedrooms'], ficheiro_analise['price'])
    plt.title('Price x Rooms')
    plt.xlabel('Rooms')
    plt.ylabel('Price')
    plt.show()
scatter_rooms_price()

#funcao para mostrar garfico ciruclar de price dos diferentes tipos de ficheiros:
def pie_price():
    labels = 'Perth', 'Melbourne', 'Delhi'
    sizes = [len(perth), len(melbourne), len(delhi)]
    colors = ['gold', 'yellowgreen', 'lightcoral']
    explode = (0.1, 0, 0)  # explode 1st slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()
pie_price()

#funcao para mostrar num grafico de barras o tamanho os landsize dos diferentes tipos de ficheiros:
def bar_landsize():
    labels = 'Perth', 'Melbourne', 'Delhi'
    sizes = [perth['landsize'].mean(), melbourne['landsize'].mean(), delhi['landsize'].mean()]
    plt.bar(labels, sizes)
    plt.title('Landsize')
    plt.xlabel('City')
    plt.ylabel('Landsize')
    plt.show()
bar_landsize()

#funcao que mostre a quantidade de address em cada ficheiro num grafico de barras:
def bar_address():
    labels = 'Perth', 'Melbourne', 'Delhi'
    sizes = [len(perth['address']), len(melbourne['address']), len(delhi['address'])]
    plt.bar(labels, sizes)
    plt.title('Address')
    plt.xlabel('City')
    plt.ylabel('Address')
    plt.show()
bar_address()

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('ficheiro_analise.csv')

# Create a bar graph to compare the number of bathrooms and bedrooms
bathroom_bedroom_count = data.groupby(['bedrooms', 'bathrooms']).size().unstack()
bathroom_bedroom_count.plot(kind='bar', stacked=False, figsize=(12, 6))
plt.title('Comparison of Bedrooms and Bathrooms')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Count')
plt.show()







