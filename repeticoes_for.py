# FOR: loop que percorre sequências, repetindo ações para cada elemento
notas = []
# valor alterado para cada repetição, pode ser usada apenas dentro do bloco de repetição
for x in range(5): # range(5)=[0,1,2,3,4], nesse caso possui 5 itens
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print("quantidade de notas", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM", codigo_aluno, "tirou a nota:", nota)
    
# WHILE: loop que executa ações enquanto a condição for verdadeira.
