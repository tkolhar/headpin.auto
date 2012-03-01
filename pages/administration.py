#!/usr/bin/env python

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from pages.base import Base
from pages.page import Page
import time

class AdministrationTab(Base):
    _admin_search_form_locator = (By.XPATH, "//form[@id='search_form']")
    _admin_search_input_locator = (By.XPATH, "//input[@id='search']")
    _admin_search_button_locator = (By.XPATH, "//button[@id='search_button']")
    _new_user_locator = (By.XPATH, "//a[@id='new']")
    
    _user_details_tab_locator = (By.XPATH, "//li[@id='details']")
    _user_roles_tab_locator = (By.XPATH, "//li[@id='roles']")
    _user_environments_tab_locator = (By.XPATH, "//li[@id='environment']")
    _user_select_result_locator = (By.ID, "select-result")
    
    _remove_user_locator = (By.CSS_SELECTOR, "a.remove_item")
    _confirmation_yes_locator = (By.XPATH, "//span[@class='ui-button-text'][text()='Yes']")
    _close_user_detail_locator = (By.CSS_SELECTOR, "a.close")
    
    _new_user_username_field_locator = (By.ID, "username_field")
    _new_user_password_field_locator = (By.ID, "password_field")
    _new_user_confirm_field_locator = (By.ID, "confirm_field")
    _new_user_email_field_locator = (By.ID, "email_field")
    _new_user_org_field_locator = (By.ID, "org_id_org_id")
    _new_user_save_user_locator = (By.ID, "save_user")
    _save_password_locator = (By.CSS_SELECTOR, "div#save_password.verify_password")
    
    _user_list_locator = (By.CSS_SELECTOR, "div.block")
    _user_block_active_locator = (By.CSS_SELECTOR, "div.block.active")
    _passwords_do_not_match_locator = (By.XPATH, "//div[@id='password_conflict'][text()='The passwords do not match']")
    
    def create_new_user(self, username=None, password=None, confirm=None, email=None, org=None, Env=None):
        new_user_link_locator = self.selenium.find_element(*self._new_user_locator)
        ActionChains(self.selenium).move_to_element(new_user_link_locator).\
            click().perform()
        
        user_name_locator = self.selenium.find_element(*self._new_user_username_field_locator)
        user_name_locator.send_keys(username)
        password_locator = self.selenium.find_element(*self._new_user_password_field_locator)
        password_locator.send_keys(password)
        confirm_locator = self.selenium.find_element(*self._new_user_confirm_field_locator)
        confirm_locator.send_keys(confirm)
        email_locator = self.selenium.find_element(*self._new_user_email_field_locator)
        email_locator.send_keys(email)
        
        save_button_locator = self.selenium.find_element(*self._new_user_save_user_locator)
        ActionChains(self.selenium).move_to_element(save_button_locator).\
            click().perform()

    def change_password(self, password, confirm=None):
        WebDriverWait(self.selenium, 30).until(lambda s: self.is_element_visible(*self._new_user_password_field_locator))
        
        change_password_field_locator = self.selenium.find_element(*self._new_user_password_field_locator)
        change_password_field_locator.send_keys(password)
        confirm_password_field_locator = self.selenium.find_element(*self._new_user_confirm_field_locator)
        
        if confirm == None:
            confirm_password_field_locator.send_keys(password)
        else:
            confirm_password_field_locator.send_keys(confirm)
            
        save_button_locator = self.selenium.find_element(*self._save_password_locator)
        ActionChains(self.selenium).move_to_element(save_button_locator).\
            click().perform()
    
    @property        
    def passwords_do_not_match_visible(self):
        return self.is_element_visible(*self._passwords_do_not_match_locator)
        
    def is_search_correct(self, criteria):
        WebDriverWait(self.selenium, 60).until(lambda s: self.is_element_visible(*self._user_list_locator))
        for user in self.users:
            if criteria not in user.name:
                raise Exception('%s does not match Search Criteria %s' % (user.name, criteria))
        return True
    
    @property
    def is_block_active(self):
        return self.is_element_present(*self._user_block_active_locator)
    
    def user(self, value):
        for user in self.users:
            if value in user.name:
                return user
        raise Exception('User not found: %s' % value)
    
    @property
    def users(self):
        return [self.Users(self.testsetup, element) for element in self.selenium.find_elements(*self._user_list_locator)]
    
    class Users(Page):
        
        _name_locator = (By.CSS_SELECTOR, 'div.column_1.one-line-ellipsis')
        
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

class RolesTab(Base):
    
    _role_list_locator = (By.CSS_SELECTOR, "div.block")
    _role_original_title_locator = (By.XPATH, "//span[@original-title='%s']")
    _role_permissions_locator = (By.ID, "role_permissions")
    _role_users_locator = (By.ID, "role_users")
    _role_customize_window_locator = (By.CSS_SELECTOR, "div.slider_one.slider.will_have_content.has_content")
    _tree_breadcrumb_locator = (By.CSS_SELECTOR, "div.tree_breadcrumb")
    _roles_role_breadcrumb_locator = (By.CSS_SELECTOR, "span#roles.currentCrumb.one-line-ellipsis")
    _role_user_list_locator = (By.CSS_SELECTOR, "li.no_slide")
    _role_user_remove_locator = (By.CSS_SELECTOR, "a.fr.content_add_remove.remove_user.st_button")
    _role_new_name_locator = (By.ID, "role_name")
    _role_new_description_locator = (By.ID, "role_description")
    _role_save_button_locator = (By.ID, "role_save")

    @property
    def is_permissions_visible(self):
        return WebDriverWait(self.selenium, 20).until(lambda s: s.find_element(*self._role_permissions_locator).is_displayed())
    
    @property
    def is_users_visible(self):
        return WebDriverWait(self.selenium, 20).until(lambda s: s.find_element(*self._role_users_locator).is_displayed())
    
    def click_role_permissions(self):
        click_locator = self.selenium.find_element(*self._role_permissions_locator)
        ActionChains(self.selenium).move_to_element(click_locator).\
            click().perform()
            
    def click_role_users(self):
        click_locator = self.selenium.find_element(*self._role_users_locator)
        ActionChains(self.selenium).move_to_element(click_locator).\
            click().perform()
            
    @property
    def is_remove_visible(self):
        return self.selenium.find_element(*self._role_user_remove_locator).is_displayed()
    
    @property        
    def get_breadcrumb_role_name(self):
        return self.selenium.find_element(*self._roles_role_breadcrumb_locator).text
    
    def create_new_role(self, name, desc="Role Created by QE Automations"):
        input_locator = self.selenium.find_element(*self._role_new_name_locator)
        for c in name:
            input_locator.send_keys(c)
            
        input_locator = self.selenium.find_element(*self._role_new_description_locator)
        for c in desc:
            input_locator.send_keys(c)
    
    def save_role(self):
        self.selenium.find_element(*self._role_save_button_locator).click()
        
    def role(self, value):
        for role in self.roles:
            if value in role.name:
                return role
        raise Exception('Role not found: %s' % value)
    
    @property
    def roles(self):
        return [self.Roles(self.testsetup, element) for element in self.selenium.find_elements(*self._role_list_locator)]
    
    def role_user(self, value):
        for role_user in self.role_users:
            if value in role_user.name:
                return role_user
        raise Exception('User not found: %s' % value)
    
    @property
    def role_users(self):
        return [self.RoleUsers(self.testsetup, element) for element in self.selenium.find_elements(*self._role_user_list_locator)]
    
    class Roles(Page):
        
        _name_locator = (By.CSS_SELECTOR, 'div.column_1')
        
        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        @property
        def name(self):
            name_text = self._root_element.find_element(*self._name_locator).text
            return name_text
        
        @property
        def is_displayed(self):
            return self.selenium.find_element(*self._name_locator).is_displayed()
        
        def click(self):
            self._root_element.find_element(*self._name_locator).click()
            
    class RoleUsers(Page):
        
        _name_locator = (By.CSS_SELECTOR, "span.sort_attr")
        _add_locator = (By.CSS_SELECTOR, "a.fr.content_add_remove.add_user.st_button")
        
        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        @property
        def name(self):
            name_text = self._root_element.find_element(*self._name_locator).text
            return name_text
        
        @property
        def is_displayed(self):
            return self.selenium.find_element(*self._name_locator).is_displayed()
        
        def add_user(self):
            self._root_element.find_element(*self._add_locator).click()