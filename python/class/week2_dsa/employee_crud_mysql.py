import pymysql

def connectDb():
    connection = None
    try:
        connection = pymysql.Connect(host="localhost", user="root", password="root", database="db1", port=3306, charset="utf8")
        print('Database Connected')
    except:
        print('Database Connection Failed')
    return connection

connection = connectDb()