#!/usr/bin/env python

import pytest

from unittestzero import Assert
from pages.home import Home
import time
xfail = pytest.mark.xfail

class TestContentManagement:
    
    def test_switch_org(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        
        current_org = home_page.header.get_text_from_switcher()
        home_page.header.click_switcher()
        home_page.header.click_org_from_switcher()
        active_org = home_page.header.get_text_from_switcher()
        Assert.not_equal(active_org, current_org)