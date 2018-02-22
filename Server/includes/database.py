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
        res = []
        for result in results:
            res.append(result)
        return res
    except:
        con.close()
        install()
        return get_clients()

def update_client(ip):
    con = sqlite3.connect(DB_LOCATION)
    cur = con.cursor()
    client = get_client(ip)
    

def get_client(ip):
    con = sqlite3.connect(DB_LOCATION)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM trackers WHERE ip=?", ip)
    print(res)
    return res

def add_client(ip,active):
    if get_client(ip) == None:
        con = sqlite3.connect(DB_LOCATION)
        cur = con.cursor()
        cur.execute("INSERT (ip, connected) INTO trackers(?,?)",(ip,active))
        con.commit()
        con.close()
    else:
        update_client(ip)