import sqlite3

def install():
    con = sqlite3.connect("./db/clients.db")
    results = con.cursor().execute("CREATE TABLE trackers (ip text, connected int)")
    con.commit()
    con.close()

def get_clients():
    con = sqlite3.connect("./db/clients.db")
    try:
        results = con.cursor().execute("SELECT * FROM trackers")
        for res in results:
            print(res)
    except:
        install()
        get_clients()