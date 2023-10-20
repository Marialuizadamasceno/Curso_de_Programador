import mysql.connector
#conectar ao banco de dados
config = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="maria2.0"
)
#criar cursor para executar comeandos em SQL
cursor = config.cursor()
def criar_cliente(nome,telefone,email,atraso,livros_idlivros,tempo_idtempo):
    sql= "INSERT INTO cliente (nome,email,telefone, atraso,livros_idlivros,tempo_idtempo) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (nome,telefone,email,atraso,livros_idlivros,tempo_idtempo)
    cursor.execute(sql,val) #cursor é para executar comandos em sql
    config.commit()
    print("cliente inserido com suscesso!")

def listar_clientes():   
    cursor.execute("SELECT * FROM cliente")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)
        
def atualizar_clientes( idcliente,nome,telefone,email,atraso,livros_idlivros,tempo_idtempo):
    sql= "UPDATE cliente SET nome=%s,email=%s,telefone=%s,atraso=%s,livros_idlivros=%s,tempo_idtempo=%s WHERE idcliente = %s"
    val= (nome,telefone,email,atraso,livros_idlivros,tempo_idtempo,idcliente)
    cursor.execute(sql,val)
    config.commit()
    print("cliente atualizado com suscesso!")

def deletar_cliente(idcliente):
    sql= "DELETE FROM cliente WHERE idcliente = %s"
    val = (idcliente,)
    cursor.execute(sql,val)
    config.commit()
    print("cliente excluído com suscesso!")
    
    
 
def menu():
    while True: 
        print("n\MENU")
        print("1. cadastrar cliente")
        print("2. imprimr cliente")
        print("3. atualizar")
        print("4. excluir")
        print("5. sair")
        
        opcao=int(input("escolha uma opção: "))
        
        if opcao == 1:
            nome = input("nome do cliente: ")
            email = input("Email do cliente: ")
            telefone = input("telefone do cliente: ")
            atraso = input("dias atrasados")
            livros_idlivros = input("id do livro")
            tempo_idtempo = input("id dos prazos")
            criar_cliente(nome,telefone,email,atraso,livros_idlivros,tempo_idtempo)
    
        elif opcao == 2:
            listar_clientes()
        
        elif opcao == 3:
            idcliente= input("digite o id do cliente")
            nome= input("novo nome")
            email = input("novo Email do cliente: ")
            telefone = input("novo telefone do cliente: ")
            atraso = input("atualize o atraso")
            livros_idlivros = input("novo id do livro")
            tempo_idtempo = input("novo id dos prazos")
            atualizar_clientes(idcliente,nome,telefone,email,atraso,livros_idlivros,tempo_idtempo)
            
        elif opcao == 4:
            idcliente=input("digite i id do cliente que deseja excluir")
            deletar_cliente(idcliente)
            
        elif opcao == 5:
            print("finalizado")
            break
            
        
            
            
        
if __name__ == "__main__":
    menu()
    
        
    #fechar cursor e a conexão com o banco de dados
    cursor.close()
    config.close()

