#!/usr/bin/env python

aeolus_msg = {
    'login' : 'Login successful!',
    'logout' : 'Aeolus Conductor | Login',
    'add_user' : 'User registered!',
    'delete_user' : 'User has been successfully deleted.',
    'add_user_group' : 'User Group added',
    'delete_user_group' : 'Deleted user group %s',
    'add_pool_family' : 'Pool family was added.',
    'delete_pool_family' : 'Pool Family was deleted!',
    'add_pool' : 'Pool added.',
    'delete_pool' : 'Pool %s was deleted.',
    'add_catalog' : 'Catalog created!',
    'delete_catalog' : 'Catalog deleted!',
    'connect_provider' : 'Successfully Connected to Provider',
    'connect_provider_acct' : 'Test Connection Success: Valid Account Details',
    'add_provider_acct' : 'Account %s was added.',
    'delete_provider_acct' : 'Provider account was deleted!'
    }

# see src/app/controllers for message text source
# https://github.com/Katello/katello/tree/master/src/app/controllers
katello_msg = {
    "add_sys_template" : "System Template '%s' was created.",
    "delete_sys_template" : "Template '%s' was deleted.",
    "add_org" : "Organization '%s' was created."
    }
