#!/usr/bin/env python

# generated from generate_dataset.py
# based on list definitions in raw_data.py

        
class Admin(object):
    '''
    Define users and groups
    '''
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
        {"fname" : "Mary",
        "lname" : "Smith",
        "email" : "mary.smith@redhat.com",
        "username" : "msmith",
        "passwd" : "2ti!)o08<CfrPI%v",
        "max_instances" : "2",
        "user_groups" : ['development'] },
        {"fname" : "James",
        "lname" : "Johnson",
        "email" : "james.johnson@apache.org",
        "username" : "jjohnson",
        "passwd" : "tw1cLeB#P0aulIR^Rg",
        "max_instances" : "6",
        "user_groups" : ['production'] },
        {"fname" : "George",
        "lname" : "Williams",
        "email" : "george.williams@mit.edu",
        "username" : "gwilliams",
        "passwd" : "`7Et%5,LVIOF",
        "max_instances" : "6",
        "user_groups" : ['test', 'admin'] },
        {"fname" : "Aaron",
        "lname" : "Jones",
        "email" : "aaron.jones@mozilla.org",
        "username" : "ajones",
        "passwd" : "er!*zZZimCe`Tsd0yT0",
        "max_instances" : "6",
        "user_groups" : ['development', 'test'] },
        {"fname" : "Nancy",
        "lname" : "Brown",
        "email" : "nancy.brown@mozilla.org",
        "username" : "nbrown",
        "passwd" : "02EyasMq|EnTzeu",
        "max_instances" : "5",
        "user_groups" : ['test', 'admin'] },
        {"fname" : "Nancy",
        "lname" : "David",
        "email" : "nancy.david@mozilla.org",
        "username" : "ndavid",
        "passwd" : "xb|gg",
        "max_instances" : "6",
        "user_groups" : ['admin', 'development'] },
        {"fname" : "Eric",
        "lname" : "Miller",
        "email" : "eric.miller@redhat.com",
        "username" : "emiller",
        "passwd" : "6zJVLx&g",
        "max_instances" : "10",
        "user_groups" : ['admin', 'production', 'test'] },
        {"fname" : "Mary",
        "lname" : "Wilson",
        "email" : "mary.wilson@redhat.com",
        "username" : "mwilson",
        "passwd" : "@NN$McG;rJH;|7",
        "max_instances" : "7",
        "user_groups" : ['test', 'production', 'admin'] },
        {"fname" : "Linda",
        "lname" : "Moore",
        "email" : "linda.moore@apache.org",
        "username" : "lmoore",
        "passwd" : "Cw.|Tut@U.QLT6Y.dU*b",
        "max_instances" : "8",
        "user_groups" : ['production'] },
        {"fname" : "Linda",
        "lname" : "Anderson",
        "email" : "linda.anderson@apache.org",
        "username" : "landerson",
        "passwd" : "AE8S@VNO",
        "max_instances" : "10",
        "user_groups" : ['admin'] },
        {"fname" : "Paul",
        "lname" : "Jackson",
        "email" : "paul.jackson@mozilla.org",
        "username" : "pjackson",
        "passwd" : "J>2uR>p)ura!h;!8>P",
        "max_instances" : "7",
        "user_groups" : ['admin', 'development', 'production'] },
        {"fname" : "Aaron",
        "lname" : "White",
        "email" : "aaron.white@redhat.com",
        "username" : "awhite",
        "passwd" : "nQ<Kc)8mm",
        "max_instances" : "1",
        "user_groups" : ['production', 'test', 'admin'] },
        {"fname" : "Aaron",
        "lname" : "Robinson",
        "email" : "aaron.robinson@mozilla.org",
        "username" : "arobinson",
        "passwd" : "t1hyb",
        "max_instances" : "2",
        "user_groups" : ['development', 'admin', 'test'] },
        {"fname" : "James",
        "lname" : "King",
        "email" : "james.king@mit.edu",
        "username" : "jking",
        "passwd" : "XmGKT6",
        "max_instances" : "2",
        "user_groups" : ['production'] },
        {"fname" : "Paul",
        "lname" : "Lopez",
        "email" : "paul.lopez@redhat.com",
        "username" : "plopez",
        "passwd" : "*|F0Z<w^1YC>",
        "max_instances" : "3",
        "user_groups" : ['production', 'test'] }]

class Provider(object):
    '''
    Define providers and provider accounts
    '''
    # provider_name string must match conductor
    # valid account types: "ec2", "rhevm", "vsphere"
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
        
class Environment(object):
    '''
    Define environments and pools
    '''
    pool_family_environments = [
        {"name" : "dev",
        "max_running_instances" : "1",
        "enabled_provider_accounts" : ['ec2-eu-west-1', 'ec2-us-west-1', 'ec2-ap-southeast-1', 'ec2-us-west-2', 'ec2-sa-east-1', 'ec2-ap-northeast-1']},
        {"name" : "test",
        "max_running_instances" : "8",
        "enabled_provider_accounts" : ['ec2-us-west-2']},
        {"name" : "stage",
        "max_running_instances" : "3",
        "enabled_provider_accounts" : ['ec2-us-west-2', 'ec2-sa-east-1', 'ec2-us-west-1', 'ec2-ap-southeast-1', 'ec2-sa-east-1', 'ec2-ap-northeast-1', 'ec2-eu-west-1']},
        {"name" : "production",
        "max_running_instances" : "4",
        "enabled_provider_accounts" : ['ec2-ap-northeast-1', 'ec2-us-west-2', 'ec2-eu-west-1', 'ec2-us-west-1']}]

    pools = [
        {"name" : "IT",
        "environment_parent" : ['dev'],
        "quota" : "8",
        "enabled" : True},
        {"name" : "web services",
        "environment_parent" : ['stage', 'dev', 'production'],
        "quota" : "4",
        "enabled" : True},
        {"name" : "engineering tools",
        "environment_parent" : ['dev', 'stage', 'production'],
        "quota" : "9",
        "enabled" : True},
        {"name" : "operations",
        "environment_parent" : ['stage', 'test'],
        "quota" : "4",
        "enabled" : True}]

class Content(object):
    '''
    Define catalogs, images and deployables
    '''
    catalogs = [
        {"name" : "IT",
        "pool_parent" : ['engineering tools']},
        {"name" : "web services",
        "pool_parent" : ['web services']},
        {"name" : "engineering tools",
        "pool_parent" : ['engineering tools', 'web services']},
        {"name" : "operations",
        "pool_parent" : ['IT', 'engineering tools']}]

    images_from_url = [
        {"name" : "rhel6-x86_64",
        "template_url" : "https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-x86_64-6Server-cf-tools.xml"},

        {"name" : "rhel5-x86_64",
        "template_url" : "https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-x86_64-5Server-cf-tools.xml"},

        {"name" : "rhel5-i386",
        "template_url" : "https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-i386-5Server-cf-tools.xml"}]
        
    deployables = [
        {"name" : "Wordpress",
        "hwp" : ['small-x86_64', 'medium-x86_64'],
        "catalog" : ['operations', 'web services', 'engineering tools']},
        {"name" : "SAP",
        "hwp" : ['large-x86_64', 'medium-x86_64'],
        "catalog" : ['engineering tools', 'web services']},
        {"name" : "Mail Server",
        "hwp" : ['small-x86_64'],
        "catalog" : ['engineering tools']},
        {"name" : "DNS Server",
        "hwp" : ['small-x86_64', 'medium-x86_64'],
        "catalog" : ['engineering tools', 'web services']},
        {"name" : "CloudEngine",
        "hwp" : ['large-x86_64'],
        "catalog" : ['IT', 'engineering tools']},
        {"name" : "SystemEngine",
        "hwp" : ['small-x86_64'],
        "catalog" : ['engineering tools', 'operations', 'web services']}]

