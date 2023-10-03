alunos[] #armaenar a função alunos
notas[]
def cadastrar_notas(): # cadastrar as notas. def serve para definir a fenção e evitar repetições.
    while True: #criar um loop para que sempre aparea as opções ---- break
        nome= input("Digite o nome do aluno ou se desejar sair, o numero 5")
        if nome == 5:
           break
        for b in range:
            nota= float(input("digite a nota do aluno:", nome , "nota:  "))
            notas.append(nota)
        aluno={'nome': nome, 'notas': notas}
        aluno.append(aluno)#armaena no final da fila
def editar_notas():
    nome= input("digite o nome do aluno que deja editar: ")
    for aluno in alunos 