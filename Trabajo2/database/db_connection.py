import pymysql as conn

class Connex:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = conn.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             database = 'superbase'
            )
            print("Conexion exitosa a mysql")

        except Exception as e:
            print("Error de conexion", e)

    def close(self):
        if self.connection:
            self.connection.close()