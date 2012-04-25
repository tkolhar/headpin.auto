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

        api = ApiTasks(mozwebqa)
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
        
        api = ApiTasks(mozwebqa)
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
        
    def test_search_systems(self, mozwebqa):
        home_page = Home(mozwebqa)
        sysapi = ApiTasks(mozwebqa)
        
        home_page.login()
        Assert.true(home_page.is_successful)
        current_org = home_page.header.get_text_from_switcher
        
        # Some bad results
        for i in range(1,5):
            new_system_name = "%s" % home_page.random_string()
            sysapi.create_new_system(new_system_name, current_org)
        
        # The actual systems to search for   
        for i in range(1,5):
            new_sys_name = "SearchSys%s" % home_page.random_string()
            sysapi.create_new_system(new_sys_name, current_org)
        
        home_page.tabs.click_tab("systems_tab")
        systems = SystemsTab(mozwebqa)
        home_page.jquery_wait(30)
        
        home_page.enter_search_criteria("SearchSys*")
        Assert.true(systems.is_search_correct("SearchSys"))