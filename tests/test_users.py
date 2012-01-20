#!/usr/bin/env python
# Name              : test_users.py
# Purpose           : Calls tests and assertions related to users.
# Contributors      : Eric L Sammons (eanxgeek)

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.administration import AdministrationTab
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
        new_user_name = "user-%s" % home_page.random_string()
        
        password = home_page.random_string()
        
        email_addr = new_user_name + "@example.com"
        administration.create_new_user(new_user_name, password, password, email_addr)

        time.sleep(5) # BZ 783153 requires this for now.
        
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
        new_user_name = home_page.random_string()
        new_user_name = "user-%s" % home_page.random_string()
        
        password = home_page.random_string()

        email_addr = new_user_name + "@example.com"
        administration.create_new_user(new_user_name, password, password, email_addr)
        
        time.sleep(5)
        Assert.true(home_page.is_successful)
        
        administration.user(new_user_name).click()
        Assert.true(administration.is_block_active)
        
        administration.remove_a_user()
        Assert.true(home_page.is_successful) 