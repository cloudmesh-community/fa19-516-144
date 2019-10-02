# fa19-516-144

## Week 5

- [] audit /cms-cloud/cms/managment/config/security/encrypt.py-bug
- [] audit /cms-cloud/cms/security/encrypt.py-bug

## Week 4

- [X] Installed mongodb through cms admin
- [X] verified name.yaml file is of correct format
- [X] Created chameleon-success.md
- [X] Exercise 1  
- [] Exercise 2  (Gregor stated I can skip this due to my submitted PR)
- [] Exercise 3  (Gregor stated I can skip this due to my submitted PR)
- [X] Submitted pull request to support cms admin mongo install on debian

## Week 3

- [X] Correct Datacenter.md  
- [X] Read "Architectures" chapter  
- [X] Read "Cloudmesh" chapter  
- [X] E.Cloudmesh.Common.1  
- [X] E.Cloudmesh.Common.2  
- [X] E.Cloudmesh.Common.3  
- [X] E.Cloudmesh.Common.4  
- [X] E.Cloudmesh.Common.5  
- [X] E.Cloudmesh.Shell.1  
- [X] E.Cloudmesh.Shell.2  
- [X] E.Cloudmesh.Shell.3  
- [X] installed mongodb version 3.2.11  
- [X] Investigate Cloud Secrets Managers  
- [X] Investigate Authentication Methodologies  
- [X] Create and update project/report.md with project proposal  

## Week 2

- [X] Read Chapter 4: Data Center  
- [X] Exercise: 2.a  
- [X] Exercise: 2.b  
- [X] Exercise: 3  
- [X] Exercise: 4  
- [X] Exercise: 5  
- [X] Exercise: 8  

## Week 1

- [x] Posted Professional Bio  
- [X] Setup Computer  
- [X] Created cloud accounts  
- [X] Filled out 'Cloud Accounts' form  
- [X] Installed Pyenv with 3.7.4 as default  
- [X] Updated Pip  
- [X] installed ePub Reade (Calibre)  

## Environment Installations

### Python

1. sudo apt-get install python virtualenv pyenv  
1. pyenv install 3.7.4  
1. pyenv global 3.7.4  
1. pyenv virtualenv ENV3  
1. pyenv activate ENV3  
1. ...  
1. pyenv ENV3 deactivate  


### Cloudmesh Cloud

1. pyenv activate ENV3  
1. mkdir cm  
1. cd cm  
1. pip install cloudmesh-installer  
1. cloudmesh-installer git clone cms  
1. cloudmesh-installer install cms -e  
1. cloudmesh-installer install cloud -e   

### MongoDB

1. cloudmesh-installer git pull cloud
2. cloudmesh-installer install cloud -e
3. Edited cloudmesh.yaml to include passwords and profile information
4. cms help
5. cms init
