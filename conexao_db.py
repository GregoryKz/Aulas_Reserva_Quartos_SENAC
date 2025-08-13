import pymysql

def conectar ():
    return pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'reserva_quartos_db'
    )
