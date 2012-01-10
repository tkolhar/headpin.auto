#!/usr/bin/env python 

import pytest

from unittestzero import Assert
from pages.home import Home

xfail = pytest.mark.xfail
nondestructive = pytest.mark.nondestructive

class TestHomePage:
    
    @nondestructive
    def test_Verify_Page_Title(self, mozwebqa):
        '''
        TCMS XXXXX
        '''
        home_page = Home(mozwebqa)
        Assert.true(home_page.is_the_current_page)
    
    @nondestructive
    def test_Username_Password_Text_Fields_Present(selfself, mozwebqa):
        home_page = Home(mozwebqa)
        Assert.true(home_page.is_username_field_present)
        Assert.true(home_page.is_password_field_present)
        
    @nondestructive
    def test_Is_Red_Hat_Logo_Present(self, mozwebqa):
        home_page = Home(mozwebqa)
        Assert.true(home_page.is_redhat_logo_visible)