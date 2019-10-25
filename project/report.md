# General Security Improvements and Introducing Key Managment for Cloudmesh  

## Group Members

- 172: Nayeem (nayeemullahbaig.93@gmail.com)  
- 144: Andrew Holland (hollanaa@iu.edu)  

## Introduction

The Cloudmesh project lacks certain security capabilities and secure coding  
practices. General improvements are required to address three primary concerns.  

First, the code base requireds a general audit on all files using openssl.  
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

Finally, the management of keys need to be automated and integrated with mongoDB.  
Cloudmesh is missing functionality to easily add keys and control the access  
policies related to key management. Functionality to utilize mongo DB have  
already been developed for the Security Rules and Security Groups functions.  
We can add Key Groups that are defined by both the related cloud provider and  
collection of related keys to fine tune access control for all connected machines.   

After addressing the primary concerns Cloudmesh will be capable of being  
further extended to integrate password managers directly into secrets  
management. This could include software such as Keepass. If successful,  
Cloudmesh can automate the generation, storage, and access of the keys and config.  

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

Task Lead: Andrew  
Status: In Progress 

Last Update: Audited cloudmesh-cloud/cloudmesh/security/encrypt.py  

### Encrypting Cloudmesh.yaml Secrets  

Task Lead: Andrew    
Status: Pending 

Last Update:   

### CMS Key Command

Task Lead: Nayeem    
Status: In Progress   

Last Update: Implemented ``` cms key add --source=FILE_PATH ```

### CMS KeyGroup Command

Task Lead: Nayeem   
Status: In Progress   

Last Update: Added KeyGroup.py file based on SecGroup.py   

## Workbreakdown

[Github Repo Insights](<https://github.com/cloudmesh-community/fa19-516-144/pulse>)  

## Progress

### Week of Monday Oct. 14th

#### Andrew

1. Created the KeyGroup.py file to handle key groups  
    1. Need to investigate the purpose of SecGroup.output  
1. Designed queries

### Week of Monday Oct. 07th

#### Andrew

1. Forked cloudmesh-cloud to local repo  
    1. fork located [here](<https://github.com/ElectricErudite/cloudmesh-cloud>)  
1. Edited cms key --source=FILEPATH to now parse filepath argument  
    1. Within [key-group branch](<https://github.com/ElectricErudite/cloudmesh-cloud/tree/key-group>)  
1. Investigating how to add new local-keygroup collection to database  
1. Installed robo3t to observe changes to local mongodb  

### Week of Monday Sep. 30th 

#### Andrew

1. Researched password managers for future integration discovered  
	1. [kpcli](<http://kpcli.sourceforge.net/>)  
	2. [gopass](<https://www.gopass.pw/>)  
	3. [kedpm](<http://kedpm.sourceforge.net/>)  
	4. [keepass2 cli](<https://keepass.info/help/base/cmdline.html>)  
1. Submitted PR for debian 9 installation of mongo  
1. Installed docker on local system to ease testing
1. Began audit of cms-cloud/cms/security/encrypt.py-bug check /project/audit.md
1. Took second pass look through the encrypt.py-bug. Wrote questions for Gregor  

