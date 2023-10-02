populacaoA=int(input("Digite a população"))
populacaoB=int(input("Digite a população"))
crescimentoA=float(input("Digite a taxa de crescimento A : "))
crescimentoB=float(input("Digite a taxa de crescimento B : "))
contagem=0
while populacaoA<populacaoB:
    populacaoA=populacaoA*crescimentoA+populacaoA
    populacaoB=populacaoB*crescimentoB+populacaoB
    contagem=contagem+1
print(contagem)