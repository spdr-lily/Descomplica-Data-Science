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
import utils
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
if __name__ == "__main__":
    main()
