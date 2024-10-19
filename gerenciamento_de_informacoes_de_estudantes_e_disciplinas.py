# Título da Prática: Gerenciamento de Informações de Estudantes e Disciplinas
# Objetivos: Compreender a finalidade do uso de lista, dicionários e tuplas

# Desenvolver um programa em Python que permita o gerenciamento de informações de estudantes e disciplinas de uma instituição de ensino.
# O objetivo é criar um sistema que utilize dicionários, tuplas e listas para armazenar e manipular essas informações.
# O programa deve iniciar com um dicionário chamado “estudantes” que irá armazenar as informações dos estudantes.
# Cada estudante será representado como uma chave no dicionário, e as informações pertinentes a esse estudante serão armazenadas em uma tupla.
# Essas informações incluem o nome, a idade e o curso do estudante.
# Além disso, o programa deve ter uma lista chamada “disciplinas”, na qual serão armazenadas as diferentes disciplinas oferecidas pela instituição.
# A lista deve ser inicializada com algumas disciplinas existentes e permitir a adição de novas disciplinas.
# A partir do dicionário “estudantes”, o programa deve ser capaz de percorrer as informações de cada estudante e exibir seu nome, idade e curso.
# Utilize um loop para percorrer o dicionário e acessar as informações da tupla.
# Da mesma forma, o programa deve percorrer a lista de disciplinas e exibi-las na tela.
# Dessa forma, o sistema proporcionará uma maneira eficiente de gerenciar e visualizar informações importantes sobre os estudantes e as disciplinas oferecidas pela instituição.
# A combinação de dicionários, tuplas e listas permitirá uma estrutura de dados organizada e flexível para atender às necessidades de gerenciamento do programa.

# Criando um dicionário com informações de estudantes
estudantes = {
    "João": (20, "Engenharia"),  # Tupla com idade e curso
    "Maria": (19, "Medicina"),
    "Carlos": (22, "Direito")
}
# Criando uma lista de disciplinas
disciplinas = ["Matemática", "Física", "Química"]

# Adicionando uma nova disciplina à lista
disciplinas.append("Biologia")

# Acessando informações dos estudantes usando o dicionário
print("Informações dos estudantes")
for estudante, info in estudantes.items():
    nome, curso = estudante, info
    idade, curso = info
    print(f"Nome: {nome}, Idade: {idade}, Curso: {curso}")

# Imprimindo as disciplinas da lista
print("\nDisciplinas:")
for disciplina in disciplinas:
    print(disciplina)
