numeros=[]
while True:
    numero=float(input("Digite um número de 1 a 10"))
    if numero >= 0 and numero <= 10:
       print("correto",numero)
       break
    else:
        print("errado, tente de novo")
    