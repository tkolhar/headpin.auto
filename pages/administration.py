#!/usr/bin/env python

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.base import Base
from pages.page import Page
from pages.locators import *
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

    @property
    def is_permissions_visible(self):
        """
        In the Roles creation process are Permissions visible, Returns True or False.
        """
        return WebDriverWait(self.selenium, 20).until(lambda s: s.find_element(*role_permissions_locator).is_displayed())
    
    @property
    def is_users_visible(self):
        """
        In the Roles creation process, are users visible, Returns True or False.
        """
        return WebDriverWait(self.selenium, 20).until(lambda s: s.find_element(*role_users_locator).is_displayed())
    
    def click_role_permissions(self):
        """
        Click on the role permission locator.
        """
        self.click(*role_permissions_locator)
        time.sleep(4)
            
    def click_role_users(self):
        """
        Click on the role users locator.
        """
        self.click(*role_users_locator)
        time.sleep(4)
        
    def click_add_permission(self):
        """
        Click the add locator to add permission.
        """
        self.click(*roles_add_permission_locator)
    
    def enter_permission_name(self, text):
        """
        Enter the name of the permission.
        """
        self.send_text(text, *roles_permission_name_locator)
    
    def enter_permission_desc(self, text):
        """
        Enter a description for the permission.
        """
        self.send_text(text, *roles_permission_desc_locator)
        
    def select_resource_type(self, resource):
        """
        Select the reource type.
        """
        resource = resource.lower()
        self.select('resource_type', resource)
        
    def click_permission_done(self):
        """
        Click Done.
        """
        self.click(*roles_permission_done_locator)
        
    def click_root_roles(self):
        """
        Click the root locator for the role being created.
        """
        self.click(*roles_locator)
        time.sleep(4)
        
    @property
    def is_remove_visible(self):
        """
        Is the remove element visible, Returns True or False.
        """
        return self.selenium.find_element(*role_user_remove_locator).is_displayed()
    
    @property        
    def get_breadcrumb_role_name(self):
        """ 
        Returns the text attribute of the role.
        """
        return self.selenium.find_element(*roles_role_breadcrumb_locator).text
    
    def save_role(self):
        """
        Executes a left mouse click on the save role button locator.
        """
        self.click(*role_save_button_locator)
        
    def create_new_role(self, name, desc="Role Created by QE Automations"):
        """
        Creates a new role via the webui.
        """
        self.click(*new_item_locator)
        self.send_text(name, *role_new_name_locator)
        self.send_text(desc, *role_new_description_locator)
        self.save_role()

    def role(self, value):
        """
        Searches through the list of roles for role.name that contains value.
        Returns the role.
        """
        for role in self.roles:
            if value in role.name:
                return role
        raise Exception('Role not found: %s' % value)

    @property
    def roles(self):
        """
        Used to parse the list of elements in the roles table.
        """
        return [self.Roles(self.testsetup, element) for element in self.selenium.find_elements(*role_list_locator)]

    def role_user(self, value):
        """
        Searches through the list of users that can be applied to a role for role_user.name that
        contains value.
        Returns role_user.
        """
        for role_user in self.role_users:
            if value in role_user.name:
                return role_user
        raise Exception('User not found: %s' % value)
    
    @property
    def role_users(self):
        """
        Used to parse the list of elements in the role user table.
        """
        return [self.RoleUsers(self.testsetup, element) for element in self.selenium.find_elements(*role_user_list_locator)]
    
    def role_org(self, value):
        """
        Searches through a list of orgs applicable to a given role where role_org.name contains value.
        Returns role_org
        """
        for role_org in self.role_orgs:
            if value in role_org.name:
                return role_org
        raise Exception("Organization %s not found" % value)
    
    @property
    def role_orgs(self):
        """
        Used to parse the list of elements in the role org table.
        """
        return [self.RoleOrgs(self.testsetup, element) for element in self.selenium.find_elements(*role_orgs_list_locator)]
    
    class RoleOrgs(Page):
        """
        Process the Organizations available to a new role.
        """
        _role_org_name_locator = (By.CLASS_NAME, 'sort_attr')
        
        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        @property
        def name(self):
            """
            Returns the text for the organization sought.
            """
            name_text = self._root_element.find_element(*self._role_org_name_locator).text
            return name_text
        
        @property
        def is_displayed(self):
            """
            Returns True if desired organization is displayed.
            """
            return self.selenium.find_element(*self._role_org_name_locator).is_displayed()
        
        def click(self):
            """
            Executes a left mouse click on the element associated with the desired
            organization.
            """
            self._root_element.find_element(*self._role_org_name_locator).click()
            time.sleep(4)
            
    class Roles(Page):
        """
        Process the available Roles.
        """
        _role_name_locator = (By.CSS_SELECTOR, 'div.column_1')
        
        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        @property
        def name(self):
            """
            Returns the text for the Role sought.
            """
            name_text = self._root_element.find_element(*self._role_name_locator).text
            return name_text
        
        @property
        def is_displayed(self):
            """"
            Returns True if the desired role is displayed.
            """
            return self.selenium.find_element(*self._role_name_locator).is_displayed()
        
        def click(self):
            """
            Executes a left mouse click on the desired role.
            """
            self._root_element.find_element(*self._role_name_locator).click()
            time.sleep(4)
            
    class RoleUsers(Page):
        """
        Processes the list of users available to a given role.
        """
        
        _role_user_name_locator = (By.CLASS_NAME, 'sort_attr')
        _add_locator = (By.CSS_SELECTOR, "a.fr.content_add_remove.add_user.st_button")
        
        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        @property
        def name(self):
            """
            Returns the text of the user sought.
            """
            name_text = self._root_element.find_element(*self._role_user_name_locator).text
            return name_text
        
        @property
        def is_displayed(self):
            """
            Returns True if the desired User is displayed.
            """
            return self.selenium.find_element(*self._role_user_name_locator).is_displayed()
        
        def add_user(self):
            """
            Executes a left mouse click on the Add Element for the desired user.
            """
            self._root_element.find_element(*self._add_locator).click()
            time.sleep(4)