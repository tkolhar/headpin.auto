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

nondestructive = pytest.mark.nondestructive
destructive = pytest.mark.destructive

class Testusers:
    
    @nondestructive
    def test_create_new_user(self, mozwebqa):
        '''
        Test to create a new org, no environment.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        Assert.true(home_page.header.is_user_logged_in)
        
        home_page.tabs.click_tab("administration_tab")
        Assert.true(home_page.is_the_current_page)
        
        administration = AdministrationTab(mozwebqa)
        new_user_name = home_page.unique_name("newuser")
        
        email_addr = new_user_name + "@example.com"
        administration.create_new_user(new_user_name, 'g00dp@ssw0rd', 'g00dp@ssw0rd', email_addr)
        Assert.true(home_page.is_successful)
        Assert.true(administration.user(new_user_name).is_displayed)