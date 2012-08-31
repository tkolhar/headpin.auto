#!/usr/bin/env python

# author: Aaron Weitekamp

# stand-alone script to create large, semi-random data set
# for CloudForms.Auto test runs
# uses lists from data/template_data.py as a template
# update template_data.py if desired and execute with no arguments

from data import template_data as raw
from string import Template
import string
from random import *

class Dataset(object):

    def __init__(self):
        self.data_file = 'data/large_dataset.py'
        self.outfile = open(self.data_file, 'w')

        header = '''#!/usr/bin/env python

# generated from generate_dataset.py
# based on list definitions in raw_data.py

        '''
        self.write_string(header)

    def close_file(self):
        self.outfile.close()

    def write_string(self, string):
        self.outfile.write('%s\n' % string)

    def write_dataset(self, name, data):
        self.outfile.write('    %s = [%s]\n\n' % (name, data))

    def write_class(self, my_class, docstring):
        string = """class %s(object):
    '''
    %s
    '''""" % (my_class, docstring)

        self.write_string(string)

    def write_indented_string(self, string):
        self.write_string('    %s' % string)

    def email(self, fname, lname, domain):
        email = "%s.%s@%s" % (fname, lname, domain)
        return email.lower()

    def username(self, fname, lname):
        username = "%s%s" % (fname[0], lname)
        return username.lower()

    def user_group_description(self, group):
        return "This is the %s group." % group 

    @property
    def passwd(self):
        i = randint(5, 20)
        chars = string.ascii_letters + string.digits + "!@#$%^&*()i;,.<>|`~"
        return ''.join(choice(chars) for x in range(i)) 

    def match_template(self, template, items):
        alist = []
        for item in items:
            alist.append(template.substitute(item))
        return ",".join(map(str, alist))

    def gen_user_group_list(self, groups):
        alist = []
        for group in groups:
            alist.append(dict(name=group, 
                description=self.user_group_description(group)))
        return alist

    def gen_user_list(self, fnames, lnames, domains, groups):
        alist = []
        for last_name in lnames:
            fname_index = randint(0, len(fnames)-1)
            dom_index = randint(0, len(domains)-1)
            group_index = randint(0, len(groups)-1)
            alist.append(dict(fname=fnames[fname_index],
                lname=last_name,
                email=self.email(fnames[fname_index], last_name, domains[dom_index]),
                username=self.username(fnames[fname_index], last_name),
                passwd=self.passwd,
                max_instances=randint(1, 10),
                user_groups=sample(groups, 
                    randint(1,len(groups)-1))
                ))
        return alist

    @property
    def provider_accounts(self):
        provider_acct = '''\
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
        '''

        return provider_acct

    def gen_env_list(self, envs, accts):
        alist = []
        for env in envs:
            alist.append(dict(environment=env, 
                max_inst=randint(1, 12), 
                prov_accts=sample(accts, (randint(1,len(accts)-1)))))
        return alist

    def gen_pool_list(self, pools, envs):
        alist = []
        for pool in pools:
            alist.append(dict(pool_env=pool,
                environments=sample(envs, (randint(1,len(envs)-1))),
                quota=randint(1, 12)))
        return alist

    def gen_cat_list(self, catalogs, pool_envs):
        alist = []
        for cat in catalogs:
            alist.append(dict(catalog=cat,
                pools=sample(pool_envs, (randint(1,len(pool_envs)-1))))),
        return alist

    @property
    def images(self):
        images = '''\
    images_from_url = [
        {"name" : "rhel6-x86_64",
        "template_url" : "https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-x86_64-6Server-cf-tools.xml"},

        {"name" : "rhel5-x86_64",
        "template_url" : "https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-x86_64-5Server-cf-tools.xml"},

        {"name" : "rhel5-i386",
        "template_url" : "https://qeblade40.rhq.lab.eng.bos.redhat.com/templates/Dev/rhel-i386-5Server-cf-tools.xml"}]
        '''
        return images

    def gen_dep_list(self, deps, hwp, catalogs):
        alist = []
        for dep in deps:
            alist.append(dict(deployable=dep,
                hwp=sample(hwp, (randint(1,len(hwp)-1))),
                catalog=sample(catalogs, (randint(1,len(catalogs)-1)))))
        return alist
    
###
# end of class
###

data = Dataset()

# user groups
data.write_class('Admin', 'Define users and groups')

user_group_template = Template('''
        {"name" : "$name", 
        "description" : "$description"}''')

user_group_list = data.gen_user_group_list(raw.user_groups)
user_group_string = data.match_template(user_group_template, user_group_list)
data.write_dataset("user_groups", user_group_string)

# users
user_template = Template('''
        {"fname" : "$fname",
        "lname" : "$lname",
        "email" : "$email",
        "username" : "$username",
        "passwd" : "$passwd",
        "max_instances" : "$max_instances",
        "user_groups" : $user_groups }''')

user_list = data.gen_user_list(raw.user_fname, 
    raw.user_lname, 
    raw.email_domains, 
    raw.user_groups)
user_string = data.match_template(user_template, user_list)
data.write_dataset("users", user_string)

# provider accounts
data.write_class('Provider', 'Define providers and provider accounts')

provider_comment = '''\
    # provider_name string must match conductor
    # valid account types: "ec2", "rhevm", "vsphere"'''

data.write_string(provider_comment)
data.write_string(data.provider_accounts)


data.write_class('Environment', 'Define environments and pools')

# environments (pool families)
env_template = Template('''
        {"name" : "$environment",
        "max_running_instances" : "$max_inst",
        "enabled_provider_accounts" : $prov_accts}''')

env_list = data.gen_env_list(raw.environments, raw.provider_accounts)
env_string = data.match_template(env_template, env_list)
data.write_dataset("pool_family_environments", env_string)

# pools
pool_template = Template('''
        {"name" : "$pool_env",
        "environment_parent" : $environments,
        "quota" : "$quota",
        "enabled" : True}''')

pool_list = data.gen_pool_list(raw.pools, raw.environments)
pool_string = data.match_template(pool_template, pool_list)
data.write_dataset("pools", pool_string)

data.write_class('Content', 'Define catalogs, images and deployables')

# catalogs
cat_template = Template('''
        {"name" : "$catalog",
        "pool_parent" : $pools}''')
cat_list = data.gen_cat_list(raw.catalogs, raw.pools)
cat_string = data.match_template(cat_template, cat_list)
data.write_dataset("catalogs", cat_string)

# images
data.write_string(data.images)

# deployables
dep_template = Template('''
        {"name" : "$deployable",
        "hwp" : $hwp,
        "catalog" : $catalog}''')

dep_list = data.gen_dep_list(raw.deployables, raw.hardware_prof, raw.catalogs)
dep_string = data.match_template(dep_template, dep_list)
data.write_dataset("deployables", dep_string)

data.close_file()

