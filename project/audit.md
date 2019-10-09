# Cloudmesh Encryption Security Audit

Updated: Oct. 03 2019  

## General Notes and Analysis


## Analysis: cloudmesh-cloud/cloudmesh/security/encrypt.py

1. Pending Answers from Gregor

### General Notes

1. Could be using pycryptography aka 'pyca' for basic crypto and file checks  
1. Could replace .format() with the new f"" syntax  
1. Should write system that encrypts bytes. That way you can pass in any data.  
1. Uses of path\_expand seem redundant given its use in the init function.  

### Notes on Functions

1. (ln:46) check\_key()  
    1. Uses homemade and could be using pyca's load pem funcs. This would allow
    for try/catching and have built in checks on file integrity.    
1. (ln:66) \_execute()  
    1. Can be replaced with cloudmesh Shell  
1. (ln:98) pem\_verify()  
    1. Note left stating it is non-functional. Investigate  
1. (ln:71) check\_passphrase()  
    1. Unnecessarily generates new key with same password.  
    1. Could utilize pyca's pubilc or private load\_pem\_key()  
1. (ln:110) pem\_create()  
    1. path\_expand should not expand entire command string but exact files
    path\_expand appears redundant due to init() expansion  
1. (ln:123) pem\_cat()  
    1. Displays the contents of a private pem file!!! (see pem\_create)  
1. (ln:136) decrypt()  
    1. Allows use of -out argement with empty string
1. (ln:146) main call  
    1. Safer to define test function instead of allowing main

### Open Questions

1. Why is the rsa format being used?  
    1. Familiarity of past programmer or technical requirement of Cloudmesh?  
    1. Could the smaller ECC keys be used to decrease communication cost?  
1. Why does the recommended key gen not use --pubout? Needs updating?  
1. Why is the pem path using default locations instead of pulling info from config?  
1. Where is the location of every instance this class is initiated or called?  
1. path\_expand is used multiple times on the 'pem' var. Is this necessary?  
1. Password stored in dict. Would any VERBOSE() call be able to access it?  

### Open Tasks

1. Look at every cms call on Encrypt  
1. Investigate what verify was attempting to do  

## Analysis: cloudmesh-cloud/cms/management/configuration/security/encryption.py

1. Current

### General Notes

1. Passwords are written to files. They should either be stored in some type of
password manager or avoided by manipulating the bytes directly  
1. The use of path\_expand() seem unnecassary given the init function  
1. Use of aes-cbc with openssl should be avoided, due to potential padding-oracle
attacks. Using aes-gcm avoids risk and introduces integrity and auth checks.  
1. Could avoid the randomKey function if using ECC key derivation. 
1. ssh-keygen is destructive if id\_rsa already exists. Should use path args. 
1. Missing verification of public and private keys on cert  
1. 

### Notes on Functions

1. getPublicKey()  
    1. Assuming cert is X.509 you can use pyca to extract the key
1. pem\_verify(): attempts to verify cert chain of trust  
    1. Issue unde investigation
1. check\_key(): checking if private key is in PEM format  
    1. could use pyca's load pem functions which already has checks

### Open Questions


