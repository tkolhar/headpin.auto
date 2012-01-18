#!/usr/bin/env python

'''
Used to define the elements specific to the systems page
and specific controls.
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from pages.base import Base
from pages.page import Page
import random
import time

class SystemsTab(Base):
    _systems_search_form_locator = (By.XPATH, "//form[@id='search_form']")
    _systems_search_input_locator = (By.XPATH, "//input[@id='search']")
    _systems_search_button_locator = (By.XPATH, "//button[@id='search_button']")
    _systems_create_new_locator = (By.XPATH, "//a[@id='new']")
    
    _new_systemname_field_locator = (By.XPATH, "//input[@id='name_field']")
    _new_system_arch_select_locator = (By.XPATH, "//select[@id='arch_arch_id']")
    _new_system_sockets_field_locator = (By.XPATH, "//input[@id='sockets_field']")
    _new_system_virt_select_locator = (By.XPATH, "//input[@value='virtual']")
    _new_system_physical_select_locator = (By.XPATH, "//input[@value='physical']")
    ## Need to add Environment elements here
    _new_system_save_locator = (By.XPATH, "//input[@id='system_save']")
    
    _facts_tab_locator = (By.XPATH, "//a[.='Facts']")
    _details_tab_locator = (By.XPATH, "//a[.='Details']")
    _software_tab_locator = (By.XPATH, "//a[.='Software']")
    _subscriptions_tab_locator = (By.XPATH, "//a[.='Subscriptions']")
    _system_details_name_locator = ""
    _system_list_locator = (By.CSS_SELECTOR, "div.block")
    _system_block_active_locator = (By.CSS_SELECTOR, "div.block.tall.active")
    
    _remove_system_locator = (By.CLASS_NAME, "remove_item")
    _confirmation_yes_locator = (By.XPATH, "//span[@class='ui-button-text'][text()='Yes']")
    
    def create_new_virt_system(self, system_name):
        ''' Create a new system '''
        new_system_link_locator = self.selenium.find_element(*self._systems_create_new_locator)
        ActionChains(self.selenium).move_to_element(new_system_link_locator).\
            click().perform()
        
        system_name_locator = self.selenium.find_element(*self._new_systemname_field_locator)
        system_name_locator.send_keys(system_name)
        
        sockets_locator = self.selenium.find_element(*self._new_system_sockets_field_locator)
        sockets_locator.send_keys(str(random.randint(0,32)))
        
        virt_locator = self.selenium.find_element(*self._new_system_virt_select_locator)
        ActionChains(self.selenium).move_to_element(virt_locator).\
            click().perform()
            
        save_button_locator = self.selenium.find_element(*self._new_system_save_locator)
        ActionChains(self.selenium).move_to_element(save_button_locator).\
            click().perform()
            
        current_no_systems = len(self.systems)
        WebDriverWait(self.selenium, 120).until(lambda s: self.is_element_present(*self._system_list_locator))
        WebDriverWait(self.selenium, 120).until(lambda s: self.is_element_present(*self._details_tab_locator))
        WebDriverWait(self.selenium, 120).until(lambda s: len(self.systems) > current_no_systems)
        time.sleep(2)
        
    def remove_a_system(self):
        '''
        Revmove a system.
        '''
        WebDriverWait(self.selenium, 30).until(lambda s: self.is_element_visible(*self._remove_system_locator))
        
        remove_button_locator = self.selenium.find_element(*self._remove_system_locator)
        ActionChains(self.selenium).move_to_element(remove_button_locator).\
            click().perform()
            
        WebDriverWait(self.selenium, 30).until(lambda s: self.is_element_visible(*self._confirmation_yes_locator))
        current_no_systems = len(self.systems)
        
        confirm_button_locator = self.selenium.find_element(*self._confirmation_yes_locator)
        ActionChains(self.selenium).move_to_element(confirm_button_locator).\
            click().perform()
        
        WebDriverWait(self.selenium, 120).until(lambda s: self.is_element_present(*self._system_list_locator))
        WebDriverWait(self.selenium, 60).until(lambda s: len(self.systems) < current_no_systems)
    
    @property
    def is_system_facts_tab_present(self):
        return self.is_element_present(*self._facts_tab_locator)
    @property
    def is_system_details_tab_present(self):
        return self.is_element_present(*self._details_tab_locator)
    
    @property
    def is_system_software_tab_present(self):
        return self.is_element_present(*self._software_tab_locator)
    
    @property
    def is_system_subscriptions_tab_present(self):
        return self.is_element_present(*self._subscriptions_tab_locator)
    
    def is_system_details_name_present(self, name):
        self._system_details_name_locator = (By.XPATH, "//div[text() = '" + name + "']")
        return self.is_element_present(*self._system_details_name_locator)
    
    @property
    def is_block_active(self):
        return self.is_element_present(*self._system_block_active_locator)
    
    def system(self, value):
        for system in self.systems:
            if value in system.name:
                return system
        raise Exception('System not found: %s' % value)
    
    @property
    def systems(self):
        return [self.Systems(self.testsetup, element) for element in self.selenium.find_elements(*self._system_list_locator)]
    
    class Systems(Page):
        
        _name_locator = (By.CLASS_NAME, 'one-line-ellipsis')
        _product_locator = (By.CSS_SELECTOR, 'div.block.tall')
        
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
