import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

perth = pd.read_csv('Ficheiros/perth_file.csv')
perth['landsize'] = perth['landsize'] / 10,76

def heatmap_v():
    perth = pd.read_csv('Ficheiros/perth_file.csv')
    perth = perth.drop(['address', 'suburb','nearest_stn','nearest_sch','date_sold'], axis=1)
    corr_matrix = perth.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='YlOrRd')
    plt.title('Correlação de variáves')
    plt.show()



def hist_preco():
    plt.hist(perth['price'], bins=100, color='purple')
    plt.title('Gráfico do preço')
    plt.xlabel('Preço(A$)')
    plt.ylabel('Frequência')
    plt.show()


def media_mediana_moda():
    mean = perth['price'].mean()
    median = perth['price'].median()
    mode = perth['price'].mode()
    print('Média do preço:', mean)
    print('Mediana do preço:', median)
    print('Moda do preço:', mode)



def plt_preco_quartos():
    # Create a bar plot of price (in millions) vs. bedrooms
    plt.figure(figsize=(12, 6))
    perth.groupby('bedrooms')['price'].mean().plot(kind='bar', color='skyblue')
    plt.title('Preço por Numero de quartos')
    plt.xlabel('Numero de Quartos')
    plt.ylabel('Preço(A$)')
    plt.xticks(rotation=0)
    plt.show()


def media_mediana_moda_quartos():
    mean = perth['bedrooms'].mean()
    median = perth['bedrooms'].median()
    mode = perth['bedrooms'].mode()
    print('\nMédia dos quartos:', mean)
    print('Mediana dos quartos:', median)
    print('Moda dos quartos:', mode)

def media_mediana_moda_bathrooms():
    mean = perth['bathrooms'].mean()
    median = perth['bathrooms'].median()
    mode = perth['bathrooms'].mode()
    print('\nMédia das casas de banho:', mean)
    print('Mediana das casas de banho:', median)
    print('Moda das casas de banho:', mode)

def data_venda():
    sold_date = perth['date_sold'].value_counts()
    print(sold_date)

def tabela_quartos_anoconstrucao():
    table = pd.crosstab(perth['bedrooms'], perth['yearbuilt'])
    print(table)

def disp_preco_landsize():
    plt.figure(figsize=(10, 6))
    sns.regplot(x='landsize', y='price', data=perth)
    plt.title('Preço em relação ao Tamanho do Terreno')
    plt.xlabel('Tamanho do terreno (m²)')
    plt.ylabel('Preço(A$)')
    plt.show()


def frequencia_quartos():
    table = perth['bedrooms'].value_counts()
    print(table)

def frequencia_anoconstrucao():
    table = perth['yearbuilt'].value_counts()
    print(table)

def numero_suburbios():
    number = perth['suburb'].value_counts()
    print(number)

def preco_garagens():

    plt.figure(figsize=(10, 6))
    perth.groupby('garage')['price'].mean().plot(kind='bar', color='blue')
    plt.title('Gráfico de Dispersão: Preço vs. Quantidade de Garagens')
    plt.xlabel('Quantidade de Garagens (Máx: 20)')
    plt.ylabel('Preço(A$)')
    plt.xticks(rotation=0)
    plt.show()


def media_mediana_moda_garagens():
    mean = perth['garage'].mean()
    median = perth['garage'].median()
    mode = perth['garage'].mode()
    print('\nMédia das garagens:', mean)
    print('Mediana das garagens:', median)

    print('Moda das garagens:', mode)


def preco_localizacao():

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='longitude', y='latitude', data=perth, hue='price', palette='coolwarm')
    plt.title('Preço em Relação à Localização Geográfica')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()

#Preço em relação ao Ano de Construção:
def preco_anoconstrucao():

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='yearbuilt', y='price', data=perth, hue='price', palette='coolwarm')
    plt.title('Preço em Relação ao Ano de Construção')
    plt.xlabel('Ano de Construção')
    plt.show()

''' Se necessário visualizar algum gráfico, basta descomentar a função correspondente. '''

# heatmap_v()
# hist_preco()
# media_mediana_moda()
# plt_preco_quartos()
# media_mediana_moda_quartos()
# media_mediana_moda_bathrooms()
# data_venda()
# tabela_quartos_anoconstrucao()
# disp_preco_landsize()
# frequencia_quartos()
# frequencia_anoconstrucao()
# numero_suburbios()
# preco_garagens()
# media_mediana_moda_garagens()
# preco_localizacao()
# preco_anoconstrucao()


