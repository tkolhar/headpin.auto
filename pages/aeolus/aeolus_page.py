#!/usr/bin/env python

from pages.base import Base
from pages.aeolus.locators import *
import time

class Aeolus(Base):

    def login(self, user, password):
        '''
        login
        '''
        # consider using send_characters if reliability is an issue
        self.send_text(user, *username_text_field)
        self.send_text(password, *password_text_field)
        self.selenium.find_element(*login_locator).click()

    def create_user(self, user):
        '''
        create user from dictionary
        '''
        self.go_to_page_view("users/new")
        self.send_text(user["fname"], *user_first_name_field)
        self.send_text(user["lname"], *user_last_name_field)
        self.send_text(user["email"], *user_email_field)
        self.send_text(user["username"], *user_username_field)
        self.send_text(user["passwd"], *user_password_field)
        self.send_text(user["passwd"], *user_password_confirmation_field)
        self.send_text(user["max_instances"], *user_quota_max_running_instances_field)
        self.selenium.find_element(*user_submit_locator).click()

    def delete_user(self, username):
        '''
        delete user
        '''
        self.go_to_page_view("users")
        self.click_by_text("a", username)
        self.selenium.find_element(*user_delete_locator).click()
        alert = self.selenium.switch_to_alert()
        alert.accept()

    def create_user_group(self, user_group):
        '''
        create user group from dictionary
        '''
        self.go_to_page_view("user_groups/new")
        self.send_text(user_group["name"], *user_group_name_field)
        self.send_text(user_group["description"], *user_group_description_field)
        self.selenium.find_element(*user_group_submit_locator).click()

    def delete_user_group(self, name):
        '''
        delete user group
        '''
        self.go_to_page_view("user_groups")
        self.click_by_text("a", name)
        self.selenium.find_element(*user_group_delete_locator).click()
        alert = self.selenium.switch_to_alert()
        alert.accept()

    def create_provider_account(self, acct):
        '''
        create provider account
        '''
        self.go_to_page_view("providers")
        self.click_by_text("a", acct['provider_name'])
        self.selenium.find_element(*prov_acct_details_locator).click()
        self.selenium.find_element(*prov_acct_new_account_field).click()
        self.send_text(acct["provider_account_name"], *prov_acct_name_field)
        self.send_text(acct["access_key"], *prov_acct_access_key_field)
        self.send_text(acct["secret_access_key"], *prov_acct_secret_access_key_field)
        self.send_text(acct["account_number"], *prov_acct_number_field)
        self.selenium.find_element(*prov_acct_key_locator).click()
        # OS dialog box
        #self.selenium.send_keys(acct["key_file"])
        self.selenium.find_element(*prov_acct_cert_locator).click()
        # OS dialog box
        #self.selenium.send_keys(acct["key_cert_file"])
        self.send_text(acct["priority"], *prov_acct_prior_field)
        self.send_text(acct["quota"], *prov_acct_quota_field)
        self.selenium.find_element(*prov_acct_save_locator).click()
        # success: div#notice flash-group/div#flash-subset
                   # "Provider Account updated!"
        # failure: div#error flash-group/div#flash-subset
                   # "Provider Account wasn't updated!"

    def delete_provider_account(self, acct):
        '''
        delete provider account
        '''
        self.go_to_page_view("providers")
        self.click_by_text("a", acct['provider_name'])
        self.selenium.find_element(*prov_acct_details_locator).click()
        self.click_by_text("a", acct['provider_account_name'])
        self.click_by_text("a", "Edit")
        self.click_by_text("a", "Delete Account")
        alert = self.selenium.switch_to_alert()
        alert.accept()
        # success: div#notice flash-group/div#flash-subset/ul#flashes
        # "Provider account was deleted!"

    def connection_test_provider_account(self, acct):
        '''
        test provider account connection
        '''
        self.go_to_page_view("providers")
        self.click_by_text("a", acct['provider_name'])
        self.selenium.find_element(*prov_acct_details_locator).click()
        self.click_by_text("a", acct['provider_account_name'])
        self.click_by_text("a", "Test Connection")
        # success: div#notice flash-group/div#flash-subset/ul#flashes
                   # "Test Connection Success: Valid Account Details"

    def connection_test_provider(self, acct):
        '''
        test provider connection
        '''
        self.go_to_page_view("providers")
        self.click_by_text("a", acct['provider_name'])
        self.click_by_text("a", "Test Connection")
        # success: div#notice flash-group/div#flash-subset/ul#flashes
                   # "Successfully Connected to Provider"

