# Project Proposal: Cloudmesh Secret

## Goals

This project will introduce functionality to interface with cloud Key  
Management Services (KMS).   

### Goal 1: OpenStack Key Management

Introduce API calls to OpenStack [barbican 8.1.0 Secrets API](<https://docs.openstack.org/api-guide/key-manager/index.html>).  
Including secrets creation, retrieval, updates, and deletion.  


### Goal 2: AWS Key Management

Introduce API calls to AWS [Secrets Manager](<https://aws.amazon.com/secrets-manager/>)  
Including secrets creation, retrieval, updates, and deletien.  


### Goal 3: Access Control

Introduce API calls for implementing OpenStack ACL and AWS Resource Policy.  

## Benchmarks

Benchmarks will include anlysis of cost of service, and performance.

## List of Possible Providers

* Openstack - [Secrets API](<https://docs.openstack.org/api-guide/key-manager/index.html>)  
* Amazon Web Services - [KMS](<https://aws.amazon.com/kms/>) or [Secrets Manager](<https://aws.amazon.com/secrets-manager/>)  
* Google Cloud Platform - [KMS](<https://cloud.google.com/kms/docs/>) or [Cloud HSM](<https://cloud.google.com/kms/docs/hsm>)  
* Azure - [Key Vault](<https://docs.microsoft.com/en-us/azure/key-vault/>)  

## Related Technology

* Kubernetes - [Secrets](<https://kubernetes.io/docs/concepts/configuration/secret/>)  
* Hashicorp - [Vault](<https://www.vaultproject.io/docs/secrets/>)  

## Possible Extensions

* Deploying standalone secrets service on top of Kubernetes.
