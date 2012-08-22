#!/usr/bin/env python 

import pytest
from unittestzero import Assert
from pages.katello.home import Home
from pages.katello.dashboard import Dashboard
from pages.katello.locators import *

@pytest.mark.nondestructive
class TestDashboard:

    def test_dashboard_present(self, mozwebqa):
        """
        Verify dashboard page contains key elements.
        """
        home_page = Home(mozwebqa)
        home_page.login()
        home_page.click(*login_org_dropdown)
        home_page.click_by_text(login_org_name_selector_css, home_page.org)
        
        dashboard = Dashboard(mozwebqa)
        
        Assert.true(dashboard.is_dashboard_dropbutton_present)
        Assert.true(dashboard.is_dashboard_subscriptions_present)
        Assert.true(dashboard.is_dashboard_notificaitons_present)
