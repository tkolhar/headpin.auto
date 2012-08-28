#!/usr/bin/env python

'''
Aeolus input data
'''

class Admin(object):
    '''
    define users and user groups
    '''
    users = [
        {"fname" : "Mo",
        "lname" : "Joe",
        "email" : "mo.joe@redhat.com",
        "username" : "mojoe",
        "passwd" : "uber_secret",
        "max_instances" : "4" },

        {"fname" : "Mary",
        "lname" : "Jo",
        "email" : "mary.jo@redhat.com",
        "username" : "maryjo",
        "passwd" : "super_duper_secret",
        "max_instances" : "8" }]

    user_groups = [
        {"name" : "dev",
        "description" : "This is the dev group"},
        {"name" : "test",
        "description" : "This is the test group" },
        {"name" : "prod",
        "description" : "This is the production group" }]

class Provider(object):
    '''
    define provider accounts
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
        "key_file" : "data/keys/pk-VWEQTLOB2QVXYQYVJOFDFTDQ7J3GSF4E.pem",
        "key_cert_file" : "data/keys/cert-VWEQTLOB2QVXYQYVJOFDFTDQ7J3GSF4E.pem",
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
    define environments, pools, images
    '''
    pool_family_environments = [
        {"name" : "dev",
        "max_running_instances" : "8"},

        {"name" : "test",
        "max_running_instances" : "4"},

        {"name" : "prod",
        "max_running_instances" : "2"}]

    pools = [
        {"name" : "wordpress devs",
        "environment_parent" : "dev",
        "quota" : "",
        "enabled" : True},

        {"name" : "database devs",
        "environment_parent" : "dev",
        "quota" : "",
        "enabled" : False},

        {"name" : "qe",
        "environment_parent" : "test",
        "quota" : "",
        "enabled" : True},
        
        {"name" : "prod engineering",
        "environment_parent" : "prod",
        "quota" : "",
        "enabled" : True}]

    catalogs = [
        # random parents from pools list
        {"name" : "Aeolus blog",
        "pool_parent" : pools[0]["name"]},

        {"name" : "Aeolus Conductor",
        "pool_parent" : pools[2]["name"]}]

    images_from_url = [
        {"name" : "rhel6-x86_64",
        "template_url" : "https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-x86_64-6Server-cf-tools.xml"},

        {"name" : "rhel5-x86_64",
        "template_url" : "https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-x86_64-5Server-cf-tools.xml"},

        {"name" : "rhel5-i386",
        "template_url" : "https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-i386-5Server-cf-tools.xml"}]


