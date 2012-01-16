#!/usr/bin/env python 

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.systems import Systems
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
        
        systems = Systems(mozwebqa)
        new_system_name = systems.unique_system_name()
        
        systems.create_new_virt_system(new_system_name)
        
        Assert.true(systems.system(new_system_name).is_displayed)
        Assert.true(systems.is_system_details_tab_present)
        Assert.true(systems.is_system_facts_tab_present)
        Assert.true(systems.is_system_software_tab_present)
        Assert.true(systems.is_system_subscriptions_tab_present)
        Assert.true(systems.is_system_details_name_present(new_system_name))
'''
    @nondestructive
    def test_remove_a_system(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.header.is_user_logged_in)
        
        home_page.tabs.click_tab("systems_tab")
        Assert.true(home_page.is_the_current_page)
        
        systems = Systems(mozwebqa)
        rmeove_system_name = systems.unique_system_name("removesystem")
        time.sleep(20)
        systems.remove_a_system(remove_system_name)
'''
        
        
        
        