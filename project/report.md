# Encryption of Cloud Secrets

- Andrew Holland  

  - repo: [fa19-516-144](<https://github.com/cloudmesh-community/fa19-516-144/tree/master>)  
  - email: hollanaa@iu.edu  

* [Contributors](<https://github.com/cloudmesh-community/fa19-516-144/graphs/contributors>)  
* [Forked Branch](<https://github.com/ElectricErudite/cloudmesh-cloud>)

## Introduction

The Cloudmesh project lacks certain security capabilities and secure coding  
practices. General improvements are required to address three primary concerns.  

First, the code base requires a general audit on all files using openssl.  
Currently two files are responsible for the security protocols and usage of  
openssl. Namely the cloudmesh-cloud/cloudmesh/security/encrypt.py and   
cloudmesh-cloud/cms/management/configuration/security/encryption.py files.  
These files require a full audit and update to use well-defined modules.   

Second, security related configuration files require obscuring secrets.  
Presently the cloudmesh.yaml file responsible for configuring Cloudmesh has all  
data presented in clear-text. The ``` cms config cat less ``` command obscures  
the passwords within the config file, but only for the screen. Any malicious  
user with read access to the file would be able to extract all passwords  
set within Cloudmesh. The config file should encrypt the password bytes by   
default to decrease the attack surface on Cloudmesh.   

After addressing the primary concerns Cloudmesh will be capable of being  
further extended to integrate password managers directly into secrets  
management. This could include software such as Keepass. If successful,  
Cloudmesh can automate the generation, storage, and access of the keys and config.  

## Implementation

### Encrypting Cloudmesh.yaml  

#### Automating Key Management

##### SSH-Agent  

Original plans included integrating ssh-agent to automatically retrieve  
passwords for key operations (such as encryption). This goes against the  
functionality of the SSH-Agent. As referenced in the IETF informational  
documentation for ssh-agent found 
[here](<https://tools.ietf.org/html/draft-miller-ssh-agent-00#section-4.5>) 
details that the agent should only  
be used for signing data.  

The ssh-agent is used to prove possession of the private key without exposing  
the private bytes of the key. This is done by generating a public-private key  
pair and sending the public key to the server. When you attempt to ssh to the  
server it will request a signature of some random data. When you retrieve the  
data you request the ssh-agent signs it and this signed data is sent back to  
the server. Since the signature can be validated by the public key you prove  
the private key is within your possession. Notice this is different than using  
the actual key bytes.   

To give a practical example of the agent being unable to provide private key  
bytes we can reference the [ssh_agent demo directory](<https://github.com/cloudmesh-community/fa19-516-144/tree/project/project/demo/ssh_agent>).  
In short, we will use a public-private key pair to encrypt some data.  
Even if the private key is added to the ssh-agent a password will be prompted.  
Please read the README within the directory further explanation.  

## Proposed Software to Integrate into Project

* Keepass(2)  
* python module: python cryptography  
* ssh-keygen  

## Related Concepts

* Elliptic Curve Cryptography  
* Advanced Encryption Standard Galois Counter Mode (AES-GCM)

## References

## Tasks

### Openssl Security Audit  

[Forked Branch](<https://github.com/ElectricErudite/cloudmesh-cloud/tree/audit>)  

### Encrypting Cloudmesh.yaml Secrets  

[Forked Branch](<https://github.com/ElectricErudite/cloudmesh-cloud/tree/audit>)  

## Progress

### Week of Monday Nov. 25th  

1. Changed encoding of secrets from base64 to integers  
1. Added cloudmesh.security section in cloudmesh.yaml default config  
1. Added cloudmesh.security.secrets to use regexp to pick attributes for encryption  
1. Implemented file reversion in case encryption or decryption fails  

### Week of Monday Nov. 18th  

1. Added writefd() to cloudmesh-common/util.py to allow writing permissions  
1. Added wr only permissions to nonce and key files  

### Week of Monday Nov. 11th  

1. add get\_path() function to Config() class to return yaml dot path(s) to key  
1. implemented means to get value from config given a dot path to key the get()  
This was necessary since the Config.get() function couldn't handle dot paths.  
1. Wrote script to begin testing encryption of config values  
1. Began integration into cloudmesh by testing Config.set with encrypted data  
1. Added file permission argument to cloudmesh.common.util.writefile  
1. Edited ```cms config encrypt``` to encrypt the config file  

### Week of Monday Nov. 4th  

1. Implemented asymmetric encryption using rsa  
1. wrote script to demonstrate ssh-agent cannot be used with encryption   
1. added README for running the scripts
1. added CmsHasher class to hash data (can be used for unique file name generation)  

### Week of Monday Oct. 28th  

1. Investigated using ssh-agent modules paramiko, and ssh2-python  
1. Investigated ssh-agent documentation. Discovered use case is for signing only.  
1. Implemented symmetric encryption using AES-GCM  

### Week of Monday Oct. 21st  

1. Finished Analysis of openssl related files found [here](<https://github.com/cloudmesh-community/fa19-516-144/blob/audit/project/audit.md>)
1. Established weekly meeting time with partner.  
1. Discussed cms key and cms keygroup commands with partner. 
1. Updated project.md to address concerns related to partner's project. 
1. Added initial writings for book chapters within the /project/chapters dir
1. Added initial encryptor and pem\_handler to replace old encrypt.py

### Week of Monday Oct. 14th

1. Created the KeyGroup.py file to handle key groups  

   1. Need to investigate the purpose of SecGroup.output  

1. Designed queries

### Week of Monday Oct. 07th

1. Forked cloudmesh-cloud to local repo  
   
   1. fork located [here](<https://github.com/ElectricErudite/cloudmesh-cloud>)  

1. Edited cms key --source=FILEPATH to now parse filepath argument  

   1. Within [key-group branch](<https://github.com/ElectricErudite/cloudmesh-cloud/tree/key-group>)  

1. Investigating how to add new local-keygroup collection to database  
1. Installed robo3t to observe changes to local mongodb  

### Week of Monday Sep. 30th 

1. Researched password managers for future integration discovered 

   1. [kpcli](<http://kpcli.sourceforge.net/>)  
   1. [gopass](<https://www.gopass.pw/>)  
   1. [kedpm](<http://kedpm.sourceforge.net/>)  
   1. [keepass2 cli](<https://keepass.info/help/base/cmdline.html>)  

1. Submitted PR for debian 9 installation of mongo  
1. Installed docker on local system to ease testing
1. Began audit of cms-cloud/cms/security/encrypt.py-bug check /project/audit.md
1. Took second pass look through the encrypt.py-bug. Wrote questions for Gregor  
