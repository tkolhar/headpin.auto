#!/usr/bin/env python

from pages.base import Base
#from pages.page import Page
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
        self.go_to_page_view("user_groups")
        self.click_by_text("a", name)
        self.selenium.find_element(*user_group_delete_locator).click()
        alert = self.selenium.switch_to_alert()
        alert.accept()
