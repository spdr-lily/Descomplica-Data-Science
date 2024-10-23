# exemplos de tipos lista
lista_numeros = [1, 2, 3]
lista_strings = ["Joao", "Maria", "Bruxa"]
lista_decimais = [10.8, 15.2, 33.3]

# manipulando os dados da lista
lista_numeros[0] = 5

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

# exemplo de lista vazia usando append
lista_vazia = []

lista_vazia.append("Olá")
lista_vazia.append("Mundo")

print(lista_vazia)

# exemplo onde se extrai o total de itens na lista, o menos valor e o maior valor:
numeros = [10, 9, 8, 7, 6]

print("total:", len(numeros))
print("menor valor:", min(numeros))
print("maior valor:", max(numeros))
