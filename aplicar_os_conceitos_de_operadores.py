# Objetivos: Calcular o custo final de um carro ao consumidor

# Desenvolver um programa que contemple o seguinte contexto:
# O custo de um carro novo para o consumidor é a soma do custo de fábrica com a porcentagem
# do distribuidor e os impostos (aplicados ao custo de fábrica).
# Supondo que o percentual do distribuidor seja de 28% e os impostos sejam de 45%,
# escreva um código no qual o usuário deve informar o custo de fábrica de um carro e,
# em seguida, calcular e apresentar no console o custo final para o consumidor.
# Onde:
# Custo de fábrica é o valor base do carro.
# Percentual do distribuidor é a porcentagem do custo de fábrica que o
# distribuidor adiciona ao valor do carro.
# Impostos é a porcentagem do custo de fábrica que é aplicada como
# impostos sobre o valor do carro.
# Utilizando os valores fornecidos (percentual do distribuidor de 28% e impostos de 45%),
# a fórmula fica assim:
# Custo final = Custo de fábrica + (Custo de fábrica * 0.28) + (Custo de fábrica * 0.45)

# RESOLUÇÃO:

# Solicitar ao usuário o custo de fábrica do carro
custo_fabrica = float(input("Informe o custo de fábrica do carro: "))
# Definir as porcentagens do distribuidor e dos impostos
percentual_distribuidor = 0.28
impostos = 0.45
# Calcular o custo final
custo_final = custo_fabrica + (custo_fabrica * percentual_distribuidor) + (custo_fabrica * impostos)
# Apresenta o custo final para o consumidor
print("O custo final do carro para o consumidor é: ", custo_final)