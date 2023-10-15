from time import sleep
import math
import matplotlib.pyplot as plt
from time import time


def criar_lista(n):
    """Cria uma lista de números de 1 a n."""
    return list(range(1, n + 1))


def calcular_estatisticas(lista):
    """Calcula a soma, o quadrado da soma, o menor e o maior número da lista."""
    soma = sum(lista)
    quadrado = soma * soma
    menor_numero = min(lista)
    maior_numero = max(lista)
    return soma, quadrado, menor_numero, maior_numero


def criar_histograma(lista):
    """Cria um histograma da lista."""
    plt.figure(num='Histograma')
    plt.hist(lista, bins=50, color='skyblue', edgecolor='gray')
    plt.title('Distribuição dos Números da Lista')
    plt.xlabel('Número')
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.show()


def criar_grafico_3d(lista, soma, raiz_quadrada):
    """Cria um gráfico 3D aprimorado com rótulos, marcadores e cores
    significativas. """
    fig = plt.figure(num='Exemplo de Gráfico 3D onde x = lista | y = soma da '
                         'lista | z = raiz quadrada da lista')
    ax = fig.add_subplot(111, projection='3d')

    x = lista
    y = [soma] * len(lista)
    z = [raiz_quadrada] * len(lista)

    # Use um marcador (por exemplo, 'o' para círculos) e uma cor (por
    # exemplo, vermelho) para os pontos
    ax.scatter(x, y, z, c='r', marker='o', label='Pontos')

    ax.set_xlabel('Números')
    ax.set_ylabel('Soma')
    ax.set_zlabel('Raiz Quadrada')

    # Adicione um título ao gráfico 3D
    plt.title('Gráfico 3D')

    # Adicione uma legenda para os pontos
    plt.legend()

    # Defina uma grade no gráfico
    ax.grid(True)

    # Exiba o gráfico 3D
    plt.show()


def main():
    print()
    print('PODER DO PYTHON!')
    print()
    print(
        'Este programa demonstra a capacidade de processamento de números em '
        'Python.')
    sleep(3)
    print()
    print(
        'Criando uma lista de números, um histograma e um gráfico 3D a partir '
        'dessa lista.')
    sleep(3)
    print()
    print(
        'A lista vai de 1 até o valor escolhido e operações estatísticas serão '
        'realizadas.')
    sleep(3)
    print()
    print('OBSERVAÇÂO: Se executado diretamente em um computador, o python '
          'consegue facilemtente processar mais de 100 milhões de números, '
          'porém se executado no browser, pode ocorrer lentidão, mas note que o'
          ' gargalo está no navegador e não na linguagem.')
    print()
    sleep(3)
    n = None  # Inicializa n como None

    while n is None:
        try:
            n = int(input('Digite um número inteiro para definir o tamanho da '
                          'lista: '))
            if n <= 0:
                print('Digite um valor maior que 0.')
                n = None
        except ValueError:
            print('Digite um número inteiro válido.')

    print('A contagem começa em...')
    print('5...')
    sleep(1)
    print('4...')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)

    tempo_inicial = time()

    lista = criar_lista(n)
    soma, quadrado, menor_numero, maior_numero = calcular_estatisticas(lista)

    print(f'O menor número da lista: {menor_numero}')
    print(f'O maior número da lista: {maior_numero}')
    print(f'A soma de todos eles: {soma}')
    print(f'O quadrado da soma dos números é: {quadrado}')
    raiz_quadrada = math.sqrt(soma)
    print(f'A raiz quadrada da soma dos números é: {raiz_quadrada}')

    tempo_final = time()
    tempo_execucao = tempo_final - tempo_inicial
    print(f'Tempo de execução dos cálculos: {tempo_execucao} segundos')

    criar_histograma(lista)
    criar_grafico_3d(lista, soma, raiz_quadrada)

    print('Fim do programa!')


if __name__ == "__main__":
    main()
