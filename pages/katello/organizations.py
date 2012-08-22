#!/usr/bin/env python
# Name              : organizations.py
# Purpose           : controls for testing the organizations tab.
# Contributors      : Eric L Sammons (eanxgeek)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from pages.base import Base
from pages.page import Page
from pages.katello.locators import *
import random
import time

class OrganizationsTab(Base):
    _org_create_new_locator = (By.XPATH, "//a[@id='new']")
    _new_orgname_field_locator = (By.XPATH, "//input[@id='name']")
    _new_orgdesc_field_locator = (By.XPATH, "//textarea[@id='description']")
    _new_orgenv_name_field_locator = (By.XPATH, "//input[@id='envname']")
    _new_orgenvdesc_field_locator = (By.XPATH, "//textarea[@id='envdescription']")
    _new_org_save_button_locator = (By.XPATH, "//input[@id='organization_save']")
    
    _org_history_tab_locator = (By.XPATH, "//li[@id='history']")
    _org_details_tab_locator = (By.XPATH, "//li[@id='details']")
    
    _org_list_locator = (By.CSS_SELECTOR, "div.block")
    _org_block_active_locator = (By.CSS_SELECTOR, "div.block.active")
    _org_remove_item_locator = (By.CSS_SELECTOR, "a.remove_item")
    _confirmation_yes_locator = (By.XPATH, "//span[@class='ui-button-text'][text()='Yes']")
    
    def create_new_org(self, orgname, envname=None):
        new_org_locator = self.selenium.find_element(*self._org_create_new_locator)
        ActionChains(self.selenium).move_to_element(new_org_locator).\
            click().perform()
        
        org_name_locator = self.selenium.find_element(*self._new_orgname_field_locator)
        for k in orgname:
            org_name_locator.send_keys(k)
        
        org_desc_locator = self.selenium.find_element(*self._new_orgdesc_field_locator)
        for k in "This is a test organization, created by web ui automation":
            org_desc_locator.send_keys(k)
        
        if envname != None:
            orgenv_name_locator = self.selenium.find_element(*self._new_orgenv_name_field_locator)
            orgenv_name_locator.send_keys(envname)
            orgenv_desc_locator = self.selenium.find_element(*self._new_orgenvdesc_field_locator)
            for k in "This environment was created by web ui automation for %s":
                orgenv_desc_locator.send_keys(k)
            
        org_save_button_locator = self.selenium.find_element(*self._new_org_save_button_locator)
        ActionChains(self.selenium).move_to_element(org_save_button_locator).\
            click().perform()
            
        #WebDriverWait(self.selenium, 20).until(lambda s: self.is_element_present(*self._org_block_active_locator))
    
    def remove_a_org(self):
        WebDriverWait(self.selenium, 20).until(lambda s: s.find_element(*self._org_remove_item_locator).is_displayed())
        
        remove_button_locator = self.selenium.find_element(*self._org_remove_item_locator)
        ActionChains(self.selenium).move_to_element(remove_button_locator).\
            click().perform()
            
        WebDriverWait(self.selenium, 20).until(lambda s: s.find_element(*self._confirmation_yes_locator).is_displayed())
        
        confirm_button_locator = self.selenium.find_element(*self._confirmation_yes_locator)
        ActionChains(self.selenium).move_to_element(confirm_button_locator).\
            click().perform()
        
    def is_search_correct(self, criteria):
        WebDriverWait(self.selenium, 60).until(lambda s: s.find_element(*self._org_list_locator).is_displayed())
        for org in self.organizations:
            if criteria not in org.name:
                raise Exception('%s does not match Search Criteria %s' % (org.name, criteria))
        return True
                
    @property 
    def is_org_details_tab_present(self):
        return self.is_element_present(*self._org_details_tab_locator)
    
    @property
    def is_org_history_tab_present(self):
        return self.is_element_present(*self._org_history_tab_locator)
    
    def organization(self, value):
        for organization in self.organizations:
            if value in organization.name:
                return organization
        raise Exception('Organization not found: %s' % value)
    
    @property
    def is_block_active(self):
        return self.is_element_present(*self._org_block_active_locator)
    
    @property
    def organizations(self):
        return [self.Organizations(self.testsetup, element) for element in self.selenium.find_elements(*self._org_list_locator)]
    
    class Organizations(Page):
        
        _name_locator = (By.CSS_SELECTOR, "div.column_1.one-line-ellipsis")
        
        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        @property
        def name(self):
            name_text = self._root_element.find_element(*self._name_locator).text
            return name_text
        
        @property
        def is_displayed(self):
            return self.is_element_visible(*self._name_locator)
        
        def click(self):
            self._root_element.find_element(*self._name_locator).click()
