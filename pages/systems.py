#!/usr/bin/env python

'''
Used to define the elements specific to the systems page
and specific controls.
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base import Base
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
    
    @property
    def create_new_virt_system(self, name_prefix="newsystem"):
        ''' Create a new system '''
        systemname = name_prefix + str(random.randint(0,10000))
        
        new_system_link_locator = self.selenium.find_element(*self._systems_create_new_locator)
        ActionChains(self.selenium).move_to_element(new_system_link_locator).\
            click().perform()
        
        system_name = self.selenium.find_element(*self._new_systemname_field_locator)
        system_name.send_keys(systemname)
        
        sockets = self.selenium.find_element(*self._new_system_sockets_field_locator)
        sockets.send_keys(str(random.randint(0,32)))
        
        virt = self.selenium.find_element(*self._new_system_virt_select_locator)
        ActionChains(self.selenium).move_to_element(virt).\
            click().perform()
            
        save_button = self.selenium.find_element(*self._new_system_save_locator)
        ActionChains(self.selenium).move_to_element(save_button).\
            click().perform()
        
        return(systemname)
    
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
    
    def is_system_details_name_present(self, systemname):
        _system_details_name_locator = (By.XPATH, "//a[.='" + systemname + "']")
        return self.is_element_present(*self._system_details_name_locator)
        
        
        
        
        
        
        
        
        
        