import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

delhi = pd.read_csv('Ficheiros/Delhi_v2.csv')
delhi['price']= delhi['price'] / 83


def heatmap():
    delhi = pd.read_csv('Ficheiros/Delhi_v2.csv')
    delhi = delhi.drop(columns = ['address','status','neworold','furnished_status','landmarks','type_of_building','desc'])
    corr_matrix = delhi.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='YlOrRd')
    plt.title('Correlação de variáveis')
    plt.show()

def media_mediana_preco():
    mean = delhi['price'].mean()
    median = delhi['price'].median()
    print('Média do preço:', mean)
    print('Mediana do preço:', median)

def media_mediana_rooms():
    media = delhi['bedrooms'].mean()
    mediana = delhi['bedrooms'].median()
    print('\nMédia dos quartos:', media)
    print('Mediana dos quartos:', mediana)

def media_mediana_bathrooms():
    media = delhi['bathrooms'].mean()
    mediana = delhi['bathrooms'].median()
    print('\nMédia das casas de banho:', media)
    print('Mediana das casas de banho:', mediana)

def media_mediana_sqft():
    media = delhi['price_sqft'].mean()
    mediana = delhi['price_sqft'].median()
    print('\nMédia do preço por metro quadrado:', media)
    print('Mediana do preço por metro quadrado:', mediana)
def tabela_tipo_de_construcao():
    tabela = delhi['type_of_building'].value_counts()
    print(tabela)
def tabela_novo_ou_velho():
    tabela = delhi['neworold'].value_counts()
    print(tabela)


def dispersao_preco_rooms():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='bedrooms', y='price', data=delhi, color='skyblue')
    plt.title('Preço em relação ao número de Quartos')
    plt.xlabel('Número de Quartos')
    plt.ylabel('Preço(A$)')
    plt.show()

def dispersao_preco_bathrooms():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='bathrooms', y='price', data=delhi, color='skyblue')
    plt.title('Preço em relação ao número de Casas de Banho')
    plt.xlabel('Número de Casas de Banho')
    plt.ylabel('Preço(A$)')
    plt.show()

def dispersao_preco_landsize():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='landsize', y='price', data=delhi, color='skyblue')
    plt.title('Preço em relação ao tamanho do terreno')
    plt.xlabel('Tamanho do terreno')
    plt.ylabel('Preço(A$)')
    plt.show()

def preco_localizacao():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='longitude', y='latitude', data=delhi,hue='price', palette='coolwarm')
    plt.title('Preço em relação à localização')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.show()


def circular_novo_ou_velho():
    plt.figure(figsize=(10, 6))
    delhi['neworold'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Novo ou Revenda')
    plt.show()


def circular_tipo_de_construcao():
    plt.figure(figsize=(10, 6))
    delhi['type_of_building'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Tipo de Construção')
    plt.show()

def histograma_novo_ou_velho():
    plt.figure(figsize=(10, 6))
    sns.histplot(data=delhi, x='neworold', kde=True, color='skyblue')
    plt.title('Histograma de Novo ou Revenda')
    plt.show()

def histograma_tipo_de_construcao():
    plt.figure(figsize=(10, 6))
    sns.histplot(data=delhi, x='type_of_building', kde=True, color='skyblue')
    plt.title('Histograma de Tipo de Construção')
    plt.show()

def landsize_pricesqft():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='landsize', y='price_sqft', data=delhi, color='skyblue')
    plt.title('Preço por metro quadrado em relação ao tamanho do terreno')
    plt.xlabel('Tamanho do terreno')
    plt.ylabel('Preço por metro quadrado')
    plt.show()

''' Se necessário visualizar algum gráfico, basta descomentar a função correspondente. '''

# print(delhi.isnull().sum())
# heatmap()
# media_mediana_preco()
# media_mediana_rooms()
# media_mediana_bathrooms()
# media_mediana_sqft()
# tabela_tipo_de_construcao()
# tabela_novo_ou_velho()
# dispersao_preco_rooms()
# dispersao_preco_bathrooms()
# dispersao_preco_landsize()
# preco_localizacao()
# circular_novo_ou_velho()
# circular_tipo_de_construcao()
# histograma_novo_ou_velho()
# histograma_tipo_de_construcao()
# landsize_pricesqft()