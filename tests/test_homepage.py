#!/usr/bin/env python 

import pytest

from unittestzero import Assert
from pages.home import Home

xfail = pytest.mark.xfail

class TestHomePage:

    def test_Verify_HomePage_Details(self, mozwebqa):
        '''
        TCMS XXXXX
        '''
        home_page = Home(mozwebqa)
        Assert.true(home_page.is_the_current_page)

    def test_Username_Password_Text_Fields_Present(self, mozwebqa):
        home_page = Home(mozwebqa)
        Assert.true(home_page.is_username_field_present)
        Assert.true(home_page.is_password_field_present)

    def test_Is_Red_Hat_Logo_Present(self, mozwebqa):
        home_page = Home(mozwebqa)
        Assert.true(home_page.is_redhat_logo_visible)

    def test_is_sam_h1_present(self, mozwebqa):
        #pytest.xfail("https://bugzilla.redhat.com/show_bug.cgi?id=783301")
        home_page = Home(mozwebqa)
        Assert.true(home_page.get_location_sam_h1['x'] == 59)
        Assert.true(home_page.get_location_sam_h1['y'] == 9)
        Assert.true(home_page.get_location_sam_h1['hCode'] == 123731968)
        
    def test_admin_login_logout(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        
        Assert.true(home_page.is_the_current_page)
        Assert.true(home_page.header.is_user_logged_in)
        
        home_page.header.click_logout()
        Assert.true(home_page.is_username_field_present)
        Assert.true(home_page.is_password_field_present)
        
    def test_invalid_login(selfself, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login("admin", "badpassword")
        
        Assert.true(home_page.is_failed)
        