#!/usr/bin/env python 

import pytest
from unittestzero import Assert
from pages.home import Home
from pages.systems import ActivationKeysTab
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