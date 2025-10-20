import bcrypt

class Encoder:

    def encode(self, string):  
        #encode,convierte a bytes, genera un salt aleatorio y obtiene un hash seguro 
        result=bcrypt.hashpw(string.encode('utf-8'), bcrypt.gensalt())    
        #convertir el hash (que está en bytes) a un string  
        return result.decode('utf-8')
    def decode(self, string, password):
        #convierte los string a byte, para poder comparar y a string, se le agrega
        #el mismo salt que tiene almacenado password
        result = bcrypt.checkpw(string.encode('utf-8'),password.encode('utf-8'))
        return result

if __name__ == '__main__':
    print(Encoder().encode("123"))