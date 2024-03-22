from Projeto import *
import pandas as pd
import folium

#funcao para mostrar grafico de cada variavel:

#funcao para motrar um grafico de dispersao do price e o landsize:
def scatter_price_landsize():
    plt.scatter(ficheiro_analise['landsize'], ficheiro_analise['price'])
    plt.title('Price x Landsize')
    plt.xlabel('Landsize')
    plt.ylabel('Price')
    plt.show()

#scatter_landsize_price()

#funcao para mostrar grafico  sobre o preco mais elevado dos diferentes ficheiros onde no eixo x temos o nome do ficheiro e no eixo y o preco:
def bar_price():
    labels = 'Perth', 'Melbourne', 'Delhi'
    sizes = [perth['price'].max(), melbourne['price'].max(), delhi['price'].max()]
    plt.bar(labels, sizes)
    plt.title('Price')
    plt.xlabel('City')
    plt.ylabel('Price')
    plt.show()

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

#faz uma tabela de frequencia sobre a data de cada ficheiro em funcao do preço:
def freq_table():
    freq_table = ficheiro_analise.groupby('date_sold').size()
    print(freq_table)
freq_table()

#Faz um grafico 3D com as variaveis longitude, latitude e price do ficheiro_analise:
def scatter_3D():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(ficheiro_analise['longitude'], ficheiro_analise['latitude'], ficheiro_analise['price'])
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Price')
    plt.show()
scatter_3D()
#mostre um grafico 3d com as variaveis bedrooms, bathrooms e price do ficheiro_analise:
def scatter_3D_bedrooms_bathrooms_price():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(ficheiro_analise['bedrooms'], ficheiro_analise['bathrooms'], ficheiro_analise['price'])
    ax.set_xlabel('Bedrooms')
    ax.set_ylabel('Bathrooms')
    ax.set_zlabel('Price')
    plt.show()
scatter_3D_bedrooms_bathrooms_price()
#mostre um grafico de barras com as variaveis yearbuilt e price do ficheiro_analise:
def bar_yearbuilt_price():
    labels = ficheiro_analise['yearbuilt']
    sizes = ficheiro_analise['price']
    plt.bar(labels, sizes)
    plt.title('Yearbuilt x Price')
    plt.xlabel('Yearbuilt')
    plt.ylabel('Price')
    plt.show()
bar_yearbuilt_price()

import pandas as pd
import folium

data = pd.read_csv('ficheiro_analise.csv')

map = folium.Map(location=[-31.9, 115.8], zoom_start=10)

for index, row in data.iterrows():
    price = row['price']
    color = 'green' if price < 500000 else 'orange' if price < 700000 else 'red'
    folium.Marker(location=[row['latitude'], row['longitude']], popup=f'Price: {price}', icon=folium.Icon(color=color)).add_to(map)
map.save('map_with_prices.html')


