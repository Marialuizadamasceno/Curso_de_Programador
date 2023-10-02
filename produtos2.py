
nomes = []
valores = []
estoques= []
fretes= []
lucros= []
custos=[]
vendas=[]
imposto11=[]
imposto22=[]
imposto33=[]
while True:
    print("n\MENU"
    "1 - insira um novo produto\n"
    "2 - valor total\n"
    "3 - imprimir\n"
    "4 - deletar\n"
    "5 - sair\n")
    opcao=int(input("escolha uma opção: "))
    if menu == 1:
        nome = input("digite o nome do produto: ")
        nomes.append(nome)
        valor = float(input("digite o valor: "))
        valores.append(valor)
        estoque = float(input("digite o estoque: "))
        estoques.append(estoque)
        frete = float(input("digite o valor do frete: "))
        fretes.append(frete)
        lucro = float(input("quanto deseja deseja ganhar em porcentagem: "))
        lucros.append(lucro)
        imposto1=float(input("imposto 1"))
        imposto11.append(imposto1)
        imposto2=float(input("imposto 2"))
        imposto22.append(imposto2)
        imposto3=float(input("imposto 3"))
        imposto33.append(imposto3)
        print("salvo")
        elif opcao==2:
        Valor= valor[b]
        Imposto1=imposto1[b]
        Imposto2=imposto2[b]
        Imposto3=imposto3[b]
        Imposto1= (Valor * imposto1)
        Imposto2= (Valor *imposto2)
        Imposto3=(Valor * imposto3)
        Frete=frete/estoque
        custo=(valor+Imposto1+Imposto2+Imposto3)+Frete
        custos.append(custo)
        venda=(custo+(custo*lucro))
        vendas.append(venda)
        print(nome, "custo:", custo, "venda",venda)
    