#!/usr/bin/env python

import pytest

from unittestzero import Assert
from pages.home import Home
from api.api import ApiTasks
from pages.contentmgmt import ContentManagementTab
import os


class TestContentManagement:
    _org1_m1_manifest = "manifest_D1_O1_M1.zip"
    _org2_m1_manifest = "manifest_D2_O2_M1.zip"
    _org4_m1_manifest = "manifest_D4_O4_M1.zip"
    _scenario2_m1_d1_manifest = "scenario2_M1_D1.zip"
    _scenario5_o1_m2_manifest = "scenario5_O1_M2.zip"
    _scenario5_o1_m1_manifest = "scenario5_O1_M1.zip"
    _bz786963_manifest = "manifest_bz786963.zip"
    
    @pytest.mark.nondestructive
    def test_switch_org(self, mozwebqa):
        """
        Return True if switching to a random org in the 
        org switcher is successful.
        """
        sysapi = ApiTasks(mozwebqa)
        home_page = Home(mozwebqa)
        
        new_org_name = "someorg%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        
        home_page.login()

        active_org = home_page.header.get_text_from_switcher
        home_page.header.click_switcher()
        home_page.header.select_a_random_switcher_org()
        
        Assert.true(home_page.header.is_dashboard_selected)
    
    @pytest.mark.destructive        
    def test_load_manifest(self, mozwebqa):
        '''
        Scenario 1: Import Manifest (M1) from Distributor (D1) input Org1
        Result: Pass
        '''
        sysapi = ApiTasks(mozwebqa)
        home_page = Home(mozwebqa)
        
        new_org_name = "manifest%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        
        home_page.login()

        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)

        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        
        if home_page.project == "katello" or home_page.project == "cfse":
            cm.click_content_providers()
            cm.select_redhat_content_provider()
 
        cm.enter_manifest(os.path.realpath(self._org1_m1_manifest))
        Assert.true(home_page.is_successful)
        Assert.not_equal(cm.get_content_table_text, "No subscriptions have been imported.")
    
    @pytest.mark.destructive    
    def test_load_same_manifest_to_same_org_wo_force(self, mozwebqa):
        '''
        Scenario 2 with a twist. Import Manifest (M1) from Distributor (D1) into 
        Org1 w/o useing force.
        Result: Expect Fail
        '''
        sysapi = ApiTasks(mozwebqa)
        home_page = Home(mozwebqa)
        
        new_org_name = "manifest%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        
        home_page.login()

        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)

        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")

        if home_page.project == "katello" or home_page.project == "cfse":
            cm.click_content_providers()
            cm.select_redhat_content_provider()

        cm.enter_manifest(os.path.realpath(self._scenario2_m1_d1_manifest))

        cm.enter_manifest(os.path.realpath(self._scenario2_m1_d1_manifest))
        Assert.true(home_page.is_failed)
    
    @pytest.mark.destructive
    def test_load_same_manifest_to_same_org_w_force(self, mozwebqa):
        '''
        Scenario 2: Re-import same manifest into same org.
        Result: Pass
        '''
        home_page = Home(mozwebqa)
        sysapi = ApiTasks(mozwebqa)
        
        new_org_name = "manifest-%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        
        home_page.login()

        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)

        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        '''
        Need to clean this up a bit
        '''
        if home_page.project == "katello" or home_page.project == "cfse":
            cm.click_content_providers()
            cm.select_redhat_content_provider()
         
        cm.enter_manifest(os.path.realpath(self._org4_m1_manifest))
        
        cm.click_force()
        cm.enter_manifest(os.path.realpath(self._org4_m1_manifest))
        Assert.true(home_page.is_successful)
    
    @pytest.mark.destructive    
    def test_load_new_manifest_into_same_org_wo_force(self, mozwebqa):
        '''
        Scenario 5: Load updated (new) manifest into org where a manifest already exists.
        Result: Pass
        '''
        sysapi = ApiTasks(mozwebqa)
        home_page = Home(mozwebqa)
        
        new_org_name = "manifest-%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        
        home_page.login()

        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)

        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")

        if home_page.project == "katello" or home_page.project == "cfse":
            cm.click_content_providers()
            cm.select_redhat_content_provider()

        cm.enter_manifest(os.path.realpath(self._scenario5_o1_m1_manifest))
        cm.enter_manifest(os.path.realpath(self._scenario5_o1_m2_manifest))
        
        Assert.true(home_page.is_successful)
        Assert.not_equal(cm.get_content_table_text, "No subscriptions have been imported.")
    
    @pytest.mark.destructive    
    def test_load_second_manifest_second_org(self, mozwebqa):
        sysapi = ApiTasks(mozwebqa)
        home_page = Home(mozwebqa)
        
        new_org_name = "manifest-%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        
        home_page.login()

        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)

        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")

        if home_page.project == "katello" or home_page.project == "cfse":
            cm.click_content_providers()
            cm.select_redhat_content_provider()

        cm.enter_manifest(os.path.realpath(self._org2_m1_manifest))
        Assert.true(home_page.is_successful)
        Assert.not_equal(cm.get_content_table_text, "No subscriptions have been imported.")
    
    @pytest.mark.destructive
    @pytest.mark.bugzilla('787278')    
    def test_load_previous_manifest_to_another_org(self, mozwebqa):
        '''
        Scenario 3: Import Manifest (M1) from Distributor (D1) into Org2.
        Result Expected: Fail
        '''
        home_page = Home(mozwebqa)
        sysapi = ApiTasks(mozwebqa)
        
        new_org_name = "manifest-%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        
        home_page.login()

        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)

        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")

        if home_page.project == "katello" or home_page.project == "cfse":
            cm.click_content_providers()
            cm.select_redhat_content_provider()

        cm.enter_manifest(os.path.realpath(self._org1_m1_manifest))
        Assert.true(home_page.is_failed)
        
    @pytest.mark.destructive    
    def test_NumberFormatException_forInputString(self, mozwebqa):
        """
        Regression Test for bz786963
        """
        home_page = Home(mozwebqa)
        sysapi = ApiTasks(mozwebqa)
        
        new_org_name = "manifest-%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        
        home_page.login()

        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)

        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")

        if home_page.project == "katello" or home_page.project == "cfse":
            cm.click_content_providers()
            cm.select_redhat_content_provider()

        cm.enter_manifest(os.path.realpath(self._bz786963_manifest))
        Assert.true(home_page.is_successful)
        Assert.not_equal(cm.get_content_table_text, "No subscriptions have been imported.")

