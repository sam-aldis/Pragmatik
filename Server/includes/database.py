import sqlite3

DB_LOCATION = "./db/clients.db"

def install():
    con = sqlite3.connect(DB_LOCATION)
    con.cursor().execute("CREATE TABLE trackers (ip text, connected int)")
    con.commit()
    con.close()

def get_clients():
    con = sqlite3.connect(DB_LOCATION)
    try:
        results = con.cursor().execute("SELECT * FROM trackers WHERE connected > 0")
        con.close()
        return results
    except:
        con.close()
        install()
        return get_clients()

def get_client(ip):
    con = sqlite3.connect(DB_LOCATION)

def add_client(ip,active):
    con = sqlite3.connect(DB_LOCATION)
    
