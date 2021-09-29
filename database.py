import sqlite3 as s

kdb = "kdb/know.db"

class database:
    def consulta(self, query):
        try:
            c = s.connect(kdb)
            cu = c.cursor()
            get = cu.execute(query)
            c.commit()
            return get
        except:
            print("Error de conexión")