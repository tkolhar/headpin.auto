#!/usr/bin/env python 

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.systems import SystemsTab
import time
import sys

nondestructive = pytest.mark.nondestructive
destructive = pytest.mark.destructive

class TestSystems:
    
    @nondestructive
    def test_create_new_virt_system(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.header.is_user_logged_in)
        
        home_page.tabs.click_tab("systems_tab")
        Assert.true(home_page.is_the_current_page)
        
        systems = SystemsTab(mozwebqa)
        new_system_name = home_page.unique_name("createsystem")
        
        systems.create_new_virt_system(new_system_name)
        Assert.true(home_page.is_successful)
        
        Assert.true(systems.system(new_system_name).is_displayed)
        Assert.true(systems.is_system_details_tab_present)
        Assert.true(systems.is_system_facts_tab_present)
        Assert.true(systems.is_system_software_tab_present)
        Assert.true(systems.is_system_subscriptions_tab_present)
        Assert.true(systems.is_system_details_name_present(new_system_name))

    @nondestructive
    def test_remove_a_system(self, mozwebqa):
        ''' 
        create and remove a system.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.header.is_user_logged_in)
        
        home_page.tabs.click_tab("systems_tab")
        Assert.true(home_page.is_the_current_page)
        
        systems = SystemsTab(mozwebqa)
        new_system_name = home_page.unique_name("removesystem")
        
        systems.create_new_virt_system(new_system_name)
        Assert.true(systems.system(new_system_name).is_displayed)
        
        Assert.true(systems.is_block_active)
        #systems.system(new_system_name).click()
        
        systems.remove_a_system()
        Assert.true(home_page.is_successful) 