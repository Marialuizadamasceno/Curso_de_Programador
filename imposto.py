def cadastrar_cliente(produtos,nome,valor,imposto1,imposto2,imposto3,quantidade,frete,lucro):
    produto={
    'Nome':nome,
    'Valor':valor,
    'Imposto1':imposto1,
    'Imposto2':imposto2,
    'imposto3':imposto3,
    'Quantidade': quantidade,
    'Frete': frete,
    'Lucro': lucro
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def imprimir_produto(produtos):
    for indice,produto in enumerate(produtos):
        print(f"cliente {indice+1}")
        print(f"Nome: {produto['Nome']}")
        print(f"Valor:{produto['Valor']}")
        print(f"Imposto1:{produto['Imposto1']}")
        print(f"Imposto2:{produto['Imposto2']}")
        print(f"Imposto3:{produto['Imposto3']}")
        print(f"Quantidade:{produto['Quantidade']}")
        print(f"Frete:{produto['Frete']}")
        print(f"Lucro:{produto['Lucro']}")
        print("************************************")

        def total_produto(produtos):
            for indice,produto  in enumerate (produtos):
                total1=(f"Quantidade:{produto['Quantidade']*produto['Valor']}") 
                impos1=(f"Imposto1:{produto['Imposto1']*produto['Valor']}")
                impos2=(f"Imposto2:{produto['Imposto2']*produto['Valor']}")
                impos3=(f"Imposto3:{produto['Imposto3']*produto['Valor']}")
                fretes=(f"Frete:{produto['Frete']/produto['Quantidade']}")
                print(total1+impos1+impos1+impos2+impos3+fretes)
       
       
produtos = []
while True:
    print("n\MENU")
    print("1. cadastrar produto")
    print("2. imprimr produto")
    print("3. total ")
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

