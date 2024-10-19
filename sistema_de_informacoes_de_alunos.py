# Título da Prática: Sistema de Informações de Alunos
# Objetivos: Compreender a finalidade do uso de funções e módulos

# O objetivo deste projeto é desenvolver um sistema de informações de alunos utilizando dicionários, funções e módulos em Python.
# O sistema será capaz de armazenar e fornecer informações detalhadas sobre os alunos, como nome, idade e curso.
# O sistema consiste em dois componentes principais: o módulo de utilidades (utils.py) e o módulo principal (main.py).
# O módulo de utilidades contém uma função chamada “saudacao()”, que recebe o nome do usuário como entrada e retorna uma saudação personalizada.

# Já o módulo principal é responsável por obter informações de um aluno específico com base em seu ID, utilizando a função “obter_informacoes_aluno()”.
# As informações dos alunos são armazenadas em um dicionário chamado “alunos”.

# Cada aluno possui um ID único e um conjunto de informações, incluindo nome, idade e curso.
# A função “obter_informacoes_aluno()” verifica se o ID fornecido pelo usuário corresponde a um aluno válido no dicionário.
# Em caso afirmativo, as informações completas do aluno são retornadas, caso contrário, uma mensagem de aluno não encontrado é exibida.
# O programa principal inicia solicitando o nome do usuário e exibindo uma saudação personalizada.
# Em seguida, solicita-se ao usuário que forneça o ID de um aluno.
# Com base nesse ID, o sistema busca as informações do aluno correspondente no dicionário e as exibe na tela.
# Com a implementação deste sistema de informações de alunos, espera-se fornecer uma maneira eficiente e organizada de armazenar e acessar dados relevantes sobre os alunos,
# facilitando o gerenciamento e a recuperação das informações quando necessário.

# Módulo: utils.py
def saudacao(nome):
    return f"Olá, {nome}!"
# Dicionário de informações dos alunos
alunos = {
    1: {
        'nome': 'João',
        'idade': 20,
        'curso': 'Engenharia'
    },
    2: {
        'Nome': 'Maria',
        'idade': 22,
        'curso': 'Ciências da Computação'
    },
    3: {
        'nome': 'Pedro',
        'idade': 21,
        'curso': 'Administração'
    }
}
# Módulo principal: main.py
import python_utils
# Função para obter informações de um aluno pelo ID
def obter_informacoes_aluno(id_aluno):
    if id_aluno in alunos:
        aluno = alunos[id_aluno]
        nome = aluno['nome']
        idade = aluno['idade']
        curso = aluno['curso']
        return f"Nome: {nome}\nIdade: {idade}\nCurso: {curso}"
    else:
        return "Aluno não encontrado."
# Função principal
def main():
    nome = input("Digite seu nome: ")
    saudacao = utils.saudacao(nome)
    print(saudacao)
    id_aluno = int(input("Digite o ID do aluno: "))
    informacoes_aluno = obter_informacoes_aluno(id_aluno)
    print(informacoes_aluno)
# Executar a função principal
if name == 'main':
    main()
