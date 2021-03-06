#!/usr/bin/env python
# Purpose           : Calls tests and assertions related to users.
# Contributors      : Eric L Sammons (eanxgeek)

import pytest
from unittestzero import Assert
from pages.katello.home import Home
from pages.katello.administration import AdministrationTab
from api.api import ApiTasks

xfail = pytest.mark.xfail

@pytest.mark.nondestructive
class Testusers:

    def test_create_new_user(self, mozwebqa):
        '''
        Test to create a new User, no org, no environment.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        
        home_page.tabs.click_tab("administration_tab")
        
        administration = AdministrationTab(mozwebqa)
        new_user_name = home_page.random_string()
        new_user_name = "newuser-%s" % home_page.random_string()
        
        password = "password%s" % home_page.random_string()
        
        email_addr = new_user_name + "@example.com"
        administration.create_new_user(new_user_name, password, password, email_addr)
        
        Assert.true(home_page.is_successful)
        Assert.true(administration.user(new_user_name).is_displayed)
        
    def test_duplicate_user_disallowed(self, mozwebqa):
        """
        Returns Pass if creating a existing user fails.
        """
        home_page = Home(mozwebqa)
        sysapi = ApiTasks(mozwebqa)
        
        new_user_name = "dupuser%s" % home_page.random_string()
        password = "password%s" % home_page.random_string()
        email_addr = new_user_name + "@example.com"
        sysapi.create_user(new_user_name, password, email_addr)
        
        home_page.login()
        home_page.tabs.click_tab("administration_tab")
        
        administration = AdministrationTab(mozwebqa)
        administration.create_new_user(new_user_name, password, password, email_addr)
        
        Assert.true(home_page.is_failed)
        
    def test_remove_a_user(self, mozwebqa):
        '''
        Test to remove a single user.
        '''
        home_page = Home(mozwebqa)
        sysapi = ApiTasks(mozwebqa)

        new_user_name = "rmuser%s" % home_page.random_string()
        password = "password%s" % home_page.random_string()
        email_addr = new_user_name + "@example.com"
        sysapi.create_user(new_user_name, password, email_addr)   

        home_page.login()
        
        home_page.tabs.click_tab("administration_tab")
        administration = AdministrationTab(mozwebqa)
        home_page.enter_search_criteria(new_user_name) 
        
        administration.user(new_user_name).click()

        home_page.click_remove()
        home_page.click_confirm()
        
        Assert.true(home_page.is_successful) 

    def test_user_search(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        
        home_page.tabs.click_tab("administration_tab")
        administration = AdministrationTab(mozwebqa)
        sysapi = ApiTasks(mozwebqa)
        
        for i in range(1,5):
            new_user_name = "%s" % home_page.random_string()
            password = "password%s" % home_page.random_string()
            email_addr = new_user_name + "@example.com"
            sysapi.create_user(new_user_name, password, email_addr)
            
        for i in range(1,5):
            new_user_name = "searchuser-%s" % home_page.random_string()
            password = "password%s" % home_page.random_string()
            email_addr = new_user_name + "@example.com"
            sysapi.create_user(new_user_name, password, email_addr)
            
        home_page.enter_search_criteria("searchuser*")
        home_page.jquery_wait(30)
        administration.is_search_correct("searchuser")
        
    def test_change_user_password_valid_as_admin(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        
        administration = AdministrationTab(mozwebqa)
        sysapi = ApiTasks(mozwebqa)
        
        new_user_name = "chgpasswd-%s" % home_page.random_string()
        password = "password%s" % home_page.random_string()
        email_addr = new_user_name + "@example.com"
        
        sysapi.create_user(new_user_name, password, email_addr)
        home_page.tabs.click_tab("administration_tab")
        home_page.enter_search_criteria(new_user_name)
        administration.user(new_user_name).click()
        
        new_password = "password%s" % home_page.random_string()
        administration.change_password(new_password)
        Assert.true(home_page.is_successful)
        
    def test_change_user_password_does_not_match_as_admin(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        
        administration = AdministrationTab(mozwebqa)
        sysapi = ApiTasks(mozwebqa)
        
        new_user_name = "chgpasswd-%s" % home_page.random_string()
        password = "password%s" % home_page.random_string()
        email_addr = new_user_name + "@example.com"
        
        sysapi.create_user(new_user_name, password, email_addr)
        home_page.tabs.click_tab("administration_tab")
        home_page.enter_search_criteria(new_user_name)
        administration.user(new_user_name).click()
        
        new_password = "password%s" % home_page.random_string()
        confirm_password = "password%s" % home_page.random_string()
        administration.change_password(new_password, confirm_password)
        Assert.true(administration.passwords_do_not_match_visible)

    def test_login_non_admin(self, mozwebqa):
        sysapi = ApiTasks(mozwebqa)
        home_page= Home(mozwebqa)
       
        new_user_name = "random%s" % home_page.random_string()
        password = "password%s" % home_page.random_string()
        email_addr = new_user_name + "@example.com"

        sysapi.create_user(new_user_name, password, email_addr)
        
        home_page.login(new_user_name, password)
        Assert.true(home_page.is_successful)
