from time import sleep
import math
import matplotlib.pyplot as plt
from time import time

# Introdução ao programa
print()
print('PODER DO PYTHON!')
print()
print(
    'O Python irá exibir agora a sua capacidade de processamento de números.')
print()
# Tempo de espera para leitura
sleep(3)
# Explicação do que o programa fará
print(
    'Criando uma lista, um histograma e um gráfico a respeito da lista, '
    'que vai de 1 até 1 milhão e ainda '
    'exibir algumas operações acerca destes números em poucos segundos. '
)
print()
# Tempo de espera para leitura
sleep(5)
print(
    'O python tem capacidade de processamento muito maior, rodando este'
    ' programa diretamente em um computador ele pode facilmente trabalhar'
    ' com mais de 100 milhões de números. Porém como será executado no browser,'
    ' será trabalhado neste exemplo com apenas 1 milhão de números.'
)
print()
# Tempo de espera para leitura
sleep(12)
# Contagem regressiva de 5 segundos para início dos cálculos
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

# Registra o tempo de início
tempo_inicial = time()

# Cria uma lista que vai de 1 a 1000000
lista = []
for numbers in range(1, 1000000):
    lista.append(numbers)

# Salva em variáveis a soma, menor número, maior número e raiz quadrada dos
# números da lista.
soma = sum(lista)
quadrado = soma * soma
menor_numero = min(lista)
maior_numero = max(lista)
raiz_quadrada = math.sqrt(soma)
print(f'O menor número da lista: {min(lista)}')
print(f'O maior número da lista: {max(lista)}')
print(f'A soma de todos eles: {soma}')
print(f'O quadrado da soma dos números é: {quadrado}')
print(f'A raiz quadrada da soma dos números é: {raiz_quadrada}')
print()

# Registra o tempo de término
tempo_final = time()

# Calcula o tempo de execução
tempo_execucao = tempo_final - tempo_inicial
print(f'Tempo de execução dos cálculos: {tempo_execucao} segundos')

# Cria um histograma da lista
plt.figure(num='Histograma')
plt.hist(lista, bins=50, color='skyblue', edgecolor='gray')
plt.title('Distribuição dos Números da Lista')
plt.xlabel('Número')
plt.ylabel('Frequência')
plt.grid(True)

# Exibe o histograma
plt.show()
print('Fim do programa!')

# Cria uma figura 3D
fig = plt.figure(num='Exemplo de Gráfico 3d onde o eixo x = lista, y = soma '
                     'e z = raiz quadrada da soma')
ax = fig.add_subplot(111, projection='3d')

# Usa a lista de números como os valores do eixo X
x = lista

# Use o resultado da soma como os valores do eixo Y
y = [soma] * len(lista)

# Usa a raiz quadrada da soma como os valores do eixo Z
z = [raiz_quadrada] * len(lista)

# Cria um gráfico de dispersão 3D
ax.scatter(x, y, z, c='r', marker='o')

# Define rótulos para os eixos
ax.set_xlabel('Números')
ax.set_ylabel('Soma')
ax.set_zlabel('Raiz Quadrada')

# Mostra o gráfico 3D
plt.show()
