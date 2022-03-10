print("ITMK - Instituto de Tecnologia Melchiades Klai")

# ----- Dados ----- #

nomes = ["Carlos", "Marlon", "Ana"]
idades = ["21", "22", "19"]
cursos = ["Biologia", "Matemática", "História"]

# ----- funções ----- #

def cadatro_aluno():
    print("")
    nome_aluno = input("Digite o nome do aluno:")
    idade_aluno = input("Digite a idade do aluno:")
    curso_aluno = input("Digite o curso o qual o aluno irá frequentar:")
    nomes.append(nome_aluno)
    idades.append(idade_aluno)
    cursos.append(curso_aluno)
    print("\nCadastro realizado com sucesso!\n")
    print("Cadastrar novo aluno?\n")
    print("1.Sim")
    print("2.Não\n")
    novo_aluno = input("Selecione uma das opções:")
    if novo_aluno == "1":
        cadatro_aluno()
    if novo_aluno == "2":
        principal()

def lista():
    if nomes == []:
        print("\nLista vazia")
        principal()
    else:
        contador = 0
        print("\nLISTA DE ALUNOS\n")
        for e1 in nomes:
            idade_X = idades[contador]
            curso_X = cursos[contador]
            dados_lista = "NOME: " + str(e1) + "; IDADE: " + str(idade_X) + " anos; CURSO: " + str(curso_X) + ";"
            print(dados_lista)
            contador=contador + 1
    principal()

def principal():
    print("\nBem-vindo ao sistema de cadastramento de alunos da ITMK!")
    print("\n1.Cadastrar aluno")
    print("2.Descadastrar aluno")
    print("3.Ver lista completa")
    print("4.Encerrar atividade\n")
    resposta=input("Selecione uma das opções:")
    condicao(resposta)

def condicao(resposta):
    if resposta == "1":
        cadatro_aluno()
    if resposta == "2":
        print()
    if resposta == "3":
        lista()
    if resposta == "4":
        print("\nAté a próxima! \nEncerrando o Programa...\n")

principal()
