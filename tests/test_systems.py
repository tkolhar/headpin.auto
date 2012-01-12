#!/usr/bin/env python 

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.systems import Systems
import time

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
        newsystem = systems.create_new_virt_system

        Assert.true(systems.is_system_details_tab_present)
        #Assert.true(systems.is_system_facts_tab_present)
        #Assert.true(systems.is_system_software_tab_present)
        #Assert.true(systems.is_system_subscriptions_tab_present)
        #Assert.true(systems.is_system_details_name_present(newsystem))        