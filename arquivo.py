import csv  # csv é o arquivo separado por vírgula,

clientes=[
    {"nome": "joão", "email": "joao@example.com", "telefone": "123-456-789"},
    {"nome": "Maria", "email": "Maria@example.com", "telefone": "123-456-788"},
    {"nome": "Pedro", "email": "Pedro@example.com", "telefone": "123-456-785"}
]#colchetes para array #chaves para dicionário
with open ('arquivo_csv', mode="w", newline="") as arquivo_csv:
    writer=csv.writer(arquivo_csv) #criar um novo arquivo
    writer.writerow(["Nome","Email","Telefone"])
    
    for cliente in clientes:#para navegar no dicionário
        writer.writerow([cliente["nome"], cliente["email"], cliente["telefone"]])
print("salvo!")