alunos=[]
def cadastrar_aluno(alunos,nome, nota1,nota2,nota3,nota4,media):
    aluno={ 
        'Nome':nome,
        'Nota1':nota1,
        'Nota2':nota2,
        'Nota3':nota3,
        'Nota4':nota4,
        'Media':media
        }
    alunos.append(aluno)
    print("aluno cadastrado com sucesso!" )
    print("*********************************************")
def cadastrar_notas():
    for indice,aluno in enumerate(alunos):
        print(f"Cliente {indice +1}")
        print(f"Nome: {aluno['Nome']} ")
        print(f"Nota1: {aluno['Nota1']} ")
        print(f"Nota2: {aluno['Nota2']} ")
        print(f"Nota3: {aluno['Nota3']}")
        print(f"Nota4: {aluno['Nota4']}")
        print(f"Media: {aluno['Media']}")
        print("*********************************************")

def editar_nota(alunos,indice,nome, nota1,nota2,nota3,nota4,media):
    if indice >= 0 and indice < len(alunos):
        alunos[indice]['Nome'] = nome
        alunos[indice]['Nota1'] = nota1
        alunos[indice]['Nota2'] = nota2
        alunos[indice]['Nota3'] = nota3
        alunos[indice]['Nota4'] = nota4
        print("Informações do cliente atualizadas com sucesso!")
        return
    else:("inválido")
alunos = []

def deletar_nota(alunos,indice):
    if indice>=0 and indice <= len(alunos):
        del alunos[indice]
        print("aluno foi de arrasta pra cima")
    else:
        return
        print("inválido")

def imprimir_nota(aluno):
    for indice, aluno in enumerate (alunos):
        print(f"Alunos {indice +1}")
        print(f"Nome {aluno['Nome']}")
        print(f"Nota1 {aluno['Nota1']}")
        print(f"Nota2 {aluno['Nota2']}")
        print(f"Nota3 {aluno['Nota3']}")
        print(f"Nota4 {aluno['Nota4']}")
        print("dados do aluno atualizados com sucesso!")
    else:
        print("indice do aluno é invalido!")

def media_nota(alunos):
    for indice, aluno in enumerate (alunos):
        print(f"Alunos {indice +1}")
        print(f"Nome: {aluno['Nome']}")
        print(f"Media: {aluno['Media']}")

def aprovado_nota(alunos):
    for indice, aluno in enumerate (alunos):
        if aluno['Media'] >= 7:
            print(f"Nome: {aluno['Nome']}")
            print(f"Media: {aluno['Media']}")
            print("aluno aprovado:")

def reprovado_nota(alunos):
    for indice, aluno in enumerate (alunos):
        if aluno['edia'] < 7:
            print(f"Nome: {aluno['Nome']}")
            print(f"Media: {aluno['Media']}")
            print("aluno reprovado:")

while True:
    print("MENU\n"
        "1. cadastrar notas\n"
        "2. editar notas\n"
        "3. deletar notas\n"
        "4. imprimir notas\n"
        "5. aprovavos\n "
        "6. reprovados\n")
    opcao=int(input("escolha uma opção"))
    if opcao==1:
        nome=input("nome")
        nota1=float(input("nota1"))
        nota2=float(input("nota1"))
        nota3=float(input("nota1"))
        nota4=float(input("nota1"))
        media=float(nota1+nota2+nota3+nota4)/4
        cadastrar_aluno(alunos,nome, nota1,nota2,nota3,nota4,media)
    if opcao == 2:
        indice=int(input("numero"))
        nota1=float(input("nota1"))
        nota2=float(input("nota1"))
        nota3=float(input("nota1"))
        nota4=float(input("nota1"))
        editar_nota(alunos,indice,nome, nota1,nota2,nota3,nota4,media)
    if opcao == 3:
        indice=int(input("numero"))
        deletar_nota(alunos,indice)
    if opcao == 4:
        imprimir_nota(alunos)
    if opcao == 5:
        aprovado_nota(alunos)
    if opcao == 6:
        reprovado_nota(alunos)
    