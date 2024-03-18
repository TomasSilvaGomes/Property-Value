from Projeto import *

#funcao para mostrar grafico de cada variavel:

#funcao para mostrar grafico de dispersao de price em funcao de landsize:
def scatter_landsize_price():
    plt.scatter(ficheiro_analise['landsize'], ficheiro_analise['price'])
    plt.title('Price x Landsize')
    plt.xlabel('Landsize')
    plt.ylabel('Price')
    plt.show()
scatter_landsize_price()

#funcao para mostrar grafico