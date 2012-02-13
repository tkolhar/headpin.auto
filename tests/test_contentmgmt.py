#!/usr/bin/env python

import pytest

from unittestzero import Assert
from pages.home import Home
from pages.api import apiTasks
from pages.contentmgmt import ContentManagementTab
import time
xfail = pytest.mark.xfail

class TestContentManagement:
    _org1_m1_manifest = "/var/tmp/manifest_D1_O1_M1.zip"
    _org2_m1_manifest = "/var/tmp/manifest_D2_O2_M1.zip"
    _org3_m1_manifest = "/var/tmp/manifest_D3_O3_M1.zip"
    _org4_m1_manifest = "/var/tmp/manifest_D4_O4_M1.zip"
    _org1_m2_manifest = "/var/tmp/manifest_D1_O1_M2.zip"
    _bz786963_manifest = "/var/tmp/manifest_bz786963.zip"
    
    def test_switch_org(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        ####
        # Create a new org, have to ensure we have +1
        # Don't fear if this org is not the selected.
        ###
        sysapi = apiTasks(mozwebqa)
        new_org_name = "someorg%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        ###
        # Get the current org for comparison later
        # and then switch org
        ###
        Assert.true(home_page.is_dialog_cleared)        
        current_org = home_page.header.get_text_from_switcher()
        home_page.header.click_switcher()
        home_page.header.click_org_from_switcher()
        active_org = home_page.header.get_text_from_switcher()
        Assert.not_equal(active_org, current_org)
            
    def test_load_manifest(self, mozwebqa):
        '''
        Scenario 1: Import Manifest (M1) from Distributor (D1) input Org1
        Result: Pass
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        ###
        # Create a org to work with
        ###
        sysapi = apiTasks(mozwebqa)
        new_org_name = "manifest%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        ###
        # Find that org and select it
        ###
        Assert.true(home_page.is_dialog_cleared)
        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)
        ###
        # Install Manifest
        ###
        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        Assert.true(home_page.is_the_current_page)
        cm.enter_manifest(self._org1_m1_manifest)
        Assert.true(home_page.is_successful)
        Assert.not_equal(cm.get_content_table_text, "No subscriptions have been imported.")
        
    def test_load_same_manifest_to_same_org_wo_force(self, mozwebqa):
        '''
        Scenario 2 with a twist. Import Manifest (M1) from Distributor (D1) into Org1 w/o useing force.
        Result: Expect Fail
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        ###
        # Create a org to work with
        ###
        sysapi = apiTasks(mozwebqa)
        new_org_name = "manifest%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        ###
        # Find that org and select it
        ###
        Assert.true(home_page.is_dialog_cleared)
        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)
        ###
        # Install Manifest
        ###
        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        Assert.true(home_page.is_the_current_page)
        cm.enter_manifest(self._org3_m1_manifest)
        Assert.true(home_page.is_successful)
        ###
        # Install manifest again
        ###
        cm.enter_manifest(self._org3_m1_manifest)
        Assert.true(home_page.is_failed)
    
    def test_load_same_manifest_to_same_org_w_force(self, mozwebqa):
        '''
        Scenario 2: Re-import same manifest into same org.
        Result: Pass
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        ###
        # Create a org to work with
        ###
        sysapi = apiTasks(mozwebqa)
        new_org_name = "manifest%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        ###
        # Find that org and select it
        ###
        Assert.true(home_page.is_dialog_cleared)
        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)
        ###
        # Install Manifest
        ###
        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        Assert.true(home_page.is_the_current_page)
        cm.enter_manifest(self._org4_m1_manifest)
        Assert.true(home_page.is_successful)
        ###
        # Install manifest again
        ###
        cm.click_force()
        cm.enter_manifest(self._org4_m1_manifest)
        Assert.true(home_page.is_successful)
        
    def test_load_new_manifest_into_same_org_wo_force(self, mozwebqa):
        '''
        Scenario 5: Load updated (new) manifest into org where a manifest already exists.
        Result: Pass
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        ###
        # Create a org to work with
        ###
        sysapi = apiTasks(mozwebqa)
        new_org_name = "manifest%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        ###
        # Find that org and select it
        ###
        Assert.true(home_page.is_dialog_cleared)
        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)
        ###
        # Install Manifest
        ###
        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        Assert.true(home_page.is_the_current_page)
        cm.enter_manifest(self._org1_m1_manifest)
        Assert.true(home_page.is_successful)
        ###
        # Install manifest again
        ###
        cm.enter_manifest(self._org1_m2_manifest)
        Assert.true(home_page.is_successful)
        Assert.true(home_page.is_dialog_cleared)
        Assert.not_equal(cm.get_content_table_text, "No subscriptions have been imported.")
        
    def test_load_second_manifest_second_org(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        ###
        # Create a org to work with
        ###
        sysapi = apiTasks(mozwebqa)
        new_org_name = "manifest%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        ###
        # Find that org and select it
        ###
        Assert.true(home_page.is_dialog_cleared)
        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)
        ###
        # Install Manifest
        ###
        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        Assert.true(home_page.is_the_current_page)
        cm.enter_manifest(self._org2_m1_manifest)
        Assert.true(home_page.is_successful)
        Assert.true(home_page.is_dialog_cleared)
        Assert.not_equal(cm.get_content_table_text, "No subscriptions have been imported.")
        
    def test_load_previous_manifest_to_another_org(self, mozwebqa):
        pytest.xfail("https://bugzilla.redhat.com/show_bug.cgi?id=787278")
        '''
        Scenario 3: Import Manifest (M1) from Distributor (D1) into Org2.
        Result Expected: Fail
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        ###
        # Create a org to work with
        ###
        sysapi = apiTasks(mozwebqa)
        new_org_name = "manifest%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        ###
        # Find that org and select it
        ###
        Assert.true(home_page.is_dialog_cleared)
        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)
        ###
        # Install Manifest
        ###
        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        Assert.true(home_page.is_the_current_page)
        cm.enter_manifest(self._org1_m1_manifest)
        Assert.true(home_page.is_failed)
        Assert.equal(cm.get_content_table_text, "No subscriptions have been imported.")
        
    def test_NumberFormatException_forInputString(self, mozwebqa):
        '''
        Regression Test for bz786963
        '''
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        ###
        # Create a org to work with
        ###
        sysapi = apiTasks(mozwebqa)
        new_org_name = "manifest%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        ###
        # Find that org and select it
        ###
        Assert.true(home_page.is_dialog_cleared)
        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)
        ###
        # Install Manifest
        ###
        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        Assert.true(home_page.is_the_current_page)
        cm.enter_manifest(self._bz786963_manifest)
        Assert.true(home_page.is_successful)
        Assert.not_equal(cm.get_content_table_text, "No subscriptions have been imported.")

