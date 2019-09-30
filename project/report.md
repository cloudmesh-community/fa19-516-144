# Introduce Encryption Functionality for Cloudmesh Configuration File

## Group Members

- Nayeem (nayeemullahbaig.93@gmail.com)  
- Andrew Holland (hollanaa@iu.edu)  

## Introduction

Increase the security capabilities of Cloudmesh be encrypting the cloudmesh.yaml  
file. Currently the configuration file is left in plaintext thus leaving  
passwords to chameleon cloud and mongodb vulnerable to any malicious user that  
gains access to the machine the file is hosted on. Encrypting the config file  
decreases the attack surface.   

This project will also attempt to integrate capabilities to manage the  
passwords within a password manager such as Keepass. If successful Cloudmesh  
can automate the generation, storage, and access of the keys and config.  

## Planned Implementation

### Goal 1: Encryption of Yaml File

1. Add location: "PATH\_TO\_FILE" section in first line
2. Add cloudmesh: configs below
3. Write python script to encrypt using AES-GCM with ECC key

### Goal 2: Integrate File into Keepass

1. Investigate using Keepass or other password manager's command line interfaces
2. Create script to take the location information, follow it and decrypt config

### Goal 3: Add Integrity Checks for Config File

1. Simplify library calls for encryption and decryption of config file
2. Modify encryption to use location within integrity check
3. Add library calls to modify location

### Goal 4: Update All Cloudmesh commands that access Config File

1. Update all Cloudmesh manipulations of config file to use new library

### Goal 5: Harden access to SSH

1. Add pam\_ssh capabilities to control access to ssh-add


## Proposed Software to Integrate into Project

* Keepass(2)  
* python module: python cryptography  
* ssh-keygen  

## Related Concepts

* Elliptic Curve Cryptography  
* Advanced Encryption Standard Galois Counter Mode (AES-GCM)

## Workbreakdown

[Github Repo Insights](<https://github.com/cloudmesh-community/fa19-516-144/pulse>)  

## Progress

### Week of Monday Sep. 30th 

#### Andrew

1. Researched password managers for future integration discovered  
	1. [kpcli](<http://kpcli.sourceforge.net/>)  
	2. [gopass](<https://www.gopass.pw/>)  
	3. [kedpm](<http://kedpm.sourceforge.net/>)  
	4. [keepass2 cli](<https://keepass.info/help/base/cmdline.html>)  

## References

