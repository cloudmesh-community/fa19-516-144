# Encryption of Cloudmesh Config File Secrets

Andrew Holland 

* repo: [fa19-516-144](<https://github.com/cloudmesh-community/fa19-516-144/tree/master>)
* email: hollanaa@iu.edu

Project Contributions

* [Contributors](<https://github.com/cloudmesh-community/fa19-516-144/graphs/contributors>)
* [Github Repo Insights](<https://github.com/cloudmesh-community/fa19-516-144/pulse>)

Repositories Impacted

* [cloudmesh-cloud](<https://github.com/cloudmesh/cloudmesh-cloud>)
  - [key.py](<https://github.com/cloudmesh/cloudmesh-cloud/blob/master/cloudmesh/key/command/key.py>)
  - [config.py](<https://github.com/cloudmesh/cloudmesh-cloud/blob/master/cloudmesh/config/command/config.py>)
  - `encrypt.py`: [removed here](<https://github.com/cloudmesh/cloudmesh-cloud/pull/255/files#diff-3d9efa259b85a5065a3c53be738e9d81>)
  - `test_encryption.py`: [removed here](<https://github.com/cloudmesh/cloudmesh-cloud/pull/255/files#diff-3d9efa259b85a5065a3c53be738e9d81>)
  
* [cloudmesh-configuration](<https://github.com/cloudmesh/cloudmesh-configuration>)
  - [Config.py](<https://github.com/cloudmesh/cloudmesh-configuration/blob/master/cloudmesh/configuration/Config.py>)
  - [encrypt.py](<https://github.com/cloudmesh/cloudmesh-configuration/blob/master/cloudmesh/configuration/security/encrypt.py>)
  - [test_encryption.py](<https://github.com/cloudmesh/cloudmesh-configuration/blob/master/tests/test_encryption.py>)
  - [cloudmesh.yaml](<https://github.com/cloudmesh/cloudmesh-configuration/blob/master/cloudmesh/configuration/etc/cloudmesh.yaml>)

* [cloudmesh-common](<https://github.com/cloudmesh/cloudmesh-common>)
  - [util.py](<https://github.com/cloudmesh/cloudmesh-common/blob/master/cloudmesh/common/util.py>)

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

## Installation and Using Cloudmesh Config Encryption

The installation and process of encryption is described in detail
within [Cloudmesh Config File Encryption](<https://cloudmesh.github.io/cloudmesh-manual/configuration/encryption.html>)

## Implementation

### Cloudmesh.Security Section

The cloudmesh.security section was added to allow users to control encryption.
This section has five noteworthy attributes.

1. publickey: The path to the public key used to encrypt the attributes
1. privatekey: The path to the private key used to decrypt the attributes
This must be the private key-paired with the public key
1. secpath: This is the operating system path that will hold keys and nonces
1. secrets: A list of regular expressions to select which attributes to encrypt
1. exceptions: A list of regular expressions to **deny** encrypting attributes

### Cloudmesh Tools for Encryption

Cloudmesh now has several classes to handle the foundation of security. 
All tools are located within [encrypt.py](<https://github.com/cloudmesh/cloudmesh-configuration/blob/master/cloudmesh/configuration/security/encrypt.py>) 

#### CmsEncryptor

The CmsEncryptor class is a general encryptor tool used for both symmetric and
asymmetric encryption schemes. Currently RSA and AES-GCM encryption schemes
are the only available schemes for encryption. This is used to take bytes of
data and return the encrypted bytes with other data if necessary. This can 
also be used for full file encryption. Due however note that this particular
functionality has not been tested with arbitrarily large file sizes.

#### CmsHasher

The CmsHasher class is used for hashing techniques. Currently SHA256 and MD5
are supported. Note MD5 is an **insecure** hashing tool. It should only be
used when you are absolutely sure that the data being hashed does not need to
be kept secret. The default and recommended hashing tool is SHA256. The 
Hasher is used hash the attribute dot paths that are encrypted and use the 
hash as a base file name. MD5 is used in this instance since the security 
of the secrets does not rely on hiding the path of the attribute that was 
encrypted. 

#### KeyHandler

The KeyHandler class is responsible for generating, writing, loading, and 
verifying the encoding and format of a given key file. Some variety of keys 
and formats are supported. Currently, private keys can have PKCS8 or OpenSSL
format and Public keys can have SubjectInfo or OpenSSH formats. 
Both PEM and SSH encoding is supported. It can support both passwordless 
and password-protected private key files.

### Encrypting and Decrypting Cloudmesh Attributes

#### Internal Process for Encryption

1. Copy the contents of the config into a secure temporary file
   If at any time an error occurs the original config file is restored 
2. The cloudmesh.security.secpath value is queried from the config
3. Load the key whose path is referenced in cloudmesh.security.publickey
4. For each regular expression, apply it on all paths of the config file
5. For each applied path, get the value and hash the full path
6. Encrypt the value with CmsEncryptor using AES-GCM
7. Take the generated key, generated, nonce, and ciphertext
8. Encrypt the nonce and key with CmsEncryptor using RSA
9. Store an integer encoding of the ciphertext in the cloudmesh config
10. Store the encrypted key and nonce in separate files with hashed base name
11. Delete the temporary file

#### Internal Process for Decryption

1. Copy the contents of the config into a secure temporary file
   If at any time an error occurs the original config file is restored 
2. Query the config for the value of cloudmesh.security.secpath
3. Load the key whose path is referenced in cloudmesh.security.privatekey
4. For each regular expression, apply it on all paths of the config file
5. For each applied path produce the hash and load the nonce and key
6. Decrypt the nonce and key with CmsEncryptor using RSA
7. Get the ciphertext from the config down the full path
8. Decrypt the ciphertext using the key, and nonce
9. Set the path attribute with the plaintext
10. Delete the files with hash as base name in the secpath directory
11. Delete the temporary file

#### Key Management

#### Keys Used in Encryption

There are two keys used for encryption and decryption. The symmetric key which
is an AES-256 key that is automatically generated by CmsEncryptor and the
private-public RSA key pair generated by the user. 

The RSA key should be in PEM format, with 2048 bits. This key could be
generated by using the ```cms key gen pem``` command. 

Since symmetric keys require more computation to crack than asymmetric keys
we encrypt the actual data with the AES-GCM cipher. This will produce the 
ciphertext (which is stored in cloudmesh.yaml), a nonce (one time random 
data), and an AES key that was used to encrypt the data. 

The nonce and key are encrypted with the user's RSA public key located at the
full file path listed within the `cloudmesh.security.publickey` attribute. 
Technically, the nonce need not be kept secret, but minimal computational
effort is lost by encrypting the data. The encrypted nonce and key are 
stored within the `cloudmesh.security.secpath` directory. This is why the 
```cloudmesh config secinit``` command was required during configuration.
The secinit command ensured the directory was created. 

#### Key Generation

Cloudmesh can generate keys using the ``cms key gen`` command. This command is
integrated with the KeyHandler class. This command can generate PEM and OpenSSH
encoded public or private RSA key. 

#### Verify Key Structure and Password

Cloudmesh can verify if a key is password protected and if a key has proper 
PEM or SSH encoding. This is executed with the ``cms key gen verify`` command.
The first check is to verify if the key is password protected. The encoding 
cannot be verified without obtaining the password to decrypt the key. If the
encoding is to be checked the ``--check_pass`` argument should be utilized.

#### Reformatting a Keys Structure and Password

Cloudmesh can reformat PEM or SSH encoded keys between each other by using the
``cloudmesh key reformat command``. This command can be useful to retain the
original value of a key but to change the formatting for key purposes.

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

There are several password managements tools that have been developed over the
last decade but not all are useful for cloudmesh. kpcli and kedpm are two 
historical password manager, but they lack modern development. Keepass2-cli 
has more active development but lacks some of the intuitive command line features
that keepassXC-cli has. the gopass password manager seems useful for the intended
purposes of cloudmesh, but it is still in early development.

### Referencing Encrypted Data

The current implementation of configuration encryption is intended to secure 
at-rest configuration secrets. This means all of the attributes are encrypted
or none of them are. This limits the practicality of utilizing the encrypt and 
decrypt commands. 

To make config encryption more useful some functionality to query encrypted data
should be introduced. This extension should not require extensive effort since 
the keys are stored and gathered in a general manner. 

One approach may be to decrypt the config within the users shell instance and 
store the private key in memory. Whenever an encrypted value is queried you 
could decrypt it, return the value, then re-encrypt the value. 

This approach should be taken with care to not expose the key contents. 
This would also mean the key could be extracted from side-channel attacks. 

Another approach would be to have some password manager store the keys. 
When a session is started have them use the password to the password db. 
Then when a value is requested, query the db for the cipher value, 
decrypt the value and return it. This has the benefit of not requiring 
re-encryption, but is vulnerable to side-channel attacks **and** requires
extensive thought on how an attacker could acquire the keys. 

### Encrypting Arbitrarily Large Files

The EncryptFile class was replaced by the `CmsEncryptor` and `KeyHandler` 
classes. The `CmsEncryptor.encrypt_file()` function is responsible for 
encrypting the contents of any given file path. This function has
undergone testing files but not with large file sizes. Namely it has 
not tested file sizes that are larger than the machines memory limits. 
To ensure the functionality is correct file sizes of 50GB+ should be 
encrypted and decrypted to ensure that data is not lost or unencrypted.

### Matching More Cases than Intended with Cloudmesh.Security.Secrets Section

By the definition of python re the `.` symbol matches any single character.
Under most practical circumstance this should match on a literal `.` character
since all paths in the cloudmesh.yaml config are presented as dotpaths.
Due to these design choices it is technically possible for the expressions 
to encrypt more values than intended.

Example) regexp = ```.*security.secrets.foo```

Let us have the following dotpaths

```
security.secrets.foo:bar
security.secretsXfoo:baz
```

Both bar and baz will be encrypted since the re `.` can match on both the
literal `.` and the character `X`. This should only bring minimal additional
overhead on the occasion it occur. This could be corrected by defining more
specific syntax when adding secrets and exceptions or by checking if the
given expression for ```cms config security add ...``` is regexp at all.
 
## References

### Password Managers

1. [kpcli](<http://kpcli.sourceforge.net/>)
2. [gopass](<https://www.gopass.pw/>)
3. [kedpm](<http://kedpm.sourceforge.net/>)
4. [keepass2 cli](<https://keepass.info/help/base/cmdline.html>)

## Acknowledgments

Gregor von Laszewsk, for assistance in writing the config encryption page
