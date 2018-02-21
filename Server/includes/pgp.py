from OpenSSL import crypto
import random

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