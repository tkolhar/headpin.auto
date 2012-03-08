#!/usr/bin/env python 

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.systems import SystemsTab
from api.api import ApiTasks
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
        Assert.true(home_page.is_successful)
        Assert.true(home_page.is_dialog_cleared)
        
        api = ApiTasks()
        current_org = home_page.header.get_text_from_switcher
        api.create_envs(current_org)
        new_system_name = "system%s" % home_page.random_string()
        api.create_new_system(new_system_name, current_org)
        
        home_page.tabs.click_tab("systems_tab")
        Assert.true(home_page.is_the_current_page)
        
        systems = SystemsTab(mozwebqa)
        Assert.true(systems.is_systems_block_present)
        system_object = systems.select_random

        systems.system(system_object).click()

        Assert.true(systems.is_system_details_tab_present)
        Assert.true(systems.is_system_facts_tab_present)
        Assert.true(systems.is_system_subscriptions_tab_present)

    def test_remove_a_system(self, mozwebqa):
        ''' 
        create via api and remove a system.
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.header.is_user_logged_in)
        
        api = ApiTasks()
        current_org = home_page.header.get_text_from_switcher
        api.create_envs(current_org)
        new_system_name = "rmsystem%s" % home_page.random_string()

        api.create_new_system(new_system_name, current_org)
        
        home_page.tabs.click_tab("systems_tab")
        Assert.true(home_page.is_the_current_page)
        
        systems = SystemsTab(mozwebqa)
        home_page.enter_search_criteria(new_system_name)
        systems.system(new_system_name).click()
        Assert.true(systems.is_block_active)
        
        systems.remove_a_system()
        Assert.true(home_page.is_successful) 