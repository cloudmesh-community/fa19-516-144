import os
import re
from base64 import b64encode, b64decode
from getpass import getpass
from cloudmesh.common.console import Console
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import path_expand
from cloudmesh.common.variables import Variables
from cloudmesh.configuration.Config import Config
from cloudmesh.security.encrypt import CmsEncryptor, KeyHandler, CmsHasher

# Sets variables within  ~/.cloudmesh/var-data 
varz = Variables()
varz['debug'] = True
varz['trace'] = True
varz['verbose'] = 10

# Config vars
## Key directory
cwd = os.getcwd()
key_path = f"{cwd}/keys"
rsa_path = f"{key_path}/rsa"
gcm_path = f"{key_path}/gcm"
## Private Key Name
priv_name = "priv.pem"
priv_path = f"{rsa_path}/{priv_name}"
## Public Key Name
pub_name = "pub.pem"
pub_path = f"{rsa_path}/{pub_name}"

# Generate directory if necessary
if not os.path.isdir(key_path):
    os.makedirs(key_path)
if not os.path.isdir(rsa_path):
    os.makedirs(rsa_path)
if not os.path.isdir(gcm_path):
    os.makedirs(gcm_path)

# Generate new encryption key
if not os.path.exists(priv_path):
    kh = KeyHandler()
    r = kh.new_rsa_key(has_password = False)
    u = kh.get_pub_key_bytes()

    #Save Private Key 
    fo = open(priv_path, "wb", 0o600)
    fo.write(r)
    fo.close()

    #Save Public key
    fo = open(pub_path, "wb", 0o600)
    fo.write(u)
    fo.close()

# Iterate over cloudmesh secrets and encrypt data
ce = CmsEncryptor()
ch = CmsHasher()
config = Config()
d = config.dict()
secrets = config.secrets()

def write_file(data = None, path = None, purpose = "w", permissions = 0o600):
    fo = open(path, purpose, permissions)
    fo.write(data)
    fo.close()

#for secret in secrets:
#   paths = config.get_path(secret, d)
paths = config.get_path('AZURE_SECRET_KEY', d)
### loop for encryption
for path in paths:
    ## Determine filename
    h = ch.hash_data(path, "MD5", "b64", True)
    fp = f"{gcm_path}/{h}" 

    # get value from config
    v = config.get_value(path)
    #TODO: add check if v is empty

    #Prepare Encrypt data
    ## assign data
    data = v
    aad = "foobar"

    ## Encode data
    b_data = data.encode()
    b_aad = aad.encode()

    ## Encrypt data
    k, n, ct = ce.encrypt_aesgcm(data = b_data, aad = b_aad)

    ## Write ciphertext contents
    ct = b64encode(ct).decode()
    write_file(ct, fp)

    ## Write key
    k = b64encode(k).decode()
    write_file(k, f"{fp}.key")

    ## Write nonce
    n = b64encode(n).decode()
    write_file(n, f"{fp}.nonce")
    
    print(f"Encrypt:{path}")
    print(f"h: {h}")
    print(f"c: {ct}")
    print(f"v: {v}")
    print("")

def read_file(path = None):
    fo = open(path, 'r')
    data = fo.read()
    fo.close()
    return data

### Loop for decryption
for path in paths:
    print(f"Decrypt:{path}")
    h = ch.hash_data(path, "MD5", "b64", True)
    print(f"h: {h}")
    fp = f"{gcm_path}/{h}" 
    
    ct = read_file(fp)
    k = read_file(f"{fp}.key")
    n = read_file(f"{fp}.nonce")

    b_ct = b64decode(ct)
    b_k = b64decode(k)
    b_n = b64decode(n)

    b_aad = b"foobar"
    pt = ce.decrypt_aesgcm(key = b_k, nonce = b_n, aad = b_aad, ct = b_ct)
    pt = pt.decode()
    print(f"c: {ct}")
    print(f"v: {pt}")
    print("")
