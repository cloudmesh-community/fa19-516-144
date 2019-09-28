# Class Exercise for 09/27/19

## Q1: What is the import statement for config = Config

from cloudmesh.configuration.Config import Config  

## Q2: How do I print the config var?

Within the python script you could use  
1. Cloudmesh's VERBOSE package
1. Python's print function
1. Import prettyprint and use the pprint function

## Q3: What cldoumesh cms command exists to list the config?

cms config cat [less]  
cms config cat displays the entire config file.  
cms config cat less displays the file without revealing passwords. 

## Q4: Can you edit the cloudmesh config file while on Zoom?

Technically yes, however, you will most likely expose your passwords. If this  
is the case it is your responsiblitity to replace the passwords to you account.  
If necessary to display the config file on zoom execute cms config cat less.  
