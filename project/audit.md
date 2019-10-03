# Cloudmesh Encryption Security Audit

Updated: Oct 2 2019  

## General Notes and Analysis

1. Could be using pycryptography aka 'pyca' for basic crypto and file checks  
1. Could replace .format() with the new f"" syntax  
1. Should write system that encrypts bytes. That way you can pass in any data.  

## Analysis: cloudmesh-cloud/cloudmesh/security/encrypt.py

1. In Progress  

### General Notes

1. (ln:46) check\_key()  
    1. Uses homemade and could be using pyca's load pem funcs. This would allow
    for try/catching and have built in checks on file integrity.    
1. (ln:66) \_execute()  
    1. Can be replaced with cloudmesh Shell  
1. (ln:98) pem\_verify()  
    1. Note left stating it is non-functional. Investigate  
1. (ln:110) pem\_create()  
    1. path\_expand should not expand entire command string but exact files
    path\_expand appears redundant due to init() expansion  
1. (ln:123) pem\_cat()  
    1. Displays the contents of a private pem file (see pem\_create)  
1. (ln:136) decrypt()  
    1. Allows use of -out argement with empty string
1. (ln:146) main call  
    1. Safer to define test function instead of allowing main

### Open Questions

1. Why is the rsa format being used?   
    1. Familiarity of past programmer or technical requirement of Cloudmesh?  
    1. Could the smaller ECC keys be used to decrease communication cost?  
1. Does the top comment need to be updated? It outputs a private pem file.  
1. Why is the pem path using default locations instead of pulling info from config?  
1. Where is the location of every instance this class is initiated or called?  
1. path\_expand is used multiple times on the 'pem' var. Is this necessary?  
1. Password stored in dict. Would any VERBOSE() call be able to access it?  

### Open Tasks

1. Look at every cms call on Encrypt  
1. Investigate what verify was attempting to do  

## Analysis: cloudmesh-cloud/cms/management/configuration/security/encryption.py

1. TODO
