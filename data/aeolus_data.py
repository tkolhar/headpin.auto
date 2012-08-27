#!/usr/bin/env python

'''
Aeolus input data
'''

class Admin(object):
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
    # provider_name string must match
    # valid account types: "ec2", "rhevm", "vsphere"
    accounts = [
        {"type" : "ec2",
        "provider_name" : "ec2-us-east-1",
        "provider_account_name" : "Public cloud east",
        "username_access_key" : "AKIAIXO4IC7JLNX24DZQ",
        "password_secret_access_key" : "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",
        "account_number" : "7835-8090-1744",
        "key_file" : "/home/aaron/dev/proj/CloudForms.Auto/data/keys/pk-VWEQTLOB2QVXYQYVJOFDFTDQ7J3GSF4E.pem",
        "key_cert_file" : "/home/aaron/dev/proj/CloudForms.Auto/data/keys/cert-VWEQTLOB2QVXYQYVJOFDFTDQ7J3GSF4E.pem",
        "provider_account_priority" : "",
        "provider_account_quota" : ""},

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
