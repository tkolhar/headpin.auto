#!/usr/bin/env python 

import pytest
from unittestzero import Assert
from pages.katello.home import Home
from pages.katello.systems import ActivationKeysTab
from pages.katello.contentmgmt import ContentManagementTab
from api.api import ApiTasks
import time

class TestActivationKeys:
    _activationkey_manifest = "/var/tmp/ActivationKeys_M1.zip"
    
    @pytest.mark.nondestructive
    def test_create_activation_key(self, mozwebqa):
        """
        Return True if create activation key is successful.
        """
        home_page = Home(mozwebqa)
        home_page.login()
        
        current_org = home_page.header.get_text_from_switcher
        api = ApiTasks(mozwebqa)
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
    
    @pytest.mark.nondestructive
    def test_remove_activationkey(self, mozwebqa):
        """
        Return True if removing a activation key is successful.
        """
        home_page = Home(mozwebqa)
        api = ApiTasks(mozwebqa)
        activationkeys = ActivationKeysTab(mozwebqa)
        
        home_page.login()
        
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

        home_page.enter_search_criteria(new_activationkey_name)
        home_page.jquery_wait(30)

        if not activationkeys.is_block_active:
            activationkeys.activationkey(new_activationkey_name).click()

        home_page.click_remove()
        home_page.click_confirm()
        Assert.true(home_page.is_successful)
        
    @pytest.mark.destructive
    def test_activation_key_workflow(self, mozwebqa):
        """
        Return True of a activation key can be created and a single
        subscription from a multi subscription manifest can be
        added.
        """
        home_page = Home(mozwebqa)
        api = ApiTasks(mozwebqa)
        _new_org_name = "activationkeyorg%s" % home_page.random_string()
        api.create_org(_new_org_name)
        api.create_envs(_new_org_name)
        
        home_page.login()
        
        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(_new_org_name)
        home_page.header.click_filtered_result(_new_org_name)
        
        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        
        if home_page.project == "katello" or home_page.project == "cfse":
            cm.click_content_providers()
            cm.select_redhat_content_provider()
            
        cm.enter_manifest(self._activationkey_manifest)
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

        activationkeys.click_available_subscriptions()
        
        rand_sub_id = activationkeys.select_a_random_sub()
        activationkeys.click_add_sub()

        activationkeys.click_applied_subscriptions()
        Assert.true(activationkeys.find_sub_by_id(rand_sub_id))
