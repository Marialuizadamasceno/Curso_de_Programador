distancia=float(input("digite a distância em km:" ))
velocidade=float(input("digite a velocidade em km/h"))
vm=distancia/velocidade
horas=int(vm)
minutos=int((vm-horas)*60)
print(horas,minutos)
