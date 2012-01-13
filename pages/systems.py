#!/usr/bin/env python

'''
Used to define the elements specific to the systems page
and specific controls.
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base import Base
from pages.page import Page
import random

class Systems(Base):
    _systems_search_form_locator = (By.XPATH, "//form[@id='search_form']")
    _systems_search_input_locator = (By.XPATH, "//input[@id='search']")
    _systems_search_button_locator = (By.XPATH, "//button[@id='search_button']")
    _systems_create_new_locator = (By.XPATH, "//a[@id='new']")
    _systems_list_box_locator = (By.XPATH, "//div[@id='list']")
    _systems_server_name_locator = (By.XPATH, "//div[@class='one-line-ellipsis']")
    
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
    _success_message = (By.XPATH, "//div[contains(@class,'jnotify-notification-message')]")
    _system_list_locator = (By.CLASS_NAME, "block_tall")
    
    _remove_system_locator = (By.CLASS_NAME, "remove_item")
    
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
    '''        
    def remove_a_system(self, system_name):
        self._system_details_name_locator = (By.XPATH, "//div[text() = '" + name + "']")
        system_list = ()
        system_list = self.get_system_list
        print system_list()
        system_locator = self.selenium.find_element(choice(system_list))
        ActionChains(self.selenium).move_to_element(system_locator).\
            click().perform()
        time.sleep(20)
    '''
    
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
    
    @property
    def is_success_message_present(self):
        return self.is_element_present(*self._success_message)
    
    def is_system_details_name_present(self, name):
        self._system_details_name_locator = (By.XPATH, "//div[text() = '" + name + "']")
        return self.is_element_present(*self._system_details_name_locator)
    
    def unique_system_name(self, name="newsystem"):
        system_name = name + str(random.randint(0,100000))
        return system_name
        
    def system(self, value):
        for system in self.systems:
            if value in system.name:
                return system
        raise Exception('System not found: %s' % value)
    
    @property
    def systems(self):
        return [self.Systems(self.testsetup, element) for element in self.selenium.find_elements(*self._system_list_locator)]
    
    class Systems(Page):
        
        _name_locator = (By.CLASS_NAME, "one-line-ellipsis")
        
        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        @property
        def name(self):
            return self._root_element.find_element(*self._name_locator).text