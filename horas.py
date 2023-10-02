distancia=float(input("digite a distância em km:" ))
velocidade=float(input("digite a velocidade em km/h"))
vm=distancia/velocidade
horas=int(vm) #int porque fica so  numero inteiro, ex:1.5 = 1
minutos=int((vm-horas)*60) #1.5-1= 0.5 multipliado por 60, dessa forma saberemos os minutos.
print(horas,minutos)
