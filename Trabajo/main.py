from database.db_connection import Connex

if __name__ == "__main__":
    db = Connex()
    db.connect()
    db.close()
