# exemplo de idade para entrar em uma festa
idade = int( input("Informe a sua idade: ") )

if idade >= 18:
    print("PERMITIDO!")
else:
    print("BLOQUEADO!")

# exemplo de salario fictício
salario = float(input("Informe o salário"))

if salario <= 3000:
    print("programador junior")
elif salario > 3000 and salario <= 6000:
    print("programador senior")
elif salario > 6000 and salario <=15000:
    print("programador senior")
else:
    print("gerente de projetos")