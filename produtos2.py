
nomes = []
valores = []
estoques= []
fretes= []
lucros= []
custos=[]
vendas=[]
imposto1=[]
imposto2=[]
imposto3=[]
while True:
    print("n\MENU")
    "1 - insira um novo produto\n"
    "2 - atualiar produto\n"
    "3 - imprimir\n"
    "4 - deletar\n"
    "5 - sair\n"))
    opcao=int(input("escolha uma opção: "))
    if menu == 1:
        nome = input("digite o nome do produto: ")
        nomes.append(nome)
        valor = input("digite o valor: ")
        valores.append(valor)
        estoque = input("digite o estoque: ")
        estoques.append(estoque)
        frete = float(input("digite o valor do frete: "))
        fretes.append(frete)
        lucro = float(input("quanto deseja deseja ganhar em porcentagem: "))
        lucros.append(lucro)
    for b in range(nome)
        Valor= valor(b)
        imposto1= (Valor[b] * 0.12)
        imposto2= (Valor[b] * 0.06)
        imposto3=(Valor[b] * 0.03)
        custo=(valor+imposto1+imposto2+imposto3)+(frete/estoque)
        custos.append(custo)
        venda=(custo+(custo*lucro))
        vendas.append(venda)
        print(nome, "custo:", custo, "venda",venda)
    