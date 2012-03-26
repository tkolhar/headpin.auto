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
    _activationkey_manifest = "/var/tmp/ActivationKeys_M1.zip"
    
    def test_create_activation_key(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        home_page.is_dialog_cleared
        
        current_org = home_page.header.get_text_from_switcher
        api = ApiTasks()
        api.create_envs(current_org)
        
        home_page.tabs.click_tab("systems_tab")
        home_page.jquery_wait(30)
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
        api = ApiTasks()
        activationkeys = ActivationKeysTab(mozwebqa)
        
        home_page.login()
        Assert.true(home_page.is_successful)
        home_page.is_dialog_cleared
        
        current_org = home_page.header.get_text_from_switcher
        api.create_envs(current_org)
        
        home_page.tabs.click_tab("systems_tab")
        home_page.jquery_wait(30)
        home_page.tabs.click_tab("activation_keys")

        new_activationkey_name = "rmactivkey%s" % home_page.random_string()
        activationkeys.click_new()
        activationkeys.enter_activation_key_name(new_activationkey_name)
        activationkeys.enter_activation_key_description(new_activationkey_name)
        activationkeys.click_save()
        Assert.true(home_page.is_successful)

        home_page.enter_search_criteria(new_activationkey_name)
        home_page.jquery_wait(30)

        #activationkeys.activationkey(new_activationkey_name).click()
        #home_page.jquery_wait(30)

        Assert.true(activationkeys.is_block_active)
        home_page.click_remove()
        home_page.click_confirm()
        Assert.true(home_page.is_successful)
        
    def test_activation_key_workflow(self, mozwebqa):
        home_page = Home(mozwebqa)
        api = ApiTasks()
        _new_org_name = "activationkeyorg%s" % home_page.random_string()
        api.create_org(_new_org_name)
        api.create_envs(_new_org_name)
        
        home_page.login()
        Assert.true(home_page.is_successful)
        home_page.is_dialog_cleared
        
        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(_new_org_name)
        home_page.header.click_filtered_result(_new_org_name)
        
        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        
        if home_page.product == "katello" or home_page.product == "cfse":
            cm.click_content_providers()
            cm.select_redhat_content_provider()
            
        cm.enter_manifest(self._activationkey_manifest)
        Assert.true(home_page.is_successful)
        home_page.is_dialog_cleared
        
        activationkeys = ActivationKeysTab(mozwebqa)
        home_page.tabs.click_tab("systems_tab")
        home_page.jquery_wait(30)
        home_page.tabs.click_tab("activation_keys")
        
        _new_activationkey_name = "%s" % home_page.random_string()
        activationkeys.click_new()
        activationkeys.enter_activation_key_name(_new_activationkey_name)
        activationkeys.enter_activation_key_description(_new_activationkey_name)
        activationkeys.click_save()
        Assert.true(home_page.is_successful)
        home_page.is_dialog_cleared
        Assert.true(activationkeys.is_block_active)

        activationkeys.click_available_subscriptions()
        
        rand_sub_id = activationkeys.select_a_random_sub()
        activationkeys.click_add_sub()

        Assert.true(home_page.is_successful)
        home_page.is_dialog_cleared
        activationkeys.click_applied_subscriptions()
        Assert.true(activationkeys.find_sub_by_id(rand_sub_id))
