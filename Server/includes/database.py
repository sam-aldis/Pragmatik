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
        cur = con.cursor()
        cur.execute("SELECT * FROM trackers WHERE connected > 0")
        results = cur.fetchall()
        con.close()
        res = []
        try:
            for result in results:
                res.append(result)
        except: 
            pass    
        return res
    except:
        con.close()
        install()
        return get_clients()

def update_client(ip):
    con = sqlite3.connect(DB_LOCATION)
    cur = con.cursor()
    client = get_client(ip)
    if client[1] <= 4:
        cli_new = int(client[1]) + 1
        cur.execute("UPDATE trackers SET connected=? WHERE ip=?", (cli_new, ip))
        con.commit()
    con.close()

def scan_and_decrease():
    con = sqlite3.connect(DB_LOCATION)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM trackers WHERE connected > 0")
    results = res.fetchall()
    for result in results:
        new_count = result[1] - 1
        cur.execute("UPDATE trackers SET connected=? WHERE ip=?", (new_count, result[0]))
        con.commit()
    con.close()
    
def get_client(ip):
    con = sqlite3.connect(DB_LOCATION)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM trackers WHERE ip=?", (ip,))
    ret = cur.fetchone()
    return ret

def add_client(ip,active):
    if get_client(ip) == None:
        con = sqlite3.connect(DB_LOCATION)
        cur = con.cursor()
        cur.execute("INSERT INTO trackers (ip, connected) VALUES (?,?)",(ip,active))
        con.commit()
        con.close()
    else:
        update_client(ip)