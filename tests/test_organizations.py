#!/usr/bin/env python
# Name              : test_organizations.py
# Purpose           : Calls tests and assertions related to organizations.
# Contributors      : Eric L Sammons (eanxgeek)

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.organizations import OrganizationsTab
from pages.api import apiTasks
import random
import time
import sys

xfail = pytest.mark.xfail

class TestOrganizations:

    def test_create_new_org(self, mozwebqa):
        '''
        Test to create a new org, no environment.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        Assert.true(home_page.header.is_user_logged_in)
        
        home_page.tabs.click_tab("organizations_tab")
        Assert.true(home_page.is_the_current_page)
        
        organizations = OrganizationsTab(mozwebqa)
        new_org_name = home_page.random_string()
        new_org_name = "Org-%s" % home_page.random_string()
        
        organizations.create_new_org(new_org_name)
        Assert.true(home_page.is_successful)
        
        Assert.true(organizations.organization(new_org_name).is_displayed)
        Assert.true(organizations.is_org_details_tab_present)
        Assert.true(organizations.is_org_history_tab_present)

    def test_create_new_org_w_env(self, mozwebqa):
        '''
        Test to create a new org, with environment.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        Assert.true(home_page.header.is_user_logged_in)
        
        home_page.tabs.click_tab("organizations_tab")
        Assert.true(home_page.is_the_current_page)
        
        ENVIRONMENTS = ["DEV", "TEST", "STAGE", "PROD"]
        randenv = random.choice(ENVIRONMENTS)
        
        organizations = OrganizationsTab(mozwebqa)
        new_org_name = home_page.random_string()
        new_org_name = "Org-%s" % home_page.random_string()
        
        organizations.create_new_org(new_org_name, randenv)
        Assert.true(home_page.is_successful)
        
        Assert.true(organizations.organization(new_org_name).is_displayed)
        Assert.true(organizations.is_org_details_tab_present)
        Assert.true(organizations.is_org_history_tab_present)