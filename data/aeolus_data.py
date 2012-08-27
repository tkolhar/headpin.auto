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
    provider_accounts = [
        {"provider_name" : "ec2-us-east-1",
        "account_name" : "my ec2",
        "access_key" : "KIAJ4MRLWELDTLRNVNA",
        "secret_access_key" : "NtwIubgKpedYIzwu9x8P+JiHv9Pv/U8ZF6yj7nQO",
        "account_number" : "7835-8090-1744",
        "key_file" : "data/certificates/pk-VWEQTLOB2QVXYQYVJOFDFTDQ7J3GSF4E.pem",
        "key_cert_file" : "data/certificates/cert-VWEQTLOB2QVXYQYVJOFDFTDQ7J3GSF4E.pem",
        "priority" : "",
        "quota" : "4"}]
