b=0
nomes= ["maionese","batata","arroz"]
precos=[50.00,2.50,37.00]
quantidade=[20, 10, 15]
for b in range(len(nomes)):
    nome=nomes[b]
    preco=precos[b]
    total=quantidade[b]*precos[b]
    numero=quantidade[b]
    print("Produto:",nome,"quantidade:", numero,"preço total:",total)