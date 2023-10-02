def cadastrar_produto(produtos,nome,valor,imposto1,imposto2,imposto3,quantidade,frete,lucro):
    produto={
    'Nome':nome,
    'Valor':valor,
    'Imposto1':imposto1,
    'Imposto2':imposto2,
    'Imposto3':imposto3,
    'Quantidade': quantidade,
    'Frete': frete,
    'Lucro': lucro
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def imprimir_produto(produtos):
    for indice,produto in enumerate(produtos):
        print(f"produto {indice+1}")
        print(f"Nome: {produto['Nome']}")
        print(f"Valor:{produto['Valor']}")
        print(f"Imposto1:{produto['Imposto1']}")
        print(f"Imposto2:{produto['Imposto2']}")
        print(f"Imposto3:{produto['Imposto3']}")
        print(f"Quantidade:{produto['Quantidade']}")
        print(f"Frete:{produto['Frete']}")
        print(f"Lucro:{produto['Lucro']}")
        print("************************************")
       
produtos = []
while True:
    print("n\MENU")
    print("1. cadastrar produto")
    print("2. imprimr produto")
    print("3.sair")
    opcao=int(input("escolha uma opção: "))
    if opcao == 1:
        nome = input("produto: ")
        valor= float(input("valor"))
        imposto1= float(input("imposto 1"))
        imposto2= float(input("imposto 2"))
        imposto3= float(input("imposto 3"))
        quantidade= float(input("quantidade"))
        frete=float(input("frete"))
        frete=frete/quantidade
        custo=(quantidade*valor)+(imposto1+imposto2+imposto3+frete)
        print("custo: ", custo)
        lucro=float(input("lucro"))
        imposto1= (valor*imposto1)/100
        imposto2= (valor*imposto2)/100 
        imposto3= (valor*imposto3)/100 
        frete=frete/quantidade
        custo=(quantidade*valor)+(imposto1+imposto2+imposto3+frete)
        print("custo: ", custo)
        lucro=(custo*lucro)/100
        print("valor lucro: ",lucro)
        total=lucro+custo
        print(total)
        cadastrar_produto(produtos,nome,valor,imposto1,imposto2,imposto3,quantidade,frete,lucro)
        imprimir_produto(produtos)
    elif opcao == 2:
        imprimir_produto(produtos)
    elif opcao == 3:
        print("caindo fora...")
        break
    else:
        print("opção inválida")
