#!/usr/bin/env python

import pytest

from unittestzero import Assert
from pages.home import Home
import time

xfail = pytest.mark.xfail

class TestTabs:

    def test_navigate_tabs(self, mozwebqa):
        tabs = ("administration_tab", "users_administration",
                              "roles_administration", "organizations_tab",
                              "organizations_subscriptions", "organizations_all",
                              "systems_tab", "activation_keys", "systems_by_environment",
                              "systems_all", "content_management_tab", "providers",
                              "dashboard_tab")
           
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.header.is_user_logged_in)
        
        for tab in tabs:
            home_page.tabs.click_tab(tab)
            Assert.true(home_page.is_the_current_page)
