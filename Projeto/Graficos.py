from Projeto import *

#funcao para mostrar grafico de cada variavel:

#funcao para mostrar grafico de dispersao de price em funcao de landsize:
def scatter_landsize_price():
    plt.scatter(ficheiro_analise['landsize'], ficheiro_analise['price'])
    plt.title('Price x Landsize')
    plt.xlabel('Landsize')
    plt.ylabel('Price')
    plt.show()
#scatter_landsize_price()

#funcao para mostrar grafico  sobre o preco mais elevado dos diferentes ficheiros onde no eixo x temos o nome do ficheiro e no eixo y o preco:
def bar_max_price():
    max_price = ficheiro_analise.groupby('source').max()['price']
    max_price.plot(kind='bar')
    plt.title('Max Price')
    plt.xlabel('Source')
    plt.ylabel('Price')
    plt.show()
bar_max_price()