# SSH Agent Demonstration  

## Purpose   

These shell scripts are used to demonstrate the capabilities of ssh-agent.  

## Hypothesis  
ssh-agent cannot be used to access the bytes of the private key  

## Overview  

encrypt data with an ssh-key that will be added to the agent  

## Scripts

1. demo-sshkeygen.sh: generates an ssh-key  
1. demo-decrypt.sh: attempts to decrypt the data.enc file with the key  
1. demo-encrypt.sh: encrypts the data file and outputs data.enc  
1. demo-keyadd.sh: adds the generated private key to the agent  
1. cleanup.sh: removes the test directory and its contents  
1. config.sh: has variable data referenced by other shell scripts  

## Process  

1. Verify data within config.sh is consistent with environment  
1. ``` ./demo-sshkeygen.sh ```  
1. ``` ./demo-encrypt.sh ```  
1. Either manually add key to agent or run ``` ./demo-keyadd ```  
1. Verify the key was added by running ``` ssh-add -l ```  
1. ``` ./demo-decrypt.sh ```  
	1. If the system prompts for a password, Fail  

## Justification

The ssh-agent can be used to verify signatures without exposing the private  
bytes. The agent does not expose the private bytes and cannot be queried for  
them. Since the openssl cannot use the key bytes (even after they are added to  
the agent) we have a practical example of the agent not providing bytes.   


