peso_dos_peixes=float(input("Escreva o peso dos peixes: "))
if peso_dos_peixes > 50:
    peso_excedente=peso_dos_peixes-50
    valor_a_ser_pago= peso_excedente*4
    print(valor_a_ser_pago)
else:
    print("não precisa pagar")