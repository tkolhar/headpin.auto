#!/usr/bin/env python

from selenium.webdriver.common.by import By

"""
Locators for aeolus pages are contained within.
"""

# login
username_text_field = (By.NAME, "login")
password_text_field = (By.ID, "password-input")
login_locator = (By.NAME, "commit")

# new user fields
user_first_name_field = (By.ID, "user_first_name")
user_last_name_field = (By.ID, "user_last_name")
user_email_field = (By.ID, "user_email")
user_username_field = (By.ID, "user_login")
user_password_field = (By.ID, "user_password")
user_password_confirmation_field = (By.ID, "user_password_confirmation")
user_quota_max_running_instances_field = (By.ID, "user_quota_attributes_maximum_running_instances")
user_submit_locator = (By.ID, "user_submit")
user_delete_locator = (By.CSS_SELECTOR, "input.button.danger")

# new user group fields
user_group_name_field = (By.ID, "user_group_name")
user_group_description_field = (By.ID, "user_group_description")
user_group_submit_locator = (By.ID, "user_group_submit")
user_group_delete_locator = (By.ID, "delete")
