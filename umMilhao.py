print()
print('PODER DO PYTHON!')
print()
print('O Python irá exibir agora a sua capacidade de processamento de números.')
print('Criando uma lista que vai de 1 até 100 milhões e ainda exibir a soma de todos esses números em poucos segundos.')
lista = []
for numbers in range(1, 100000001):
    lista.append(numbers)
print(lista)
print(f'O menor número da lista: {min(lista)}')
print(f'O maior número da lista: {max(lista)}')
print(f'A soma de todos eles: {sum(lista)}')