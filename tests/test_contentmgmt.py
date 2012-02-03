#!/usr/bin/env python

import pytest

from unittestzero import Assert
from pages.home import Home
from pages.api import apiTasks
from pages.contentmgmt import ContentManagementTab
import time
xfail = pytest.mark.xfail

class TestContentManagement:
    
    def test_switch_org(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        ####
        # Create a new org, have to ensure we have +1
        # Don't fear if this org is not the selected.
        ###
        sysapi = apiTasks(mozwebqa)
        new_org_name = "someorg-%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        ###
        # Get the current org for comparison later
        # and then switch org
        ###        
        current_org = home_page.header.get_text_from_switcher()
        home_page.header.click_switcher()
        home_page.header.click_org_from_switcher()
        active_org = home_page.header.get_text_from_switcher()
        Assert.not_equal(active_org, current_org)
            
    def test_load_manifest(self, mozwebqa, manifest_file="/var/tmp/sam_manifest_1.zip"):
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        ###
        # Create a org to work with
        ###
        sysapi = apiTasks(mozwebqa)
        new_org_name = "manifest-%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        ###
        # Find that org and select it
        ###
        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)
        ###
        # Install Manifest
        ###
        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        Assert.true(home_page.is_the_current_page)
        cm.enter_manifest(manifest_file)
        Assert.true(home_page.is_successful)
        Assert.not_equal(cm.get_content_table_text, "No subscriptions have been imported.")
        
    def test_load_second_manifest(self, mozwebqa):
        self.test_load_manifest(mozwebqa, "/var/tmp/sam_manifest_2.zip")
        
    def test_load_previous_manifest_to_another_org(self, mozwebqa):
        pytest.xfail("https://bugzilla.redhat.com/show_bug.cgi?id=786963")
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        ###
        # Create a org to work with
        ###
        sysapi = apiTasks(mozwebqa)
        new_org_name = "manifest-%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        ###
        # Find that org and select it
        ###
        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)
        ###
        # Install Manifest
        ###
        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        Assert.true(home_page.is_the_current_page)
        cm.enter_manifest("/var/tmp/sam_manifest_1.zip")
        Assert.true(home_page.is_failed)
        Assert.not_equal(cm.get_content_table_text, "No subscriptions have been imported.")
        
    def test_NumberFormatException_forInputString(self, mozwebqa):
        pytest.xfail("https://bugzilla.redhat.com/show_bug.cgi?id=787278")
        home_page = Home(mozwebqa)
        home_page.login()
        Assert.true(home_page.is_successful)
        ###
        # Create a org to work with
        ###
        sysapi = apiTasks(mozwebqa)
        new_org_name = "manifest-%s" % home_page.random_string()
        sysapi.create_org(new_org_name)
        ###
        # Find that org and select it
        ###
        home_page.header.click_switcher()
        home_page.header.filter_org_in_switcher(new_org_name)
        home_page.header.click_filtered_result(new_org_name)
        ###
        # Install Manifest
        ###
        cm = ContentManagementTab(mozwebqa)
        home_page.tabs.click_tab("content_management_tab")
        Assert.true(home_page.is_the_current_page)
        cm.enter_manifest("/var/tmp/bz786963.zip")
        Assert.true(home_page.is_successful)
        Assert.not_equal(cm.get_content_table_text, "No subscriptions have been imported.")