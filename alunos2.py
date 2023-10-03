alunos = []

def cadastrar_notas():
    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar o cadastro): ")
        if nome.lower() == 'sair':
            break
        notas = []
        for i in range(4):
            nota = float(input("Digite a nota", i+1,"do aluno", nome, ":"))
            notas.append(nota)
        aluno = {'nome': nome, 'notas': notas}
        alunos.append(aluno)

def editar_notas():
    nome = input("Digite o nome do aluno que deseja editar as notas: ")
    for aluno in alunos:
        if aluno['nome'] == nome:
            for i in range(4):
                nota = float(input(f"Digite a nova nota {i+1} do aluno {nome}: "))
                aluno['notas'][i] = nota
            print("Notas atualizadas com sucesso.")
            return
    print("Aluno não encontrado.")

def deletar_notas():
    nome = input("Digite o nome do aluno que deseja deletar as notas: ")
    for aluno in alunos:
        if aluno['nome'] == nome:
            alunos.remove(aluno)
            print("Notas deletadas com sucesso.")
            return
    print("Aluno não encontrado.")

def imprimir_notas():
    for aluno in alunos:
        print(f"Notas do aluno {aluno['nome']}: {aluno['notas']}")

def calcular_media():
    total = 0
    for aluno in alunos:
        total += sum(aluno['notas'])
    media = total / (len(alunos) * 4)
    return media

def alunos_aprovados():
    media = calcular_media()
    print("Alunos aprovados:")
    for aluno in alunos:
        if sum(aluno['notas']) / 4 >= 7:
            print(aluno['nome'])

def alunos_reprovados():
    media = calcular_media()
    print("Alunos reprovados:")
    for aluno in alunos:
        if sum(aluno['notas']) / 4 < 7:
            print(aluno['nome'])

while True:
    print("\n1 - Cadastrar notas")
    print("2 - Editar notas")
    print("3 - Deletar notas")
    print("4 - Imprimir notas")
    print("5 - Calcular média")
    print("6 - Alunos aprovados")
    print("7 - Alunos reprovados")
    print("8 - Encerrar o cadastro")
    
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        cadastrar_notas()
    elif opcao == 2:
        editar_notas()
    elif opcao == 3:
        deletar_notas()
    elif opcao == 4:
        imprimir_notas()
    elif opcao == 5:
        media = calcular_media()
        print(f"Média das notas: {media}")
    elif opcao == 6:
        alunos_aprovados()
    elif opcao == 7:
        alunos_reprovados()
    elif opcao == 8:
        break
    else:
        print("Opção inválida.")