quanto_ganha_por_hora=float(input("Quanto você ganha por hora ?"))
quantas_horas_por_mes=float(input("Quantas horas você trabalha por mês?"))
salario_bruto=(quanto_ganha_por_hora*quantas_horas_por_mes)
imposto1=salario_bruto*0.11
print("valor a ser pago para o IR",imposto1)
imposto2=salario_bruto*0.08
print("valor a ser pago para o INSS",imposto2)
imposto3=salario_bruto*0.05
print("valor a ser pago para o sindicado",imposto3)
soma_dos_impostos=imposto1+imposto2+imposto3
print("a soma dos impostos : ", soma_dos_impostos)
salario_liquido=salario_bruto-soma_dos_impostos
print(salario_liquido)