#!/usr/bin/env python

#####
# Name            : base.py
# Purpose         : Common elements and controls
# Contributor     : Eric L Sammons
#####

import re

from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from pages.page import Page

import time
import string
import random


class Base(Page):

    _current_page_locator = (By.CSS_SELECTOR, ".paginator .num > a:nth-child(1)")

    _redhat_logo_link_locator = (By.CSS_SELECTOR, "#head header a")
    _redhat_logo_image_locator = (By.XPATH, "//img[contains(@src, '/headpin/images/rh-logo.png')]")
    _headpin_logo_image_locator = (By.XPATH, "//img[contains(@src, '/headpin/images/logo.png')]")

    _sam_header_locator = (By.CSS_SELECTOR, "#head header h1")
    _success_notification_locator = (By.CSS_SELECTOR, "div.jnotify-notification.jnotify-notification-success")
    _error_notification_locator = (By.CSS_SELECTOR, "div.jnotify-notification.jnotify-notification-error")
    _sam_h1_locator = (By.CSS_SELECTOR, "h1")
    _hello_link_locator = (By.XPATH, "//a[contains(@href, '/headpin/users?id=')]")
    _search_form_locator = (By.XPATH, "//form[@id='search_form']")
    _search_input_locator = (By.XPATH, "//input[@id='search']")
    _search_button_locator = (By.XPATH, "//button[@id='search_button']")
    _footer_version_text_locator = (By.CSS_SELECTOR, "div.grid_16.ca.light_text")
    _remove_item_locator = (By.CSS_SELECTOR, "a.remove_item")
    _confirmation_yes_locator = (By.XPATH, "//span[@class='ui-button-text'][text()='Yes']")
    
    def random_string(self):
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for x in range(random.randint(8, 16)))
    
    @property
    def page_title(self):
        WebDriverWait(self.selenium, 10).until(lambda s: self.selenium.title)
        return self.selenium.title

    @property
    def redhat_logo_title(self):
        return self.selenium.find_element(*self._redhat_logo_link_locator).get_attribute('title')
    
    def enter_search_criteria(self, criteria):
        search_input_locator = self.selenium.find_element(*self._search_input_locator)
        for c in criteria:
            search_input_locator.send_keys(c)
        search_input_locator.send_keys("\n")
        #self.selenium.find_element(*self._search_button_locator).click()
        # Give block time to update; should investigate using WebDriverWait.
        time.sleep(1)
    
    def click_remove(self):
        WebDriverWait(self.selenium, 60).until(lambda s: self.is_element_visible(*self._remove_item_locator))
        remove_button_locator = self.selenium.find_element(*self._remove_item_locator)
        ActionChains(self.selenium).move_to_element(remove_button_locator).\
            click().perform()
            
    def click_confirm(self):
        WebDriverWait(self.selenium, 60).until(lambda s: self.is_element_visible(*self._confirmation_yes_locator))
        confirm_button_locator = self.selenium.find_element(*self._confirmation_yes_locator)
        ActionChains(self.selenium).move_to_element(confirm_button_locator).\
            click().perform()

    @property
    def redhat_logo_image_source(self):
        return self.selenium.find_element(*self._amo_logo_image_locator).get_attribute('src')

    def is_footer_version_text_visible(self):
        #return self.selenium.find_elements_by_partial_link_text('Subscription Asset Manager Version')
        return self.selenium.find_element(*self._footer_version_text_locator).text
    
    @property
    def is_redhat_logo_visible(self):
        if self.product == "SAM":
            return self.is_element_visible(*self._redhat_logo_image_locator)
        elif self.product == "HEADPIN":
            return self.is_element_visible(*self._headpin_logo_image_locator)
            

    def click_redhat_logo(self):
        self.selenium.find_element(*self._redhat_logo_link_locator).click()
        
    def click_hello_link(self):
        self.selenium.find_element(*self._hello_link_locator).click()
    
    @property
    def is_sam_h1_visible(self):
        return self.is_element_visible(*self._sam_h1_locator)
    
    def click_sam_h1(self):
        try:
            self.selenium.find_element(*self._sam_h1_locator).click()
            return True
        except:
            throw ("The header element should be visible, it's not, do something!") 
    
    @property
    def get_location_sam_h1(self):
        return self.get_location(*self._sam_h1_locator)

    @property
    def is_successful(self):
        return self.is_element_visible(*self._success_notification_locator)
    
    @property
    def is_failed(self):
        return self.is_element_visible(*self._error_notification_locator)
    
    @property
    def current_page(self):
        return int(self.selenium.find_element(*self._current_page_locator).text)

    @property
    def header(self):
        return Base.HeaderRegion(self.testsetup)
    
    @property
    def tabs(self):
        return Base.TabRegion(self.testsetup)

    class HeaderRegion(Page):

        _account_controller_locator = (By.CSS_SELECTOR, "li.hello")
        _logout_locator = (By.XPATH, "//a[normalize-space(.)='Logout']")
        _org_switcher_locator = (By.CSS_SELECTOR, "a#switcherButton")
        _org_switcher_org_locator = (By.CSS_SELECTOR, "a[href*='org_id=2']")
        _org_input_filter_locator = (By.CSS_SELECTOR, "input#orgfilter_input")
        _org_filtered_button_locator = (By.CSS_SELECTOR, "button.filter_button")
        
        def click_logout(self):
            self.selenium.find_element(*self._logout_locator).click()

        @property
        def is_user_logged_in(self):
            return self.is_element_visible(*self._account_controller_locator)
        
        def click_hello(self):
            self.selenium.find_element(*self._account_controller_locator).click()
        
        def click_switcher(self):
            self.selenium.find_element(*self._org_switcher_locator).click()
        
        def click_org_from_switcher(self):
            WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_visible(*self._org_switcher_org_locator))
            self.selenium.find_element(*self._org_switcher_org_locator).click()
        
        def get_text_from_switcher(self):
            return self.selenium.find_element(*self._org_switcher_locator).text 
        
        def filter_org_in_switcher(self, criteria):
            org_input_filter = self.selenium.find_element(*self._org_input_filter_locator)
            for c in criteria:
                org_input_filter.send_keys(c)
            
        def click_filtered_result(self, criteria):
            _org_filtered_result_locator = (By.XPATH, "//a[contains(text(), '" + criteria + "')]")
            self.selenium.find_element(*_org_filtered_result_locator).click()
    
    class TabRegion(Page):
        ''' 
        Define elements of the tab region and 
        appropriate actions on those elements.
        '''
        _dashboard_tab_locator = (By.XPATH, "//a[.='Dashboard']")
        
        _content_management_tab_locator = (By.XPATH, "//a[.='Content Management']")
        _providers_content_management_subtab_locator = (By.XPATH, "//a[@href='/headpin/providers/redhat_provider'][text()='Content Providers']")
        
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
                WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_visible(*self._dashboard_tab_locator))
                click_locator = self.selenium.find_element(*self._dashboard_tab_locator)
            elif "content_management_tab" in tab:
                WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_visible(*self._content_management_tab_locator))
                click_locator = self.selenium.find_element(*self._content_management_tab_locator)
            elif "providers" in tab:
                #hover_locator = self.selenium.find_element(*self._content_management_tab_locator)
                WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_visible(*self._providers_content_management_subtab_locator))
                click_locator = self.selenium.find_element(*self._providers_content_management_subtab_locator)
            elif "systems_tab" in tab:
                WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_visible(*self._systems_tab_locator))
                click_locator = self.selenium.find_element(*self._systems_tab_locator)
            elif "systems_all" in tab:
                WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_visible(*self._all_systems_subtab_locator))
                #hover_locator = self.selenium.find_element(*self._systems_tab_locator)
                click_locator = self.selenium.find_element(*self._all_systems_subtab_locator)
            elif "systems_by_environment" in tab:
                #hover_locator = self.selenium.find_element(*self._systems_tab_locator)
                WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_visible(*self._all_systems_subtab_locator))
                click_locator = self.selenium.find_element(*self._by_environments_systems_subtab_locator)
            elif "activation_keys" in tab:
                WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_visible(*self._activiation_keys_systems_subtab_locator))
                #hover_locator = self.selenium.find_element(*self._systems_tab_locator)
                click_locator = self.selenium.find_element(*self._activiation_keys_systems_subtab_locator)
            elif "organizations_tab" in tab:
                WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_visible(*self._organizations_tab_locator))
                click_locator = self.selenium.find_element(*self._organizations_tab_locator)
            elif "organizations_all" in tab:
                #hover_locator = self.selenium.find_element(*self._organizations_tab_locator)
                WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_visible(*self._list_organizations_subtab_locator))
                click_locator = self.selenium.find_element(*self._list_organizations_subtab_locator)
            elif "organizations_subscriptions" in tab:
                #hover_locator = self.selenium.find_element(*self._organizations_tab_locator)
                WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_visible(*self._subscriptions_organizations_subtab_locator))
                click_locator = self.selenium.find_element(*self._subscriptions_organizations_subtab_locator)
            elif "administration_tab" in tab:
                WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_visible(*self._administration_tab_locator))
                click_locator = self.selenium.find_element(*self._administration_tab_locator)
            elif "users_administration" in tab:
                #hover_locator = self.selenium.find_element(*self._administration_tab_locator)
                WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_visible(*self._users_admin_subtab_locator))
                click_locator = self.selenium.find_element(*self._users_admin_subtab_locator)
            elif "roles_administration" in tab:
                #hover_locator = self.selenium.find_element(*self._administration_tab_locator)
                WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_visible(*self._roles_admin_subtab_locator))
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