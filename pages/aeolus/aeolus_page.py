#!/usr/bin/env python

from pages.base import Base
from pages.aeolus.locators import *
import time

class Aeolus(Base):

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
        self.send_text(acct["username_access_key"], *prov_acct_access_key_field)
        self.send_text(acct["password_secret_access_key"], *prov_acct_secret_access_key_field)
        if acct["type"] == "ec2":
            self.send_text(acct["account_number"], *prov_acct_number_field)
            self.selenium.find_element(*prov_acct_key_file_locator).click()
            # OS dialog box -- TODO: manual step
            #self.selenium.send_keys(acct["key_file"])
            self.selenium.find_element(*prov_acct_cert_file_locator).click()
            # OS dialog box -- TODO: manual step
            #self.selenium.send_keys(acct["key_cert_file"])
        self.send_text(acct["provider_account_priority"], *prov_acct_prior_field)
        self.send_text(acct["provider_account_quota"], *prov_acct_quota_field)
        self.selenium.find_element(*prov_acct_save_locator).click()
        # return
        # success: "Provider Account updated!"
        # failure: "Provider Account wasn't updated!"

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
        # return success: "Provider account was deleted!"

    def connection_test_provider_account(self, acct):
        '''
        test provider account connection
        '''
        self.go_to_page_view("providers")
        self.click_by_text("a", acct['provider_name'])
        self.selenium.find_element(*prov_acct_details_locator).click()
        self.click_by_text("a", acct['provider_account_name'])
        self.click_by_text("a", "Test Connection")
        # return success: "Test Connection Success: Valid Account Details"

    def connection_test_provider(self, acct):
        '''
        test provider connection
        '''
        self.go_to_page_view("providers")
        self.click_by_text("a", acct['provider_name'])
        self.click_by_text("a", "Test Connection")
        # return success: "Successfully Connected to Provider"

