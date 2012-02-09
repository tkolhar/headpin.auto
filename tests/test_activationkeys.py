#!/usr/bin/env python 

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.systems import ActivationKeysTab
from pages.contentmgmt import ContentManagementTab
from api.api import ApiTasks
import time

xfail = pytest.mark.xfail

class TestActivationKeys:
    _manifest_ = "/var/tmp/ActivationKeys_M1.zip"
    
    def test_create_activation_key(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        
        home_page.tabs.click_tab("systems_tab")
        home_page.tabs.click_tab("activation_keys")
        
        activationkeys = ActivationKeysTab(mozwebqa)
        
        new_activationkey_name = "newactivkey-%s" % home_page.random_string()
        activationkeys.click_new()
        activationkeys.enter_activation_key_name(new_activationkey_name)
        activationkeys.enter_activation_key_description(new_activationkey_name)
        activationkeys.click_save()
        Assert.true(home_page.is_successful)
        
    def test_remove_activationkey(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        
        home_page.tabs.click_tab("systems_tab")
        home_page.tabs.click_tab("activation_keys")
        
        activationkeys = ActivationKeysTab(mozwebqa)
        
        new_activationkey_name = "rmactivkey-%s" % home_page.random_string()
        activationkeys.click_new()
        activationkeys.enter_activation_key_name(new_activationkey_name)
        activationkeys.enter_activation_key_description(new_activationkey_name)
        activationkeys.click_save()
        Assert.true(home_page.is_successful)
        
        home_page.enter_search_criteria(new_activationkey_name)
        activationkeys.activationkey(new_activationkey_name).click()
        
        Assert.true(activationkeys.is_block_active)
        home_page.click_remove()
        home_page.click_confirm()
        Assert.true(home_page.is_successful)
        
    def test_activation_key_workflow(self, mozwebqa):
        ###
        # Create a org specific to this test.
        ###
        api = ApiTasks
        _new_org_name = "activationkeyorg%s" % home_page.random_string()
        api.create_new_org(_new_org_name)
        ###
        # Login
        ###
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        ###
        # Change to the newly created org
        ###
        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(_new_org_name)
        home_page.header.click_filtered_result(_new_org_name)
        ###
        # Navigate to Content Management and load manifest
        ###
        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        Assert.true(home_page.is_the_current_page)
        cm.enter_manifest(self._manifest_)
        Assert.true(home_page.is_successful)
        ###
        # Navigate to Activation Keys
        ###
        activationkeys = ActivationKeysTab(mozwebqa)
        home_page.tabs.click_tab("systems_tab")
        home_page.tabs.click_tab("activation_keys")
        
        