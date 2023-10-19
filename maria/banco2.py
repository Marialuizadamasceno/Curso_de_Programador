import mysql.connector
 #configuração da conexão com banco de dados
config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database':'maria2.0'
}

try:
    con = mysql.connector.connect(**config) #con = variável, ** ignora o dicionário
    if con.is_connected(): #variável, is_connected para verificar se a conexação teve êxito.
        print("certo")
        con.close() #fechar a conexão
except mysql.connector.Error as err: #nomear
    print("erro",err)