#!/usr/bin/env python 

import pytest

from unittestzero import Assert
from pages.katello.home import Home
import time

@pytest.mark.nondestructive
class TestHomePage(object):

    def test_verify_page_title(self, mozwebqa):
        home_page = Home(mozwebqa)
        Assert.true(home_page.is_the_current_page)

    def test_username_password_text_fields_present(self, mozwebqa):
        home_page = Home(mozwebqa)
        Assert.true(home_page.is_username_field_present)
        Assert.true(home_page.is_password_field_present)
    
    def test_admin_login_logout(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        home_page.select_org(home_page.org).click()
                
        home_page.header.click_logout()
        Assert.true(home_page.is_username_field_present)
        Assert.true(home_page.is_password_field_present)
        
    def test_invalid_login(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login("admin", "badpassword")
        Assert.true(home_page.is_failed)
        
