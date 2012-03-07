#!/usr/bin/env python
# Purpose           : Calls tests and assertions related to roles.
# Contributors      : Eric L. Sammons (irc: eanxgeek)

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.administration import RolesTab
from api.api import ApiTasks
import time

xfail = pytest.mark.xfail

class TestRoles:
    def test_confirm_default_roles(self, mozwebqa):
        roles = ["Administrator", "Read Everything"]
    
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)

        rolestab = RolesTab(mozwebqa)

        home_page.tabs.click_tabv2("administration_tab")
        try:
            home_page.jquery_wait()
        finally:
            home_page.tabs.click_tabv2("roles_administration")
    
        for role in roles:
            rolestab.role(role).click()
            Assert.true(rolestab.is_permissions_visible)
            Assert.true(rolestab.is_users_visible)
            
            home_page.jquery_wait()
            displayed_role = rolestab.get_breadcrumb_role_name
            Assert.equal(displayed_role, role, "Expected role was not found")

    def test_add_user_to_administrator_role(self, mozwebqa):
        home_page = Home(mozwebqa)
        sysapi = ApiTasks()
        rolestab = RolesTab(mozwebqa)
        
        username = "admin%s" % home_page.random_string()
        email = username + "@example.com"
        password = home_page.random_string()
        
        sysapi.create_user(username, password, email)
        
        home_page.login()
        Assert.true(home_page.is_successful)   
        
        home_page.tabs.click_tabv2("administration_tab")
        home_page.jquery_wait(20)
        home_page.tabs.click_tabv2("roles_administration")
            
        rolestab.role("Administrator").click()
        rolestab.click_role_users()
        
        rolestab.role_user(username).add_user()
        Assert.true(rolestab.is_remove_visible)  
        
    def test_add_user_to_readeverything_role(self, mozwebqa):
        home_page = Home(mozwebqa)
        sysapi = ApiTasks()
        rolestab = RolesTab(mozwebqa)
        
        username = "readevery%s" % home_page.random_string()
        email = username + "@example.com"
        password = home_page.random_string()
        
        sysapi.create_user(username, password, email)
        
        home_page.login()
        Assert.true(home_page.is_successful)   
        
        home_page.tabs.click_tabv2("administration_tab")
        home_page.jquery_wait(30)
        home_page.tabs.click_tabv2("roles_administration")
            
        rolestab.role("Read Everything").click()
        rolestab.click_role_users()
        
        rolestab.role_user(username).add_user()
        Assert.true(rolestab.is_remove_visible)
        
    def test_create_new_role(self, mozwebqa):
        home_page = Home(mozwebqa)
        rolestab = RolesTab(mozwebqa)
        
        home_page.login()
        Assert.true(home_page.is_successful)   
        
        home_page.tabs.click_tabv2("administration_tab")
        home_page.jquery_wait(30)
        home_page.tabs.click_tabv2("roles_administration")
        
        role_name = "plainrole%s" % home_page.random_string()
        home_page.jquery_wait(20)
        home_page.click_new()
        home_page.jquery_wait(20)
        rolestab.create_new_role(role_name)
        home_page.jquery_wait(20)
        rolestab.save_role()
        Assert.true(home_page.is_successful)
        
    def test_create_role_name_already_taken(self, mozwebqa):
        home_page = Home(mozwebqa)
        rolestab = RolesTab(mozwebqa)
        
        home_page.login()
        Assert.true(home_page.is_successful)   
        
        home_page.tabs.click_tabv2("administration_tab")
        home_page.jquery_wait(30)
        home_page.tabs.click_tabv2("roles_administration")
        
        role_name = "plainrole%s" % home_page.random_string()
        home_page.jquery_wait(20)
        home_page.click_new()
        home_page.jquery_wait(20)
        rolestab.create_new_role(role_name)
        home_page.jquery_wait(20)
        rolestab.save_role()
        Assert.true(home_page.is_successful)
        
        home_page.jquery_wait(20)
        home_page.click_new()
        home_page.jquery_wait(20)
        rolestab.create_new_role(role_name)
        home_page.jquery_wait(20)
        rolestab.save_role()
        Assert.true(home_page.is_failed)
        
    def test_create_environment_ro_role(self, mozwebqa):
        pytest.xfail("work in progress")
        home_page = Home(mozwebqa)
        sysapi = ApiTasks()
        rolestab = RolesTab(mozwebqa)
        role_name = "environ_ro_%s" % home_page.random_string()
        
        sysapi.create_role(role_name)
        
        home_page.login()
        Assert.true(home_page.is_successful)
        
        home_page.tabs.click_tabv2("administration_tab")
        home_page.jquery_wait(30)
        home_page.tabs.click_tabv2("roles_administration")
        home_page.jquery_wait(30)
        rolestab.click_role_permissions()
        