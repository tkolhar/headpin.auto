#!/usr/bin/env python
# Purpose           : Calls tests and assertions related to users.
# Contributors      : Eric L Sammons (eanxgeek)

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.administration import AdministrationTab
from pages.api import apiTasks
import time
import sys
from selenium.webdriver.support.ui import WebDriverWait

xfail = pytest.mark.xfail

class Testusers:

    def test_create_new_user(self, mozwebqa):
        '''
        Test to create a new User, no org, no environment.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        Assert.true(home_page.header.is_user_logged_in)
        
        home_page.tabs.click_tab("administration_tab")
        Assert.true(home_page.is_the_current_page)
        
        administration = AdministrationTab(mozwebqa)
        new_user_name = home_page.random_string()
        new_user_name = "newuser-%s" % home_page.random_string()
        
        password = home_page.random_string()
        
        email_addr = new_user_name + "@example.com"
        administration.create_new_user(new_user_name, password, password, email_addr)
        
        Assert.true(home_page.is_successful)
        Assert.true(administration.user(new_user_name).is_displayed)
        
    def test_remove_a_user(self, mozwebqa):
        '''
        Test to remove a single user.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        Assert.true(home_page.header.is_user_logged_in)
        
        home_page.tabs.click_tab("administration_tab")
        Assert.true(home_page.is_the_current_page)
        
        administration = AdministrationTab(mozwebqa)
        sysapi = apiTasks(mozwebqa)
        
        new_user_name = home_page.random_string()
        new_user_name = "rmuser-%s" % home_page.random_string()
        password = home_page.random_string()
        email_addr = new_user_name + "@example.com"
        sysapi.create_user(new_user_name, password, email_addr)   
        time.sleep(2)
        home_page.enter_search_criteria("rmuser") 
        
        administration.user(new_user_name).click()
        Assert.true(administration.is_block_active)
        
        administration.remove_a_user()
        Assert.true(home_page.is_successful) 

    def test_user_search(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        
        home_page.tabs.click_tab("administration_tab")
        administration = AdministrationTab(mozwebqa)
        sysapi = apiTasks(mozwebqa)
        
        for i in range(1,5):
            new_user_name = "searchuser-%s" % home_page.random_string()
            password = home_page.random_string()
            email_addr = new_user_name + "@example.com"
            sysapi.create_user(new_user_name, password, email_addr)
            
        home_page.enter_search_criteria("searchuser")
        administration.is_search_correct("searchuser")
        
    def test_change_user_password_valid_as_admin(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        
        administration = AdministrationTab(mozwebqa)
        sysapi = apiTasks(mozwebqa)
        
        new_user_name = "chgpasswd-%s" % home_page.random_string()
        password = home_page.random_string()
        email_addr = new_user_name + "@example.com"
        
        sysapi.create_user(new_user_name, password, email_addr)
        home_page.tabs.click_tab("administration_tab")
        home_page.enter_search_criteria(new_user_name)
        administration.user(new_user_name).click()
        
        new_password = home_page.random_string()
        administration.change_password(new_password)
        Assert.true(home_page.is_successful)
        Assert.false(administration.passwords_do_not_match_visible)
        
    def test_change_user_password_does_not_match_as_admin(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        
        administration = AdministrationTab(mozwebqa)
        sysapi = apiTasks(mozwebqa)
        
        new_user_name = "chgpasswd-%s" % home_page.random_string()
        password = home_page.random_string()
        email_addr = new_user_name + "@example.com"
        
        sysapi.create_user(new_user_name, password, email_addr)
        home_page.tabs.click_tab("administration_tab")
        home_page.enter_search_criteria(new_user_name)
        administration.user(new_user_name).click()
        
        new_password = home_page.random_string()
        confirm_password = home_page.random_string()
        administration.change_password(new_password, confirm_password)
        Assert.true(administration.passwords_do_not_match_visible)
        
        