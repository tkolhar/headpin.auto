#!/usr/bin/env python 

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.systems import SystemsTab
import time
import sys

nondestructive = pytest.mark.nondestructive
destructive = pytest.mark.destructive
xfail = pytest.mark.xfail

class TestSystems:
    
    @nondestructive
    def test_systems_page(self, mozwebqa):
        '''
        Randomly select a system from the systems page
        and verify that key elements are present.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.header.is_user_logged_in)
        
        home_page.tabs.click_tab("systems_tab")
        Assert.true(home_page.is_the_current_page)
        
        systems = SystemsTab(mozwebqa)
        Assert.true(systems.is_systems_block_present)
        system_object = systems.select_random

        systems.system(system_object).click()

        Assert.true(systems.is_system_details_tab_present)
        Assert.true(systems.is_system_facts_tab_present)
        Assert.true(systems.is_system_subscriptions_tab_present)
        
    def test_is_create_new_present(self, mozwebqa):
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

    @nondestructive
    def test_remove_a_system(self, mozwebqa):
        pytest.xfail("https://bugzilla.redhat.com/show_bug.cgi?id=783299")
        ''' 
        create and remove a system.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.header.is_user_logged_in)
        
        home_page.tabs.click_tab("systems_tab")
        Assert.true(home_page.is_the_current_page)
        
        systems = SystemsTab(mozwebqa)
        new_system_name = home_page.unique_name()
        
        systems.create_new_virt_system(new_system_name)
        Assert.true(systems.system(new_system_name).is_displayed)
        
        Assert.true(systems.is_block_active)
        #systems.system(new_system_name).click()
        
        systems.remove_a_system()
        Assert.true(home_page.is_successful) 