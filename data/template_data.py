#!/usr/bin/env python

# lists used by generate_dataset.py to create large data set

# data is fictitious 
# any connection to actual people is purly coincidental
# no quality engineers were injured in the writing of this code

user_groups = ["admin", "development", "test", "production"]

user_fname = ["John", "Paul", "George", "Ringo", "Aaron", "James", "Eric", 
              "Mary", "Linda", "Elizabeth", "Susan", "Nancy", "Mom"]

user_lname = ["Smith", "Johnson", "Williams", "Jones", "Brown", 
              "David", "Miller", "Wilson", "Moore", "Anderson",
              "Jackson", "White", "Robinson", "King", "Lopez"]

email_domains = ["redhat.com", "apache.org", "mozilla.org", "mit.edu"]

provider_roles = ["Provider User", "Provider Administer"]

user_roles = ["Global Deployable Administrator", 
    "Global Administrator", 
    "Global Pool User", 
    "Global Realm Administrator", 
    "Global HWP User", 
    "Global HWP Administrator", 
    "Global Image Administrator", 
    "Global Pool Administrator", 
    "Global Provider Administrator", 
    "Global Provider User"]

providers = ["ec2", "rhevm", "vsphere"]

provider_accounts = ["rhevm", 
    "vsphere",
    "ec2-ap-northeast-1",
    "ec2-ap-southeast-1",
    "ec2-eu-west-1",
    "ec2-sa-east-1",
    "ec2-sa-east-1",
    "ec2-us-west-1",
    "ec2-us-west-2"]

environments = ["dev", "test", "stage", "production"]

pools = ["IT", "web services", "engineering tools", "operations"]

catalogs = ["IT", "web services", "engineering tools", "operations"]

hardware_prof = ["small-x86_64", "medium-x86_64", "large-x86_64"]

deployables = ["Wordpress", "SAP", "Mail Server", "DNS Server", "CloudEngine", "SystemEngine"]

images = ["https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-x86_64-6Server-cf-tools.xml", 
          "https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-x86_64-5Server-cf-tools.xml",
          "https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-i386-5Server-cf-tools.xml"]


