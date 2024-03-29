from Projeto import *
import matplotlib.pyplot as plt
from folium.plugins import MarkerCluster
import folium


ficheiro_concat = pd.read_csv('Ficheiros/ficheiro_concat.csv')
mapa = folium.Map(location=[-31.9, 115.9], zoom_start=10)
marker_cluster = MarkerCluster().add_to(mapa)

for index, row in ficheiro_concat.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=f"Price: ${row['price']}").add_to(marker_cluster)

mapa.save('mapa.html')

'''
def mapa_mundi():
    data = pd.read_csv('Ficheiros/ficheiro_concat.csv')
    mapa = folium.Map(location=[-31.9, 115.9], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(mapa)
    for index, row in data.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=f"Price: ${row['price']}").add_to(marker_cluster)
        mapa.save('mapa.html')


def scatter_price_landsize():
    plt.scatter(ficheiro_concat['landsize'], ficheiro_concat['price'])
    plt.title('Price x Landsize')
    plt.xlabel('Landsize')
    plt.ylabel('Price')
    plt.show()

#scatter_landsize_price()

def bar_price():
    labels = 'Perth', 'Melbourne', 'Delhi'
    sizes = [perth['price'].max(), melbourne['price'].max(), delhi['price'].max()]
    plt.bar(labels, sizes)
    plt.title('Price')
    plt.xlabel('City')
    plt.ylabel('Price')
    plt.show()

def scatter_rooms_price():
    plt.scatter(ficheiro_concat['bedrooms'], ficheiro_concat['price'])
    plt.title('Price x Rooms')
    plt.xlabel('Rooms')
    plt.ylabel('Price')
    plt.show()

def pie_casas():
    labels = 'Perth', 'Melbourne', 'Delhi'
    sizes = [len(perth), len(melbourne), len(delhi)]
    colors = ['gold', 'yellowgreen', 'lightcoral']
    explode = (0.1, 0, 0)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()
    plt.title('Quantidade de casas há venda')


def bar_landsize():
    labels = 'Perth', 'Melbourne', 'Delhi'
    sizes = [perth['landsize'].mean(), melbourne['landsize'].mean(), delhi['landsize'].mean()]
    plt.bar(labels, sizes)
    plt.title('Landsize')
    plt.xlabel('City')
    plt.ylabel('Landsize')
    plt.show()
def comparacao_quartos_bathrooms():
    data= pd.read_csv('Ficheiros/ficheiro_concat.csv')
    bathroom_bedroom_count = data.groupby(['bedrooms', 'bathrooms']).size().unstack()
    bathroom_bedroom_count.plot(kind='bar', stacked=False, figsize=(12, 6))
    plt.title('Comparação de Quartos e Casas de Banho')
    plt.xlabel('Numero de Quartos')
    plt.ylabel('Numero de Casas de Banho')
    plt.show()

def freq_table():
    freq_table = ficheiro_concat.groupby('date_sold').size()
    print(freq_table)

def scatter_3D():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(ficheiro_concat['longitude'], ficheiro_concat['latitude'], ficheiro_concat['price'])
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Price')
    plt.show()

def scatter_3D_bedrooms_bathrooms_price():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(ficheiro_concat['bedrooms'], ficheiro_concat['bathrooms'], ficheiro_concat['price'])
    ax.set_xlabel('Bedrooms')
    ax.set_ylabel('Bathrooms')
    ax.set_zlabel('Price')
    plt.show()

def bar_yearbuilt_price():
    labels = ficheiro_concat['yearbuilt']
    sizes = ficheiro_concat['price']
    plt.bar(labels, sizes)
    plt.title('Yearbuilt x Price')
    plt.xlabel('Yearbuilt')
    plt.ylabel('Price')
    plt.show()



def heat_map():
    plt.matshow(ficheiro_concat.corr())
    plt.show()


def create_subplots():
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
    for i, column in enumerate(ficheiro_concat.columns):
        ficheiro_concat[column].plot(ax=axes[i], title=column)
        plt.show()
'''