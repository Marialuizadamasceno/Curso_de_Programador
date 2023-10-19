import mysql.connector
config ={
'user':'root',
'password':'root',
'host':'127.0.0.1',
'database':'maria2.0'
}

try:
    con = mysql.connector.connect(**config)
    if con.is_connected():
        print("certo")
        con.close
except mysql.connector.Error as err:
    print("erro")