def cadastrar_cliente(clientes,nome,email,telefone):
    cliente={
    'Nome':nome,
    'Email':email,
    'Telefone':telefone
    }
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def imprimir_cliente(clientes):
    for indice,cliente in enumerate(clientes):
        print(f"cliente {indice+1}")
        print(f"Nome: {cliente['Nome']}")
        print(f"Email:{cliente['Email']}")
        print(f"telefone:{cliente['Telefone']}")
        print("************************************")

clientes = []
while True:
    print("n\MENU")
    print("1. cadastrar cliente")
    print("2. imprimr cliente")
    print("3.sair")
    opcao=int(input("escolha uma opção: "))
    if opcao == 1:
        nome = input("nome do cliente: ")
        email = input("Email do cliente: ")
        telefone = input("telefone do cliente: ")
        cadastrar_cliente(clientes,nome,email,telefone)
        imprimir_cliente(clientes)
    elif opcao == 2:
        imprimir_cliente(clientes)
    elif opcao == 3:
        print("caindo fora...")
        break
    else:
        print("opção inválida")

