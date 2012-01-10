#!/usr/bin/env python 

import pytest

from unittestzero import Assert
from pages.home import Home

xfail = pytest.mark.xfail
nondestructive = pytest.mark.nondestructive

class TestHome:
    
    @nondestructive
    def test_Title(self, mozwebqa):
        '''
        TCMS XXXXX
        '''
        home_page = Home(mozwebqa)
        Assert.true(home_page.is_the_current_page)
        #Assert.true(home_page)