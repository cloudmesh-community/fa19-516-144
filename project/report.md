# Encryption of Cloud Secrets

- Andrew Holland  

  - repo: [fa19-516-144](<https://github.com/cloudmesh-community/fa19-516-144/tree/master>)  
  - email: hollanaa@iu.edu  

* [Contributors](<https://github.com/cloudmesh-community/fa19-516-144/graphs/contributors>)  
* [Forked Branch](<https://github.com/ElectricErudite/cloudmesh-cloud>)

## Introduction  

The Cloudmesh project does not include the encryption of its secrets within the  
cloudmesh.yaml file. This introduces major concers if the yaml file is  
accidentally shared or if a malicious agent gets access to the local machine.  
Either of these scenarios would mean the total exposure of all secrets the user  
added to cloudmesh.  

The first major task is creating a series of general tools that can be used to  
repalce the current EncryptFile class. The EncryptFile class only offers  
encryption using the default name and a few openssl calls. The new suite should  
be able to provide symmetric and assymmetric encryption, hashing, password  
collection, key loading, and key verification. These features can all be added  
by using trused modules such as python cryptography or 'pyca'.  

The second task involves updating the current ```cms config encrypt``` and  
```cms config decrypt``` commands that can take the new suite's tools and  
encrypt the specific attributes that should be kept secret. This will also  
require introducing a new section to the cloudmesh.yaml file that controls  
security and some customizable way for users to decide which attributes should  
be encrypted.   

After addressing these tasks Cloudmesh users will be capable of having finer  
control over the security features of cloudmesh. This may also introduce  
further security opportunities that could be addressed in the future.   

## Process  

### Installation  

Assuming the following PRs are approved.   
* [cms-cloud](<https://github.com/cloudmesh/cloudmesh-cloud/pull/245>)  
* [cms-configuration](<https://github.com/cloudmesh/cloudmesh-configuration/pull/2>)  

1. Install cloudmesh-cloud as directed in the cloudmesh v4 documentation  
  - [documentation](<https://cloudmesh.github.io/cloudmesh-manual/installation/install.html>)  

### Preperation  

1. Generate an RSA public-private key pair using your favorite tool  
1. Run ```cloudmesh config secinit```  
1. Run ```cloudmesh config set cloudmesh.security.publickey=PATH```  
  - Where PATH is the path to your RSA public key  
1. Run ``cloudmesh config set cloudmesh.security.privatekey=PATH```  
  - Where PATH is the path to your RSA private key  
1. Edit the cloudmesh.yaml file with your favorite editor  
  - Under the cloudmesh.security.secrets section add regular expressions to
catch any secret you wish to encrypt. Reference the implementation section
below for more details.  

### Encryption  

1. Run ```cloudmesh config encrypt```  
  - Note: that the cloudmesh.version attribute should NOT be changed while the  
    file is encrypted. Please reference the Special Cases section below.   

### Decryption  

1. Run ```cloudmesh config decrypt```  
  - Enter the password for your private key when prompted.
Hit enter if there is no password   


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

## Special Cases

### Upgrading Cloudmesh.yaml After Encrypting Attributes  

The cloudmesh.yaml version number is tied to the encryption of the data. If the
version number is changed manually after the attributes are encrypted you will
NOT be able to decrypt the data. This is used to future-proof Cloudmesh
from attacks relaint on exploiting old version numbers. 

Simply run ```cloudmesh config decrypt``` before upgrading your config file. 

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
1. Created Pull Request for [cms-cloud](<https://github.com/cloudmesh/cloudmesh-cloud/pull/245>)  
1. Created Pull Request for [cms-common](<https://github.com/cloudmesh/cloudmesh-common/pull/10>)  
1. Created Pull Request for [cms-configuration](<https://github.com/cloudmesh/cloudmesh-configuration/pull/2>)  

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
