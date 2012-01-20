#!/usr/bin/env python 

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.systems import SystemsTab
from pages.api import apiTasks
import random
import time
import sys

xfail = pytest.mark.xfail

class TestSystems:
    
    def test_systems_page(self, mozwebqa):
        '''
        Randomly select a system from the systems page
        and verify that key elements are present.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.header.is_user_logged_in)
        ###
        # API Setup
        ###
        sysapi = apiTasks(mozwebqa)
        new_org_name = "ACME_Corporation"
        new_system_name = "System-%s" % home_page.random_string()

        sysapi.create_envs(new_org_name)
        sysapi.create_new_system(new_system_name, new_org_name)
        
        home_page.tabs.click_tab("systems_tab")
        Assert.true(home_page.is_the_current_page)
        
        systems = SystemsTab(mozwebqa)
        Assert.true(systems.is_systems_block_present)
        system_object = systems.select_random

        systems.system(system_object).click()

        Assert.true(systems.is_system_details_tab_present)
        Assert.true(systems.is_system_facts_tab_present)
        Assert.true(systems.is_system_subscriptions_tab_present)
        
    def test_is_new_system_present(self, mozwebqa):
        pytest.xfail("https://bugzilla.redhat.com/show_bug.cgi?id=783299")
        '''
        Regression testing for bz783299, new system
        is no longer supported from webui.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.header.is_user_logged_in)
        
        home_page.tabs.click_tab("systems_tab")
        Assert.true(home_page.is_the_current_page)
        
        systems = SystemsTab(mozwebqa)
        Assert.false(systems.is_new_system_link_present)

    def test_remove_a_system(self, mozwebqa):
        ''' 
        create via api and remove a system.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.header.is_user_logged_in)
        
        sysapi = apiTasks(mozwebqa)
        new_org_name = "ACME_Corporation"
        new_system_name = "System-%s" % home_page.random_string()

        sysapi.create_envs(new_org_name)
        sysapi.create_new_system(new_system_name, new_org_name)
        
        home_page.tabs.click_tab("systems_tab")
        Assert.true(home_page.is_the_current_page)
        
        systems = SystemsTab(mozwebqa)
        systems.system(new_system_name).click()
        Assert.true(systems.is_block_active)
        
        systems.remove_a_system()
        Assert.true(home_page.is_successful) 