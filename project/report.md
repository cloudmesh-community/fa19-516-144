# Encryption of Cloud Secrets

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

## Process

The cloudmesh.yaml configuration file stores passwords and other secrets to
simplify accessing machines. By default **none** of the passwords are
encrypted. Encryption allows you to store your secrets within the file and
prevents the accidental exposure of your secrets (if you edit your config while
sharing a screen) and makes it harder for malicious users to steal your
passwords. This is all done through the ```cms config encrypt``` and
```cms config decrypt``` commands. 

### Installation

You must be sure that cloudmesh is installed. The easiest way to install
cloudmseh is via pip. However, it is not yet released with the security extensions
we discuss below. If you would like to use them you need to install
cloudmesh-cloud from source. Which is discussed in the 
[cloudmesh manual](<https://cloudmesh.github.io/cloudmesh-manual/installation/install.html>)
To remind you how easy it is you can use the following steps.

```bash
$ mkdir cm 
$ cd cm
$ pip install cloudmesh-installer
$ cloudmesh-installer git clone cloud 
$ cloudmesh-installer install cloud
$ cms help
```

Please remember that after this you will have to configure your `~/.cloudmesh/cloudmesh.yaml`

After the system has been installed cloudmesh will need to initilaze its
security capabilities. If you wish to control where it is initialized reference the 
[Additional Configuration Options](#aco) section below. Otherwise, initialize the
configuration capabilites by running the the following. 

```bash
$ cms config secinit
```

Now that we have the proper system related properties initalized we need an RSA
public-private key pair to execute encryption and decryption of the data.
The public key is used to encrypt data and the private key is used to decrypt.
If you have previously generated an RSA key pair please reference the
[Additional Configuration Options](#aco) section below. Otherwise run the following.

```bash
$ cms key gen pem --set_path
```

Now that we have the initialized system and RSA key pair we can encrypt the config. 

### Encrypting the Config File

The configuration file can be encrypted by running the following command.
By default the encryption command will encrypt everything within the
cloudmesh.yaml file that is not necessary for decryption. 
To edit which attributes are encrypted or excluded from encryption reference
the [Additional Configuration Options](#aco) section below. 

```bash
$ cms config encrypt
```

After this command is completed all of the explicitly defined secrets are
encrypted at rest. This means that even if the data is exposed the data should
be secured by typical definitions of security. This also means that any other
cloudmesh command that references an encrypted attribute will return an
encrypted value. Thus, care should be taken to not call commands that require
encrypted attributes. To reference the original values you must decrypt the
config file. 

### Decrypting the Config File

The configuration file can be decrypted by running the following command. 

```bash
$ cms config decrypt
```

If the private key was password protected you must enter the password when
prompted. If the key has no password either hit enter immediately after being
prompted or run the following. 

```bash
$ cms config decrypt --nopass
```

### Additional Configuration Options<a name="aco"></a>

#### Changing the secinit Directory

The secinit directory controls where encryption related data is stored. The
default location is ~/.cloudmesh/security. If you wish to change this location
you must edit the `cloudmesh.security.secpath` attribute. For example, if you
wish that cloudmesh secrets are stored within `~/.cloudmesh/.foosec` run the following

```bash
$ cms config set cloudmesh.security.secpath=~/.cloudmesh/.foosec
$ cms config secinit
```

#### CMS Key Gen Options 

##### Changing Key Names 

The `cms key gen` command will automatically generate the key pair into the default
locations of `~/.ssh/id_rsa` and `~/.ssh/id_rsa.pub`. If this key already exists or
if you prefer a different location use the --filename=FILENAME flag. Where FILENAME is
the full path to the key you would like to generate. For example, if we would
like to have a keys called `cms` and `cms.pub` in the .ssh directory execute

```bash
$ cms key gen pem --filename=~/.ssh/cms
```

##### Setting Keys for Encryption Without Key Gen Command

The path to the encryption and decryption keys are located in
`cloudmesh.security.pubickey` and `cloudmesh.security.privatekey` respectively.
When keys are generated with the `--set_path` argument they set these attributes 
after the keys are generated. 

If you already have RSA keys that are PEM encoded you can set the path directly.
For instance let us assume we already had `~/.ssh/priv/cms` and its public key
pair `~/.ssh/pub/cms.pub`

```bash
$ cms config set cloudmesh.security.privatekey=~/.ssh/priv/cms
$ cms config set cloudmesh.security.publickey=~/.ssh/pub/cms.pub
```

Note: the keys can be located anywhere since they are looked up before encryption.

##### Generating a Key Without a Password

Passwords for your RSA private key are recommended. It is much easier to 
**lose all security gurantees** if you private key is not encrypted.
Unless you have a good reason, keep a password on your private file. 
If you understand this and still wish to generate a key without a password run

```bash
$ cms key gen pem --nopass
```

#### Selecting Attributes to Encrypt

Internally, Cloudmesh represents all attributes as the yaml dot path to the
attribute. The `cloudmesh.security.secrets` attribute takes a list of python
regular expressions that will be matched on the dot paths to the attributes.

To learn the specifics about python regular expression please reference the 
[python re documentation](<https://docs.python.org/3.7/library/re.html>)

By default, the secrets section has `.*` which encrypts everything

If you wish to encrypt all `AZURE_SECRET_KEY` attributes you can execute

```bash
$ cms config security add --secrets=.*AZURE_SECRET_KEY
```

If you wish to encrypt a specific attribute you can provide the dot path.
For instance, to encrypt the mongo database `MONGO_PASSWORD`

```bash
$ cms config security add --secrets=cloudmesh.data.mongo.MONGO_PASSWORD
```

If you wish to remove any regular expressions from secrets run the following.

```bash
$ cms config security rmv --secrets=cloudmesh.data.mongo.MONGO_PASSWORD
```

#### Selecting Attributes to Exclude from Encryption

The `cloudmesh.security.exceptions` section is intended to list attributes that
must **not** be encrypted. This section also explicitly uses python regular
expressions to capture the attribute dot paths. The default exceptions
included in the exceptions section are necessary for the decryption of data.

Note that the exceptions section has priority over the secrets section. If
there is ever an attribute that is matched on both secrets and exceptions
regular expressions the attribute will **not** be encrypted.

For instance, if you wish to ensure that none of the `AZURE_SECRET_KEY`
attributes are encrypted run the following. 

```bash
$ cms config security add --exceptions=.*AZURE_SECRET_KEY
```

If you wish to exclude a specific attribute give the dot path.

```bash
$ cms config security add --exceptions=cloudmesh.data.mongo.MONGO_PASSWORD
```

If you wish to remove any regular expressions within the exceptions section run
the ```cms config security rmv``` command. For instance to remove the example
exceptions. 

```bash
$ cms config security rmv --exceptions=.*AZURE_SECRET_KEY
$ cms config security rmv --exceptions=cloudmesh.data.mongo.MONGO_PASSWORD
```

## Implementation

### Cloudmesh.Security Section

The cloudmesh.security section was added to allow users to control encryption.
In the current implementation the security section has five noteworthy attributes.

1. publickey: The path to the public key used to encrypt the attributes
1. privatekey: The path to the private key used to decrypt the attributes
This must be the private key-paired with the public key
1. secpath: This is the operating system path that will hold keys and nonces
1. secrets: A list of regular expressions to select which attributes to encrypt
1. exceptions: A list of regular expressions to select attribute to **not** encrypt

### Cloudmesh Tools for Encryption

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

#### KeyLoader

The KeyLoader class is responsible for generating, writing, loading, and 
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
10. Store the encrypted key and nonce in separate files with the hash as base name
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

Since symmetric keys require more computation to crack than assymmetric keys
we encrypt the actual data with the AES-GCM cipher. This will produce the 
ciphertext (which is stored in cloudmesh.yaml), a nonce (one time random 
data), and an AES key that was used to encrypt the data. 

The nonce and key are encrypted with the users RSA key pair located at the 
path listed within the `cloudmesh.security.publickey` attribute. 
Technically, the nonce need not be kept secret, but minimal computational
effort is lost by encrypting the data. The encrypted nonce and key are 
stored within the `cloudmesh.security.secpath` directory. This is why the 
```cloudmesh config secinit``` command was required during configuration.
The secinit command ensured the directory was created. 

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
that keepassXC-cli has. the gopass password manager seems useful for the inteded
purposes of cloudmesh, but it is still in early development. 

### Referencing Encrypted Data

The current implementation of configuration encryption is intended to secure 
the configuration secrets at rest. This means all of the attributes are encrypted
or none of them are. This limits the practicality of utilizing the encrypt and 
decrypt commands. 

To make config encryption more useful some functionality to query encrypted data
should be introduced. This extension should not require extensive effort since 
the keys are stored and gathered in a general manner. 

One appoarch may be to decrypt the config within the users shell instance and 
store the private key in memory. Whenever an encrypted value is quired you 
could decrypt it, return the value, then re-encrypt the value. 

This apporoach should be taken with care to not expose the key contents. 
This would also mean the key could be extracted from side-channel attacks. 

Another apporach would be to have some password manager store the keys. 
When a session is started have them use the password to the password db. 
Then when a value is requested, query the db for the cipher value, 
decrypt the value and return it. This has the benefit of not requiring 
re-encryption, but is vulnerable to side-channel attacks **and** requires
extensive thought on how an attacker could acquire the keys. 

### Replacing the EncryptFile class

The EncryptFile class can be replaced by the combination of CmsEncryptor,
CmsHasher, and KeyHandler classes. The KeyHandler class generates and 
verifies the integrity of keys. The CmsEncryptor has an implementation of 
full file encryption. Namely the `CmsEncryptor.encrypt_file()` function. 
This function has not been tested with arbitrarily large files. 

Provided testing has been conducted, all references to the EncryptFile should
be replaced by the relevant CmsEncryptor, CmsHasher, or KeyHandler functions.

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
 
## Refernces

### Password Managers

1. [kpcli](<http://kpcli.sourceforge.net/>)
2. [gopass](<https://www.gopass.pw/>)
3. [kedpm](<http://kedpm.sourceforge.net/>)
4. [keepass2 cli](<https://keepass.info/help/base/cmdline.html>)

