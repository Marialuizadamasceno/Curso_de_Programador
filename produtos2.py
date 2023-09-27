
nomes = []
valores = []
estoques= []
fretes= []
lucros= []
custos=[]
vendas=[]
imposto1=0.12
imposto2=0.06
imposto3=0.03
while True:
    menu=float(input("escolha uma opção para o menu:\n"
    "1 - insira um novo produto\n"
    "2 - atualiar produto\n"
    "3 - imprimir\n"
    "4 - deletar\n"
    "5 - sair\n"))
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
    for i in range(len(nomes)):
        nomes=nome[i]
        estoques=estoque[i]
        lucros=(lucro/estoques)[i]
        valores=valor[i]
        imposto1= (valor * 0.12)
        imposto2= (valor * 0.06)
        imposto3=(valor * 0.03)
        custo=(valor+imposto1+imposto2+imposto3)+(frete/estoque)
        custos.append(custo)
        venda=(custo+(custo*lucro))
        vendas.append(venda)
    for i in range(len(nome)):
        print(nome, "custo:", custo, "venda",venda)
    