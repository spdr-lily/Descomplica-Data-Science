# Título da Prática: Aplicar os conceitos de estrutura de decisão
# Objetivos: Compreender a finalidade do uso If, else, for e while

# Desenvolver um programa que verifique se uma lista de números é composta por números pares ou ímpares.
# O programa deve utilizar as estruturas condicionais “if” e “for” da linguagem de programação Python.
# O programa receberá uma lista de números como entrada. Essa lista pode conter qualquer quantidade de números inteiros.

# Seu objetivo é percorrer cada número da lista e determinar se ele é par ou ímpar.
# Para realizar essa tarefa, você deve implementar um laço “for” que iterará sobre cada elemento da lista.
# Dentro do laço, você deve utilizar uma estrutura condicional “if” para verificar se o número atual é divisível por 2.

# Caso o número seja divisível por 2, ele será considerado par. Caso contrário, será considerado ímpar.
# A cada iteração do laço, o programa deverá exibir uma mensagem indicando se o número é par ou ímpar.
# Por exemplo, para o número 4, o programa deve exibir a mensagem “4 é um número par”, enquanto para o número 7, a mensagem será “7 é um número ímpar”.
# Após percorrer toda a lista, o programa deverá exibir a quantidade total de números pares e ímpares encontrados.
# Para testar o seu programa, você pode criar diferentes listas de números com quantidades variadas de elementos.
# Certifique-se de que o programa está exibindo corretamente a classificação dos números como pares ou ímpares.
# Implemente o programa em Python e teste-o com diferentes entradas.
# Certifique-se de que ele está funcionando corretamente e fornecendo os resultados esperados.

# RESPOSTA:
# Exemplo de código utilizando if e for
# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Iteração sobre os números
for numero in numeros:
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print(f"{numero} é um número par.")
    else:
        print(f"{numero} é um número ímpar.")
