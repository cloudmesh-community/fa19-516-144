# Open Notes About Project

## Gregor's Wish List of Tasks

1. Audit files using openssl  
	1. Audit cloudmesh-cloud/cloudmesh/management/configuration/security/encryption.py-bug  
	1. Audit /cloudmesh-cloud/cloudmesh/security/encryption/encrypt.py-bug  
	1. look at path-expand  
	1. use string format instead of \*\*data  
	1. combine with cms/sec/enc/encrypt.py if necessary
1. Audit Encryption and Decryption functions
	1. Implement verification function for enc and dec functions
	1. Use ssh-agent to access the keys for encryption and decryption  
1. Audit init file 
	1. Inspect line 89
1. Implement ```cms key add NAME --source=FILENAME```  
1. Implement --dry-run on cms key  
1. Implement all of the ```csm key group``` commands  
	1. Add new mongo groups similar to 'secgroup' and 'secrules'  
	1. Define group members, name, and policies  
	1. Design way for keys to be distributed (or verified in such a manner)  
1. Add Security Group management for Azure  


## Open Questions for Configuration

1. Will the file have full encryption or inline byte encryption?
	1. If full, will you store the ecc key?
	2. If inline, how will partition lines whilst preserving yaml format?
2. Is there a password manager that can be easily integrated by command line?

