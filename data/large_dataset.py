#!/usr/bin/env python

# generated from generate_dataset.py
# based on list definitions in raw_data.py

        

###
# Users and groups
###

user_groups = [
    {"name" : "admin", 
    "description" : "This is the admin group."},
    {"name" : "development", 
    "description" : "This is the development group."},
    {"name" : "test", 
    "description" : "This is the test group."},
    {"name" : "production", 
    "description" : "This is the production group."}]

users = [
    {"fname" : "Eric",
    "lname" : "Smith",
    "email" : "eric.smith@mozilla.org",
    "username" : "esmith",
    "passwd" : "31TRjyt7;tJ1",
    "max_instances" : "4",
    "user_groups" : ['development', 'production', 'admin'] },
    {"fname" : "Linda",
    "lname" : "Johnson",
    "email" : "linda.johnson@mozilla.org",
    "username" : "ljohnson",
    "passwd" : "gE`.eJ;yb2S9Ui",
    "max_instances" : "10",
    "user_groups" : ['production', 'admin', 'development'] },
    {"fname" : "Ringo",
    "lname" : "Williams",
    "email" : "ringo.williams@mozilla.org",
    "username" : "rwilliams",
    "passwd" : "aYi^9D@%AVk0",
    "max_instances" : "7",
    "user_groups" : ['test'] },
    {"fname" : "Linda",
    "lname" : "Jones",
    "email" : "linda.jones@apache.org",
    "username" : "ljones",
    "passwd" : "x;>1Szal5",
    "max_instances" : "9",
    "user_groups" : ['development', 'test'] },
    {"fname" : "Aaron",
    "lname" : "Brown",
    "email" : "aaron.brown@apache.org",
    "username" : "abrown",
    "passwd" : "i*s`0O72n4Ets8x",
    "max_instances" : "5",
    "user_groups" : ['production'] },
    {"fname" : "George",
    "lname" : "David",
    "email" : "george.david@redhat.com",
    "username" : "gdavid",
    "passwd" : "RZXXXAU88l",
    "max_instances" : "6",
    "user_groups" : ['development'] },
    {"fname" : "Eric",
    "lname" : "Miller",
    "email" : "eric.miller@apache.org",
    "username" : "emiller",
    "passwd" : "diDLtPV!babTkmofGB",
    "max_instances" : "10",
    "user_groups" : ['development', 'production', 'test'] },
    {"fname" : "Ringo",
    "lname" : "Wilson",
    "email" : "ringo.wilson@apache.org",
    "username" : "rwilson",
    "passwd" : ";hm^Q,VoOHk",
    "max_instances" : "9",
    "user_groups" : ['admin', 'test', 'development'] },
    {"fname" : "Mary",
    "lname" : "Moore",
    "email" : "mary.moore@apache.org",
    "username" : "mmoore",
    "passwd" : "6Q2J`$URz",
    "max_instances" : "4",
    "user_groups" : ['production', 'test'] },
    {"fname" : "Paul",
    "lname" : "Anderson",
    "email" : "paul.anderson@apache.org",
    "username" : "panderson",
    "passwd" : "^X;eCAV05$|n98cBPvO!",
    "max_instances" : "6",
    "user_groups" : ['production', 'test', 'development'] },
    {"fname" : "Mary",
    "lname" : "Jackson",
    "email" : "mary.jackson@mozilla.org",
    "username" : "mjackson",
    "passwd" : "Oz(D<88,w)KjZL,i~T`",
    "max_instances" : "3",
    "user_groups" : ['development', 'test', 'admin'] },
    {"fname" : "Paul",
    "lname" : "White",
    "email" : "paul.white@mozilla.org",
    "username" : "pwhite",
    "passwd" : "BliE|k0",
    "max_instances" : "8",
    "user_groups" : ['production'] },
    {"fname" : "Mom",
    "lname" : "Robinson",
    "email" : "mom.robinson@redhat.com",
    "username" : "mrobinson",
    "passwd" : "XKPez",
    "max_instances" : "5",
    "user_groups" : ['production', 'development', 'test'] },
    {"fname" : "Linda",
    "lname" : "King",
    "email" : "linda.king@mozilla.org",
    "username" : "lking",
    "passwd" : "d;J|1Hi^wNI2ardmJJ",
    "max_instances" : "2",
    "user_groups" : ['production', 'test', 'development'] },
    {"fname" : "George",
    "lname" : "Lopez",
    "email" : "george.lopez@mozilla.org",
    "username" : "glopez",
    "passwd" : "`d3!,St",
    "max_instances" : "10",
    "user_groups" : ['development', 'production', 'test'] }]


###
# Provider Accounts
#
# provider_name string must match conductor
# valid account types: "ec2", "rhevm", "vsphere"
# support for Rackspace and Openstack?
###

accounts = [
    {"type" : "ec2",
    "provider_name" : "ec2-us-east-1",
    "provider_account_name" : "Public cloud east",
    "username_access_key" : "",
    "password_secret_access_key" : "",
    "account_number" : "",
    "key_file" : "",
    "key_cert_file" : "",
    "provider_account_priority" : "",
    "provider_account_quota" : "" },

    {"type" : "rhevm",
    "provider_name" : "rhevm-default",
    "provider_account_name" : "rhevm",
    "username_access_key" : "admin@internal",
    "password_secret_access_key" : "dog8code",
    "provider_account_priority" : "",
    "provider_account_quota" : "" },

    {"type" : "vsphere",
    "provider_name" : "vsphere-default",
    "provider_account_name" : "vsphere",
    "username_access_key" : "Administrator",
    "password_secret_access_key" : "R3dhat!",
    "provider_account_priority" : "",
    "provider_account_quota" : "" }]

###
# Environments
###

pool_family_environments = [
    {"name" : "dev",
    "max_running_instances" : "1",
    "enabled_provider_accounts" : ['ec2-us-west-2', 'vsphere', 'ec2-sa-east-1', 'rhevm']},
    {"name" : "test",
    "max_running_instances" : "7",
    "enabled_provider_accounts" : ['ec2-us-west-1', 'vsphere', 'ec2-ap-southeast-1']},
    {"name" : "stage",
    "max_running_instances" : "5",
    "enabled_provider_accounts" : ['ec2-sa-east-1', 'rhevm', 'ec2-us-west-2', 'ec2-ap-northeast-1', 'ec2-ap-southeast-1', 'ec2-sa-east-1', 'vsphere', 'ec2-us-west-1']},
    {"name" : "production",
    "max_running_instances" : "2",
    "enabled_provider_accounts" : ['ec2-sa-east-1']}]

pools = [
    {"name" : "IT",
    "environment_parent" : ['test', 'dev', 'production'],
    "quota" : "11",
    "enabled" : True},
    {"name" : "web services",
    "environment_parent" : ['dev', 'test', 'stage'],
    "quota" : "8",
    "enabled" : True},
    {"name" : "engineering tools",
    "environment_parent" : ['test'],
    "quota" : "5",
    "enabled" : True},
    {"name" : "operations",
    "environment_parent" : ['production', 'dev'],
    "quota" : "9",
    "enabled" : True}]


###
# Content
###

catalogs = [
    {"name" : IT,
    "pool_parent" : ['web services', 'operations']},
    {"name" : web services,
    "pool_parent" : ['web services', 'operations']},
    {"name" : engineering tools,
    "pool_parent" : ['operations', 'web services']},
    {"name" : operations,
    "pool_parent" : ['operations', 'IT', 'engineering tools']}]

images_from_url = [
    {"name" : "rhel6-x86_64",
    "template_url" : "https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-x86_64-6Server-cf-tools.xml"},

    {"name" : "rhel5-x86_64",
    "template_url" : "https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-x86_64-5Server-cf-tools.xml"},

    {"name" : "rhel5-i386",
    "template_url" : "https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-i386-5Server-cf-tools.xml"}]
deployables = [
    {"name" : "Wordpress",
    "hwp" : ['medium-x86_64'],
    "catalog" : ['IT', 'engineering tools', 'web services']},
    {"name" : "SAP",
    "hwp" : ['small-x86_64', 'large-x86_64'],
    "catalog" : ['engineering tools']},
    {"name" : "Mail Server",
    "hwp" : ['large-x86_64', 'small-x86_64'],
    "catalog" : ['operations', 'engineering tools', 'IT']},
    {"name" : "DNS Server",
    "hwp" : ['small-x86_64', 'medium-x86_64'],
    "catalog" : ['operations', 'web services']},
    {"name" : "CloudEngine",
    "hwp" : ['medium-x86_64'],
    "catalog" : ['web services', 'operations']},
    {"name" : "SystemEngine",
    "hwp" : ['medium-x86_64'],
    "catalog" : ['web services', 'operations', 'IT']}]

