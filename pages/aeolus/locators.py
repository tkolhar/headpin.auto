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

# new provider account fields
prov_acct_details_locator = (By.ID, "details_accounts")
prov_acct_new_account_field = (By.ID, "new_provider_account")
prov_acct_name_field = (By.ID, "provider_account_label")
prov_acct_access_key_field = (By.ID, "provider_account_credentials_hash_username")
prov_acct_secret_access_key_field = (By.ID, "provider_account_credentials_hash_password")
prov_acct_number_field = (By.ID, "provider_account_credentials_hash_account_id")
prov_acct_key_file_locator = (By.ID, "provider_account_credentials_hash_x509private")
prov_acct_cert_file_locator = (By.ID, "provider_account_credentials_hash_x509public")
prov_acct_prior_field = (By.ID, "provider_account_priority")
prov_acct_quota_field = (By.ID, "quota_instances")
prov_acct_save_locator = (By.ID, "save")
prov_acct_delete_locator = (By.ID, "delete_button")

# confirmation flash message locators
success_confirmation_locator = (By.ID, "flashes")
fail_confirmation_locator = (By.ID, "flash-subset")
