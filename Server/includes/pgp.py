from OpenSSL import crypto
from Crypto.Cipher import AES
from hashlib import md5
import random

class PublicKey():
    def __init__(self, password, data=""):
        self.password = hashlib.md5(password.encode("UTF-8").digest())
        self.data = data
        self.crypt = AES.new(self.password)

    def encrypt():
        dlen = len(self.data)
        to_add = (16 - (dlen % 16))
        self.data.ljust(to_add)
        return self.crypt.encrypt(self.data)

    def decrypt():
        return self.crypt.decrypt(self.data).strip()
    

def create_key(username,uid):
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2014)
    cert = crypto.X509()
    cert.get_subject().C = "PG"
    cert.get_subject().ST = str(uid)
    cert.get_subject().L = "PRAGMATIKA"
    cert.get_subject().OU = "CERT.PRAGMATIK"
    cert.get_subject().O = username
    cert.get_subject().CN = "decentralized"
    cert.set_serial_number(random.randrange(1000,100000))
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha1')

    return (crypto.dump_certificate(crypto.FILETYPE_PEM, cert), crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

# example usage create_key("samaldis",332)