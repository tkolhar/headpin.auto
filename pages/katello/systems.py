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
from pages.katello.locators import *
from random import choice
import random

class SystemsTab(Base):
    _systems_search_form_locator = (By.XPATH, "//form[@id='search_form']")
    _systems_search_input_locator = (By.XPATH, "//input[@id='search']")
    _systems_search_button_locator = (By.XPATH, "//button[@id='search_button']")
    #_systems_create_new_locator = (By.XPATH, "//a[@id='new']")
    #_systems_create_new_locator = (By.ID, "new")
    
    _new_systemname_field_locator = (By.XPATH, "//input[@id='name_field']")
    _new_system_arch_select_locator = (By.XPATH, "//select[@id='arch_arch_id']")
    _new_system_sockets_field_locator = (By.XPATH, "//input[@id='sockets_field']")
    _new_system_virt_select_locator = (By.XPATH, "//input[@value='virtual']")
    _new_system_physical_select_locator = (By.XPATH, "//input[@value='physical']")
    _new_system_save_locator = (By.XPATH, "//input[@id='system_save']")
    
    _facts_tab_locator = (By.XPATH, "//a[.='Facts']")
    _details_tab_locator = (By.XPATH, "//a[.='Details']")
    _software_tab_locator = (By.XPATH, "//a[.='Software']")
    _subscriptions_tab_locator = (By.XPATH, "//a[.='Subscriptions']")
    #_system_details_name_locator = ""
    _system_list_locator = (By.CSS_SELECTOR, "div.block")
    _system_block_active_locator = (By.CSS_SELECTOR, "div.block.tall.active")
    _system_block_locator = (By.CSS_SELECTOR, "div.block.tall")
    _remove_system_locator = (By.CLASS_NAME, "remove_item")
    _confirmation_yes_locator = (By.XPATH, "//span[@class='ui-button-text'][text()='Yes']")
    
    def remove_a_system(self):
        '''
        Revmove a system.
        '''
        WebDriverWait(self.selenium, 30).until(lambda s: s.find_element(*self._remove_system_locator).is_displayed())
        
        remove_button_locator = self.selenium.find_element(*self._remove_system_locator)
        ActionChains(self.selenium).move_to_element(remove_button_locator).\
            click().perform()
            
        WebDriverWait(self.selenium, 30).until(lambda s: s.find_element(*self._confirmation_yes_locator).is_displayed())
        current_no_systems = len(self.systems)
        
        confirm_button_locator = self.selenium.find_element(*self._confirmation_yes_locator)
        ActionChains(self.selenium).move_to_element(confirm_button_locator).\
            click().perform()
        
    
    @property
    def is_system_facts_tab_present(self):
        return self.is_element_present(*self._facts_tab_locator)
    @property
    def is_system_details_tab_present(self):
        return self.is_element_visible(*self._details_tab_locator)
    
    @property
    def is_system_software_tab_present(self):
        return self.is_element_present(*self._software_tab_locator)
    
    @property
    def is_system_subscriptions_tab_present(self):
        return self.is_element_present(*self._subscriptions_tab_locator)
    
    def is_system_details_name_present(self, name):
        self._system_details_name_locator = (By.XPATH, "//div[text() = '" + name + "']")
        return self.is_element_visible(*self._system_details_name_locator)
    
    @property
    def is_new_system_link_present(self):
        return self.is_element_present(*self._systems_create_new_locator)
    
    @property
    def is_block_active(self):
        return self.is_element_present(*self._system_block_active_locator)
    
    @property
    def is_systems_block_present(self):
        return self.is_element_visible(*self._system_list_locator)
    
    @property
    def select_random(self):
        return choice(self.systems).name
    
    def is_search_correct(self, criteria):
        
        WebDriverWait(self.selenium, 30).until(lambda s: s.find_element(*self._system_block_locator).is_displayed())
        self.jquery_wait()
        for sys in self.systems:
            if criteria not in sys.name:
                raise Exception('%s does not match Search Criteria %s' % (sys.name, criteria))
        return True
    
    def system(self, value):
        for system in self.systems:
            if value in system.name:
                return system
        raise Exception('System not found: %s' % value)
    
    @property
    def systems(self):
        return [self.Systems(self.testsetup, element) for element in self.selenium.find_elements(*self._system_list_locator)]

###
# from aw
###
    def create_system_template(self, name, desc):
        '''
        create system template, name and description
        '''
        #self.selenium.find_element(*new_template).click()
        self.selenium.find_element(*new_template).click()
        self.send_text(name, *system_template_name)
        self.send_text(desc, *system_template_description)
        self.selenium.find_element(*template_save).click()

    def remove_element(self):
        '''
        click remove button
        '''
        self.selenium.find_element(*remove_template).click()
        self.click_by_text('span', 'Yes')
###
# end from aw
###

    class Systems(Page):
        
        _name_locator = (By.CLASS_NAME, 'one-line-ellipsis')
        
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

class ActivationKeysTab(Base):
    _activation_key_name_input_field_locator = (By.CSS_SELECTOR, "input#activation_key_name")
    _activation_key_description_locator = (By.CSS_SELECTOR, "textarea#activation_key_description")
    _activation_key_save_button_locator = (By.CSS_SELECTOR, "input#save_key")
    _activation_key_new_button_locator = (By.CSS_SELECTOR, "a#new.block.fr")
    _activationkey_list_locator = (By.CSS_SELECTOR, "div.block")
    _activationkey_block_active_locator = (By.CSS_SELECTOR, "div.block.active")
    
    _subscriptions_locator = (By.CSS_SELECTOR, "span.fl.subscription_row input")
    _subscriptions_checkbox_locator = (By.XPATH, "//input[@type='checkbox']")
    
    _available_subscriptions_tab_locator = (By.XPATH, "//a[.= 'Available Subscriptions']")
    _applied_subscriptions_tab_locator = (By.XPATH, "//a[.= 'Applied Subscriptions']")
    _available_subscriptions_input_filter_locator = (By.CSS_SELECTOR, "input#filter")
    _available_subscriptions_submit_locator = (By.CSS_SELECTOR, "input#subscription_submit_button.submit")
    
    def enter_activation_key_name(self, name):
        '''Enter the name of the new activation key'''
        name_locator = self.selenium.find_element(*self._activation_key_name_input_field_locator)
        for c in name:
            name_locator.send_keys(c)
            
    def enter_activation_key_description(self, desc):
        description_locator = self.selenium.find_element(*self._activation_key_description_locator)
        for c in desc:
            description_locator.send_keys(c)
            
    def click_save(self):
        save_button_locator = self.selenium.find_element(*self._activation_key_save_button_locator)
        ActionChains(self.selenium).move_to_element(save_button_locator).\
            click().perform()
            
    def click_new(self):
        new_button_locator = self.selenium.find_element(*self._activation_key_new_button_locator)
        ActionChains(self.selenium).move_to_element(new_button_locator).\
            click().perform()
    
    @property
    def is_block_active(self):
        return self.is_element_present(*self._activationkey_block_active_locator)
    
    def click_available_subscriptions(self):
        WebDriverWait(self.selenium, 10).until(lambda s: s.find_element(*self._available_subscriptions_tab_locator).is_displayed())
        self.selenium.find_element(*self._available_subscriptions_tab_locator).click()
        
    def click_applied_subscriptions(self):
        self.jquery_wait()
        self.selenium.find_element(*self._applied_subscriptions_tab_locator).click()
    
    @property
    def is_filter_visible(self):
        return self.is_element_visible(*self._available_subscriptions_input_filter_locator)
    
    def find_sub_by_id(self, id):
        try:
            self.selenium.find_element(By.ID, id)
            return True
        except:
            raise Exception("Expecited subscription %s not visible" % id)

    def select_a_random_sub(self):
        self.jquery_wait()
        subs = self.selenium.find_elements(*self._subscriptions_locator)
        sub = subs[random.randint(0, len(subs)-1)]
        sub_id = sub.get_attribute('id')
        self.selenium.find_element(By.ID, sub_id).click()
        return sub_id
        
    def click_add_sub(self):
        add_button = self.selenium.find_element(*self._available_subscriptions_submit_locator)
        add_button.click()
               
    def activationkey(self, value):
        for activationkey in self.activationkeys:
            if value in activationkey.name:
                return activationkey
        raise Exception('ActivationKey not found: %s' % value)

    @property
    def activationkeys(self):
        return [self.ActivationKeys(self.testsetup, element) for element in self.selenium.find_elements(*self._activationkey_list_locator)]

    class ActivationKeys(Page):
        
        _name_locator = (By.CLASS_NAME, 'one-line-ellipsis')
        
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
