#!/usr/bin/env python

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the redhat Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.redhat.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is redhat WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# redhat.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Bebe <florin.strugariu@softvision.ro>
#                 Alex Rodionov <p0deje@gmail.com>
#                 Teodosia Pop <teodosia.pop@softvision.ro>
#                 Alex Lakatos <alex@greensqr.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

import re

from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from pages.page import Page

import time


class Base(Page):

    _current_page_locator = (By.CSS_SELECTOR, ".paginator .num > a:nth-child(1)")

    _redhat_logo_link_locator = (By.CSS_SELECTOR, "#head header a")
    _redhat_logo_image_locator = (By.CSS_SELECTOR, "#head header img")

    _sam_header_locator = (By.CSS_SELECTOR, "#head header h1")
    
    @property
    def page_title(self):
        WebDriverWait(self.selenium, 10).until(lambda s: self.selenium.title)
        return self.selenium.title

    @property
    def redhat_logo_title(self):
        return self.selenium.find_element(*self._redhat_logo_link_locator).get_attribute('title')

    @property
    def redhat_logo_image_source(self):
        return self.selenium.find_element(*self._amo_logo_image_locator).get_attribute('src')

    @property
    def is_redhat_logo_visible(self):
        return self.is_element_visible(*self._redhat_logo_image_locator)

    def click_redhat_logo(self):
        self.selenium.find_element(*self._redhat_logo_link_locator).click()

    @property
    def current_page(self):
        return int(self.selenium.find_element(*self._current_page_locator).text)

    @property
    def header(self):
        return Base.HeaderRegion(self.testsetup)
    
    @property
    def tabs(self):
        return Base.TabRegion(self.testsetup)

    @property
    def _extract_integers(self, regex_pattern, *locator):
        """
        Returns a list of integers extracted from the text elements
        matched by the given xpath_locator and regex_pattern.
        """
        addon_numbers = [element.text for element in self.selenium.find_elements(*locator)]

        integer_numbers = [
            int(re.search(regex_pattern, str(x).replace(",", "")).group(1))
            for x in addon_numbers
        ]
        return integer_numbers

    class HeaderRegion(Page):

        #LoggedIn
        _account_controller_locator = (By.XPATH, "//li[@class='hello']/a")
        _logout_locator = (By.XPATH, "//a[normalize-space(.)='Logout']")
        
        def click_logout(self):
            self.selenium.find_element(*self._logout_locator).click()

        @property
        def is_user_logged_in(self):
            return self.is_element_visible(*self._account_controller_locator)
    
    class TabRegion(Page):
        ''' 
        Define elements of the tab region and 
        appropriate actions on those elements.
        '''
        _dashboard_tab_locator = (By.XPATH, "//a[.='Dashboard']")
        
        _content_management_tab_locator = (By.XPATH, "//a[.='Content Management']")
        _providers_content_management_subtab_locator = (By.XPATH, "//a[.='Providers']")
        
        _systems_tab_locator = (By.XPATH, "//a[.='Systems']")
        _all_systems_subtab_locator = (By.XPATH, "//a[.='All']")
        _by_environments_systems_subtab_locator = (By.XPATH, "//a[.='By Environments']")
        _activiation_keys_systems_subtab_locator = (By.XPATH, "//a[.='Activation Keys']")
        
        _organizations_tab_locator = (By.XPATH, "//a[.='Organizations']")
        _list_organizations_subtab_locator = (By.XPATH, "//a[.='List']")
        _subscriptions_organizations_subtab_locator = (By.XPATH, "//a[.='Subscriptions']")
        
        _administration_tab_locator = (By.XPATH, "//a[.='Administration']")
        _users_admin_subtab_locator = (By.XPATH, "//a[.='Users']")
        _roles_admin_subtab_locator = (By.XPATH, "//a[.='Roles']")
        
        def click_tab(self, tab):
            '''
            Determine which locator to use
            '''
            click_locator = ""
            hover_locator = ""
            
            if "dashboard_tab" in tab:
                click_locator = self.selenium.find_element(*self._dashboard_tab_locator)
            elif "content_management_tab" in tab:
                click_locator = self.selenium.find_element(*self._content_management_tab_locator)
            elif "providers" in tab:
                #hover_locator = self.selenium.find_element(*self._content_management_tab_locator)
                click_locator = self.selenium.find_element(*self._providers_content_management_subtab_locator)
            elif "systems_tab" in tab:
                click_locator = self.selenium.find_element(*self._systems_tab_locator)
            elif "systems_all" in tab:
                #hover_locator = self.selenium.find_element(*self._systems_tab_locator)
                click_locator = self.selenium.find_element(*self._all_systems_subtab_locator)
            elif "systems_by_environment" in tab:
                #hover_locator = self.selenium.find_element(*self._systems_tab_locator)
                click_locator = self.selenium.find_element(*self._by_environments_systems_subtab_locator)
            elif "activation_keys" in tab:
                #hover_locator = self.selenium.find_element(*self._systems_tab_locator)
                click_locator = self.selenium.find_element(*self._activiation_keys_systems_subtab_locator)
            elif "organizations_tab" in tab:
                click_locator = self.selenium.find_element(*self._organizations_tab_locator)
            elif "organizations_all" in tab:
                #hover_locator = self.selenium.find_element(*self._organizations_tab_locator)
                click_locator = self.selenium.find_element(*self._list_organizations_subtab_locator)
            elif "organizations_subscriptions" in tab:
                #hover_locator = self.selenium.find_element(*self._organizations_tab_locator)
                click_locator = self.selenium.find_element(*self._subscriptions_organizations_subtab_locator)
            elif "administration_tab" in tab:
                click_locator = self.selenium.find_element(*self._administration_tab_locator)
            elif "users_administration" in tab:
                #hover_locator = self.selenium.find_element(*self._administration_tab_locator)
                click_locator = self.selenium.find_element(*self._users_admin_subtab_locator)
            elif "roles_administration" in tab:
                #hover_locator = self.selenium.find_element(*self._administration_tab_locator)
                click_locator = self.selenium.find_element(*self._roles_admin_subtab_locator)
            '''
            if hover_locator:
                ActionChains(self.selenium).move_to_element(hover_locator).\
                    move_to_element(click_locator).\
                    click().perform()
            else:
            '''
            ActionChains(self.selenium).move_to_element(click_locator).\
                click().perform()
                    
    '''
    class BreadcrumbsRegion(Page):

        _breadcrumb_locator = (By.CSS_SELECTOR, '#breadcrumbs>ol')  # Base locator
        _link_locator = (By.CSS_SELECTOR, ' a')

        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        def click_breadcrumb(self):
            self._root_element.find_element(*self._link_locator).click()

        @property
        def name(self):
            return self._root_element.text

        @property
        def link_value(self):
            return self._root_element.find_element(*self._link_locator).get_attribute('href')
    '''
