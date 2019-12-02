# Encryption of Cloud Secrets

- Andrew Holland  

  - repo: [fa19-516-144](<https://github.com/cloudmesh-community/fa19-516-144/tree/master>)  
  - email: hollanaa@iu.edu  

* [Contributors](<https://github.com/cloudmesh-community/fa19-516-144/graphs/contributors>)  
* [fork cms-cloud](<https://github.com/ElectricErudite/cloudmesh-cloud>)  
* [fork cms-common](<https://github.com/ElectricErudite/cloudmesh-common>)  
* [fork cms-config](<https://github.com/ElectricErudite/cloudmesh-configuration>)  

## Introduction  

The Cloudmesh project does not include the encryption of its secrets within the  
cloudmesh.yaml file. This introduces major concerns if the yaml file is  
accidentally shared or if a malicious agent gets access to the local machine.  
Either of these scenarios would mean the total exposure of all secrets the user  
added to cloudmesh.  

The first major task is creating a series of general tools that can be used to  
replace the current EncryptFile class. The EncryptFile class only offers  
encryption using the default name and a few openssl calls. The new suite should  
be able to provide symmetric and asymmetric encryption, hashing, password  
collection, key loading, and key verification. These features can all be added  
by using trusted modules such as python cryptography or 'pyca'.  

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

1. Install cloudmesh-cloud as directed in the cloudmesh v4 [documentation](<https://cloudmesh.github.io/cloudmesh-manual/installation/install.html>)  

### Preparation  

1. Generate an RSA public-private key pair using your favorite tool  
  * One option includes openssl  
    * Run ```openssl genrsa -aes256 -out PRV_NAME 2048```  
    * Then run ```openssl rsa -in PRV_NAME -pubout -out PUB_NAME```  
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

### Decryption  

1. Run ```cloudmesh config decrypt```  
  - Enter the password for your private key when prompted.
Hit enter if there is no password   

## Implementation

### Cloudmesh.Security Section  

The cloudmesh.security section was added to allow users to control encryption.  
In the current implementation the security section has four noteworthy attributes.  

1. publickey: The path to the public key used to encrypt the attributes  
1. privatekey: The path to the private key used to decrypt the attributes  
  - This must be the private key-paired with the public key  
1. secpath: This is the operating system path that will hold keys and nonces  
1. secrets: A list of regular expressions to select which attributes to encrypt  

#### Selecting the Attributes  

The cloudmesh.security.secrets section is intended for users to add python regular  
expressions. These expressions are used to capture every attribute the user  
wishes to encrypt.  
To learn the specifics about regular expression please reference the 
[python re 3.7 documentation](<https://docs.python.org/3.7/library/re.html>)  

Inside the default config files exists two expressions to start the process.  
To be explicit, you should review the expressions to ensure they meet your  
security needs before encrypting the config file. The current implementation  
will **only** encrypt the attributes that the regular expressions detail.  

The first expression is: \*\.AZURE_SECRET_KEY  
This expression will encrypt all paths that end with AZURE_SECRET_KEY.  

The second expression: cloudmesh.comet.endpoints.dev.userpass.password  
This expression will encrypt the attribute at the end of the path.  
Please note that the regular expressions must be crafted with care.  

Reference the limitations section for more information.  

#### Listing Exceptions to Encryption  

The cloudmesh.security.exceptions section is intended to list attributes that  
must not be encrypted. This section also explicitly uses python regular  
expressions to capture which paths will **not** be encrypted. The default  
regexps are necessary to decrypt data after they are encrypted. This includes  
the entirety of the cloudmesh.security section and some mongodb attributes.    

The exceptions section has higher priority over the secrets section. If a  
path is matched between both the secrets and exceptions regular expressions the  
path attribute will **not** be encrypted.  

### Cloudmesh Tools for Encryption  

#### CmsEncryptor  

The CmsEncryptor class is a general encryptor tool used for both symmetric and
asymmetric encryption schemes. Currently RSA and AES-GCM encryption schemes
are the only available schemes for encryption. This is used to take bytes of
data and return the encrypted bytes with other data if necessary.  

#### CmsHasher  

The CmsHasher class is used for hashing techniques. Currently SHA256 and MD5  
are supported. Note MD5 is an **insecure** hashing tool. It should only be  
used when you are absolutely sure that the data being hashed does not need to  
be kept secret. The default and recommended hashing tool is SHA256.  

#### KeyLoader  

The KeyLoader class is responsible for opening and verifying the format of a
given key file. Some variety of keys and formats are supported. Currently
private keys can have PKCS8 or OpenSSL format and Public keys can have Subject
Info or OpenSSH formats. Both PEM and SSH encoding is supported. It can open
both passwordless and password-protected private key files.  

### Encrypting and Decrypting Cloudmesh Attributes  

#### Process for Encryption

1. Copy the contents of the config into a secure temporary file  
  - If at any time an error occurs the original config file is restored   
1. The cloudmesh.security.secpath value is queried from the config  
1. Load the key whose path is referenced in cloudmesh.security.publickey
1. For each regular expression, apply it on all paths of the config file  
1. For each applied path, get the value and hash the full path
1. Encrypt the value with CmsEncryptor using AES-GCM  
1. Take the generated key, generated, nonce, and ciphertext  
1. Encrypt the nonce and key with CmsEncryptor using RSA  
1. Store an integer encoding of the ciphertext in the cloudmesh config  
1. Store the encrypted key and nonce in separate files with the hash as base name  
1. Delete the temporary file

#### Process for Decryption  

1. Copy the contents of the config into a secure temporary file
  - If at any time an error occurs the original config file is restored   
1. Query the config for the value of cloudmesh.security.secpath  
1. Load the key whose path is referenced in cloudmesh.security.privatekey  
1. For each regular expression, apply it on all paths of the config file  
1. For each applied path produce the hash and load the nonce and key  
1. Decrypt the nonce and key with CmsEncryptor using RSA  
1. Get the ciphertext from the config down the full path  
1. Decrypt the ciphertext using the key, nonce, and cloudmesh.version number
1. Set the path attribute with the plaintext  
1. Delete the files with hash as base name in the secpath directory  
1. Delete the temporary file

#### Key Management

#### Keys Used in Encryption  

There are two keys used for encryption and decryption. The symmetric key which
is an AES-256 key that is automatically generated by CmsEncryptor and the
private-public RSA key pair generated by the user. 

The RSA key should be in PEM format, with 2048 bits. 

##### Attempt to Automate with SSH-Agent

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

## Limitations  

### Non-Authenticated Data  

Initially the CMS Encryptor utilized AES-GCM Additional Authenticated Data or  
'aad'. The aad is non-secret data that can be paired with encryption to  
guarantee the integrity of some other data. Originally the CmsEncryptor used the  
cloudmesh version number as the aad. This introduced some instability when  
encrypting large data sets required reverting the config file. Thus it was  
removed. Since it was removed the Encryptor is not utilizing a powerful tool  
granted by AES-GCM.   

### Password Management   

Passwords on private keys must be entered manually upon each request to decrypt  
the data. No password management integration currently exists to ensure  
passwords are only queried upon the first call. Password manager cli may be  
possible solution (albeit exploitable via side-channel attacks, and potentially  
extractable from local users). One possible tool to integrate may be 
[keepassXC-cli](<https://www.mankier.com/1/keepassxc-cli#>)  

### Decrypting or Acquiring Encrypted Data  

The current implementation of configuration encryption encrypts all or none of  
the target attributes. This means there is currently no functionality to query  
for the value of a single attribute. Since each attribute is encrypted  
individually with AES-GCM cipher the introduction of a query that decrypts  
returns and encrypts should be trivial, especially if password management is  
integrated.   

### Full File Encryption  

The CmsEncryptor is only encrypting data that could be held in memory. Thus  
full file encryption is currently not supported. This could be extended if the  
encryptor adds methods to process large quantities of bytes.   

### Matching More Cases than Intended with Cloudmesh.Security.Secrets Section    

By the definition of re the '.' symbol matches any single character.  
Under most practical circumstance this should match on a literal '.' character  
since all paths in the cloudmesh.yaml config are presented as dotpaths.  
Due to these design choices it is technically possible for the expressions   
to encrypt more values than intended.  

Example) regexp = '\.\*security\.secrets\.foo'  

Let us have the following dotpaths  
  * security.secrets.foo:bar  
  * security.secretsXfoo:baz    

Both bar and baz will be encrypted since the re '\.' can match on both the  
literal '\.' and the character 'X'. This should only bring minimal additional  
overhead on the occasion it occurs.   
 
## Work Breakdown  

### Week of Monday Nov. 25th  

1. Changed encoding of secrets from base64 to integers  
1. Added cloudmesh.security section in cloudmesh.yaml default config  
1. Added cloudmesh.security.secrets to use regexp to pick attributes for encryption  
1. Implemented file reversion in case encryption or decryption fails  
1. Created Pull Request for [cms-cloud](<https://github.com/cloudmesh/cloudmesh-cloud/pull/245>)  
1. Created Pull Request for [cms-common](<https://github.com/cloudmesh/cloudmesh-common/pull/10>)  
1. Created Pull Request for [cms-configuration](<https://github.com/cloudmesh/cloudmesh-configuration/pull/2>)  
1. Added couldmesh.security.exceptions to use regexp to deny encryption   

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
