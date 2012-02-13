#!/usr/bin/env python

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.hello import Hello
import time
import sys
from selenium.webdriver.support.ui import WebDriverWait

xfail = pytest.mark.xfail

class TestHello:
    def test_hello_link_works(self, mozwebqa):
        #pytest.xfail("https://bugzilla.redhat.com/show_bug.cgi?id=784016")
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        Assert.true(home_page.is_dialog_cleared)
        
        hello = Hello(mozwebqa)
        
        home_page.click_hello_link()
        Assert.true(hello.is_username_present)
        
    def test_helptips_enabled_default(self, mozwebqa):
        #pytest.xfail("https://bugzilla.redhat.com/show_bug.cgi?id=784016")
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        Assert.true(home_page.is_dialog_cleared)
        
        hello = Hello(mozwebqa)
        
        home_page.click_hello_link()
        Assert.true(hello.is_helptips_enabled_present)
        
    def test_update_helptips(self, mozwebqa):
        #pytest.xfail("https://bugzilla.redhat.com/show_bug.cgi?id=784016")
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        
        hello = Hello(mozwebqa)
        
        home_page.click_hello_link()
        hello.click_helptips()
        # Need to ensure this gets pushed to the DB
        time.sleep(2)
        Assert.true(home_page.is_successful)
        Assert.true(home_page.is_dialog_cleared)
        home_page.tabs.click_tab("dashboard_tab")
        home_page.click_hello_link()
        Assert.false(hello.is_helptips_enabled)
        ###
        # Reset the value for future tests.
        ###
        home_page.click_hello_link()
        hello.click_helptips()
        ###
        # Need to ensure this gets pushed to the DB
        ###
        time.sleep(2)
        Assert.true(home_page.is_successful)
        home_page.tabs.click_tab("dashboard_tab")
        home_page.click_hello_link()
        Assert.true(hello.is_helptips_enabled)
        
    def test_update_email_addr(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        Assert.true(home_page.is_dialog_cleared)
        
        hello = Hello(mozwebqa)
        
        home_page.click_hello_link()
        
        new_user_email = "user-%s@example.com" % home_page.random_string()
        hello.update_email_addr(new_user_email)
        Assert.true(home_page.is_successful)
        
#    def test_change_password(self, mozwebqa):
#        home_page = Home(mozwebqa)
#        home_page.login()
#        Assert.true(home_page.is_successful)
#        
#        hello = Hello(mozwebqa)
#        
#        home_page.click_hello_link()
#        new_password = home_page.random_string()
#        hello.change_password(new_password)

        