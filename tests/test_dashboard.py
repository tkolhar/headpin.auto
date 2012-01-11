#!/usr/bin/env python 

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.dashboard import Dashboard

nondestructive = pytest.mark.nondestructive
destructive = pytest.mark.destructive

class TestDashboard:
    
    @nondestructive
    def test_dashboard_present(self, mozwebqa):
        '''
        Verify dashboard page contains key elements.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_the_current_page)
        Assert.true(home_page.header.is_user_logged_in)
        
        dashboard = Dashboard(mozwebqa)
        Assert.true(dashboard.is_dashboard_dropbutton_present)
        Assert.true(dashboard.is_dashboard_subscriptions_present)
        Assert.true(dashboard.is_dashboard_notificaitons_present)