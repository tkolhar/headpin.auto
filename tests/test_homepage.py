#!/usr/bin/env python 

import pytest

from unittestzero import Assert
from pages.home import Home

xfail = pytest.mark.xfail

@pytest.mark.nondestructive
class TestHomePage:

    def test_Verify_HomePage_Details(self, mozwebqa):
        home_page = Home(mozwebqa)
        Assert.true(home_page.is_the_current_page)

    def test_Username_Password_Text_Fields_Present(self, mozwebqa):
        home_page = Home(mozwebqa)
        Assert.true(home_page.is_username_field_present)
        Assert.true(home_page.is_password_field_present)

    def test_Is_Red_Hat_Logo_Present(self, mozwebqa):
        home_page = Home(mozwebqa)
        Assert.true(home_page.is_redhat_logo_visible)

    @pytest.mark.bugzilla(783301)
    def test_is_sam_h1_present(self, mozwebqa):
        # Really no accurate way to test this as window sizes change
        # and the element can be "visible" but not seen as it is hidden
        # behind another.
        home_page = Home(mozwebqa)
        Assert.true(home_page.is_sam_h1_visible)
        Assert.true(home_page.click_sam_h1())
    
    def test_admin_login_logout(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
                
        home_page.header.click_logout()
        Assert.true(home_page.is_username_field_present)
        Assert.true(home_page.is_password_field_present)
        
    def test_invalid_login(selfself, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login("admin", "badpassword")
        
        Assert.true(home_page.is_failed)
        