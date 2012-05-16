#!/usr/bin/env python 

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.dashboard import Dashboard

xfail = pytest.mark.xfail

class TestDashboard:

    def test_dashboard_present(self, mozwebqa):
        '''
        Verify dashboard page contains key elements.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        
        dashboard = Dashboard(mozwebqa)
        Assert.true(dashboard.is_dashboard_dropbutton_present)
        Assert.true(dashboard.is_dashboard_subscriptions_present)
        Assert.true(dashboard.is_dashboard_notificaitons_present)