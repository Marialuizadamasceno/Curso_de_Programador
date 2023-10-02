valor_produto = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade: "))
imposto1 = float(input("Digite o valor do imposto 1: "))
imposto2 = float(input("Digite o valor do imposto 2: "))
imposto3 = float(input("Digite o valor do imposto 3: "))
frete = float(input("Digite o valor do frete: "))
frete2= frete/quantidade

imposto1 = (valor_produto * imposto1)/100
imposto2= (valor_produto * imposto2)/100
imposto3=(valor_produto * imposto3)/100
preco_custo=valor_produto+imposto1+imposto2+imposto3+frete2
 
preco_venda = preco_custo + (preco_custo * 0.6)

print("O preço de custo é:", preco_custo)
print("O preço de venda é:", preco_venda)