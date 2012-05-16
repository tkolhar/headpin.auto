#!/usr/bin/env python
from unittestzero import Assert
from pages.home import Home
from pages.administration import RolesTab
from api.api import ApiTasks
import time
import pytest

from data.datadrv import *

class TestRolesDataDriven(object):
    scenarios = [scenario1,scenario2]
    
    def test_datadriven_rbac(self, mozwebqa, org, perm_name, resource, verbs, allowed, disallowed):
        """
        Perform a data driven test related to role based access controls.
        All parameters are fullfilled by the data.  
        
        :param org: Organization Name
        :param perm_name: Permission name
        :param resource: Resource
        :param verbs: A tuple of verbs
        :returns: Pass or Fail for the test
        """

        sysapi = ApiTasks(mozwebqa)
        home_page = Home(mozwebqa)
        rolestab = RolesTab(mozwebqa)
        
        role_name = "role_%s" % (home_page.random_string())
        perm_name = "perm_%s" % (home_page.random_string())
        username = "user%s" % home_page.random_string()
        email = username + "@example.com"
        password = "redhat%s" % (home_page.random_string())
        
        sysapi.create_org(org)
        sysapi.create_user(username, password, email)
        
        home_page.login()
        
        home_page.tabs.click_tab("administration_tab")
        home_page.tabs.click_tab("roles_administration")
        rolestab.create_new_role(role_name)
        
        rolestab.click_role_permissions()
            
        rolestab.role_org(org).click()
        rolestab.click_add_permission()
        
        rolestab.select_resource_type(resource)
        home_page.click_next()
        for v in verbs:
            home_page.select('verbs', v)
        home_page.click_next()
        
        rolestab.enter_permission_name(perm_name)
        rolestab.enter_permission_desc('Added by QE test.')
        rolestab.click_permission_done()
        
        rolestab.click_root_roles()
        rolestab.click_role_users()
            
        rolestab.role_user(username).add_user()
        
        home_page.header.click_logout()
        home_page.login(username, password)
        
        for t in allowed:
            Assert.true(t(home_page))
        
        for t in disallowed:
            Assert.false(t(home_page))
