def cadastrar_produto(produtos,produtoA, preco, quantidade):
    produto={
        'Produtos':produtoA,
        'Preco':preco,
        'Quantidade':quantidade
        }
    produtos.append(produto)
    print("produto cadastrado!;)")

def imprimir_produto(produtos):
    for indice,produto in enumerate (produtos) : 
        print(f"produto {indice+1}")
        print(f"Podutos: {produto['Produtos']}")
        print(f"Preco:{produto['Preco']}")
        print(f"Quantidade:{produto['Quantidade']}")
        print(f"TOTAL:{produto['Quantidade']*produto['Preco']}")
        print("************************************")

def total_produto(produtos):
    for indice,produto  in enumerate (produtos):
       print(f"Quantidade:{produto['Quantidade']*produto['Preco']}")


produtos=[]

while True:
    print("n\MENU")
    print("1. cadastrar produto")
    print("2. imprimir produto")
    print("3. preço total")
    print("4. sair")
    opcao=int(input("digite um número"))
    if opcao == 1:
        produtoA=input("produto")
        preco=float(input("preço"))
        quantidade=int(input("quantidade"))
        cadastrar_produto(produtos,produtoA, preco, quantidade)
        imprimir_produto(produtos)
    elif opcao == 2:
        imprimir_produto(produtos)
    elif opcao == 3:
        total_produto(produtos)
    elif opcao == 4:
        print("bye bye")
        break
    else:
        print("opção inválida")






    


