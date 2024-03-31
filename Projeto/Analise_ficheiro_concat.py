import matplotlib.pyplot as plt
from folium.plugins import MarkerCluster
import folium
import seaborn as sns
from Projeto import *


'''
ficheiro_concat = pd.read_csv('Ficheiros/ficheiro_concat.csv')
mapa = folium.Map(location=[-31.9, 115.9], zoom_start=10)
marker_cluster = MarkerCluster().add_to(mapa)

for index, row in ficheiro_concat.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=f"Price: ${row['price']}").add_to(marker_cluster)

mapa.save('mapa.html')

'''
def mapa_mundi():
    ficheiro_concat = pd.read_csv('Ficheiros/ficheiro_concat.csv')
    mapa = folium.Map(location=[-31.9, 115.9], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(mapa)

    for index, row in ficheiro_concat.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=f"Price: ${row['price']}").add_to(marker_cluster)

    mapa.save('mapa.html')


def preco_casas():
    labels = 'Perth', 'Melbourne', 'Delhi'
    sizes = [perth['price'].max(), melbourne['price'].max(), delhi['price'].max()]
    plt.bar(labels, sizes)
    plt.title('Preço máximo das casas por cidade')
    plt.xlabel('Cidade')
    plt.ylabel('Preço(A$)')
    plt.show()

def preco_quartos():
    plt.scatter(ficheiro_concat['bedrooms'], ficheiro_concat['price'])
    plt.title('Preço por quantidade de quartos')
    plt.xlabel('Quartos')
    plt.ylabel('Preço(A$)')
    plt.show()

def percentagem_casas():
    labels = 'Perth', 'Melbourne', 'Delhi'
    sizes = [len(perth), len(melbourne), len(delhi)]
    colors = ['gold', 'yellowgreen', 'lightcoral']
    explode = (0.1, 0, 0)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title('Percentagem de casas vendidas no conjunto de dados total')
    plt.axis('equal')
    plt.show()



def tamanho_casas_cidades():
    labels = 'Perth', 'Melbourne', 'Delhi'
    sizes = [perth['landsize'].mean(), melbourne['landsize'].mean(), delhi['landsize'].mean()]
    plt.bar(labels, sizes)
    plt.title('Tamanho do terreno')
    plt.xlabel('Cidade')
    plt.ylabel('Tamanho do terreno')
    plt.show()
def compar_bedrooms_bathrooms():
    plt.figure(figsize=(10,6))
    sns.countplot(x='bedrooms', hue='bathrooms', data=ficheiro_concat)
    plt.title('Comparação de quartos e casas de banho')
    plt.show()

def tabela_datavenda():
    freq_table = ficheiro_concat.groupby('date_sold').size()
    print(freq_table)


def quartos_bathrooms_preco():
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='bedrooms', y= 'bathrooms', hue= 'price' , data=ficheiro_concat, palette='coolwarm')
    plt.title('Preço dos quartos e casas de banho')
    plt.xlabel('Quartos')
    plt.ylabel('Casas de Banho')
    plt.show()

def preco_anodeconstrucao():
    #so contar yearbuilt a partir de 1830:
    data = ficheiro_concat[ficheiro_concat['yearbuilt'] > 1830]
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='yearbuilt', y='price', data=data)
    plt.title('Preço por Ano de Construção')
    plt.xlabel('Ano de Construção')
    plt.ylabel('Preço(A$)')
    plt.show()



# preco_casas()
# preco_quartos()
# percentagem_casas()
# tamanho_casas_cidades()
# tabela_datavenda()
# quartos_bathrooms_preco()
# preco_anodeconstrucao()