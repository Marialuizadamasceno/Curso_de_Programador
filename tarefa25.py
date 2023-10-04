import csv
def cadastrar_cliente(clientes, nome , email, telefone):
    cliente ={
        'Nome': nome,
        'Email':email,
        'Telefone': telefone
    }
    clientes.append(cliente)
    print("suscesso!")
clientes=[] 
nome = input("nome do cliente: ")
email = input("Email do cliente: ")
telefone = input("telefone do cliente: ")
cadastrar_cliente(clientes,nome,email,telefone)

def ler_dados_csv():
    with open('clientes.csv', mode='r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            print(f"Nome:{linha['Nome']}, Email: {linha['Email']}, Telefone:{['Telefone']}")
            cadastrar_cliente(clientes,nome,email,telefone)

def gravar_dado():
    

def criar_arquivo_csv():
    with open('arquivo_csv', mode="w", newline="") as arquivo_csv:
        writer=csv.writer(arquivo_csv) #criar um novo arquivo
        writer.writerow(["Nome","Email","Telefone"])
    
        for clientee in clientes: #para navegar no dicionário
             writer.writerow([clientee["Nome"], clientee["Email"], clientee["Telefone"]])
             print("salvo!")

while True:
    print("MENU\n"
        "1. cadastrar \n"
        "2. imprimir\n"
        "3. salvar\n")
    opcao=int(input("escolha uma opção"))

    if opcao == 1:
        nome = input("nome do cliente: ")
        email = input("Email do cliente: ")
        telefone = input("telefone do cliente: ")
        cadastrar_cliente(clientes,nome,email,telefone)
    elif opcao == 2:
        ler_dados_csv()

    elif opcao == 3:
        print("salvo com sescesso!")