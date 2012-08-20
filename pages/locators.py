#!/usr/bin/env python

from selenium.webdriver.common.by import By

"""
Locators for all pages are contained within.
"""
# Home Page and login related locators
username_text_field = (By.CSS_SELECTOR, "input#username.username")
password_text_field = (By.CSS_SELECTOR, "input#password-input.password")
login_locator = (By.CSS_SELECTOR, "input#login_btn.button.fr")
switcher_button = (By.CSS_SELECTOR, "a#switcherButton")
logout_locator = (By.XPATH, "//a[normalize-space(.)='Logout']")
# Dashboard locators
dashboard_dropbutton_locator = (By.XPATH, "//div[contains(@class, 'dropbutton')]")
dashboard_subscriptions_locator = (By.XPATH, "//div[@id='dashboard_subscriptions']")
dashboard_nofications_locator = (By.XPATH, "//div[@id='dashboard_notifications']")
# Tabs
dashboard_tab = (By.ID, "dashboard")
content_tab = (By.ID, "content")
providers_tab = (By.XPATH, "//a[.='Content Providers']")
systems_tab = (By.ID, "systems")
systems_all_tab = (By.ID, "registered") 
systems_by_environment_tab = (By.ID, "env") 
activation_keys_tab = (By.XPATH, "//a[.='Activation Keys']")
administer_tab = (By.ID, "admin")
#
#
account_controller_locator = (By.CSS_SELECTOR, "li.hello")
org_switcher_locator = (By.ID, "switcherButton")
org_switcher_org_locator = (By.CSS_SELECTOR, "a[href*='org_id=2']")
org_input_filter_locator = (By.CSS_SELECTOR, "input#orgfilter_input")
org_filtered_button_locator = (By.CSS_SELECTOR, "button.filter_button")
switcher_org_list_locator = (By.CSS_SELECTOR, "a.fl.clear")
dashboard_tab_active_locator = (By.CSS_SELECTOR, "li#dashboard.dashboard.top_level.active.selected")
dashboard_subscriptions_locator = (By.ID, "dashboard_subscriptions")
role_list_locator = (By.CSS_SELECTOR, "div.block")
role_original_title_locator = (By.XPATH, "//span[@original-title='%s']")
role_permissions_locator = (By.ID, "role_permissions")
role_users_locator = (By.ID, "role_users")
role_customize_window_locator = (By.CSS_SELECTOR, "div.slider_one.slider.will_have_content.has_content")
tree_breadcrumb_locator = (By.CSS_SELECTOR, "div.tree_breadcrumb")
roles_role_breadcrumb_locator = (By.CSS_SELECTOR, "span#roles.currentCrumb.one-line-ellipsis")
role_user_list_locator = (By.CSS_SELECTOR, "li.no_slide")
role_user_remove_locator = (By.CSS_SELECTOR, "a.fr.content_add_remove.remove_user.st_button")
role_new_name_locator = (By.ID, "role_name")
role_new_description_locator = (By.ID, "role_description")
role_save_button_locator = (By.ID, "role_save")
role_orgs_list_locator = (By.CSS_SELECTOR, "ul.filterable li.slide_link")
roles_add_permission_locator = (By.ID, "add_permission")
roles_resource_type_locator = (By.ID, "resource_type")
roles_permission_name_locator = (By.ID, "permission_name")
roles_permission_done_locator = (By.ID, "save_permission_button")
roles_permission_desc_locator = (By.ID, "description")
roles_locator = (By.CSS_SELECTOR, "span#roles.one-line-ellipsis")
current_page_locator = (By.CSS_SELECTOR, ".paginator .num > a:nth-child(1)")
redhat_logo_link_locator = (By.CSS_SELECTOR, "#head header a")
sam_header_locator = (By.CSS_SELECTOR, "#head header h1")
success_notification_locator = (By.CSS_SELECTOR, "div.jnotify-notification.jnotify-notification-success")
error_notification_locator = (By.CSS_SELECTOR, "div.jnotify-notification.jnotify-notification-error")
sam_h1_locator = (By.CSS_SELECTOR, "h1")
hello_link_locator = (By.XPATH, "//a[contains(@href, '/users?id=')]")
search_form_locator = (By.XPATH, "//form[@id='search_form']")
search_input_locator = (By.XPATH, "//input[@id='search']")
search_button_locator = (By.XPATH, "//button[@id='search_button']")
footer_version_text_locator = (By.CSS_SELECTOR, "div.grid_16.ca.light_text")
new_item_locator = (By.ID, "new")
remove_item_locator = (By.CSS_SELECTOR, "a.remove_item")
close_item_locator = (By.CSS_SELECTOR, "a.close")
confirmation_yes_locator = (By.XPATH, "//span[@class='ui-button-text'][text()='Yes']")
next_button_locator = (By.ID, "next_button")
activation_key_new_name_locator = (By.ID, "activation_key_name")
organization_new_name_locator = (By.ID, "new")
close_locator = (By.CLASS_NAME, "close")
login_org_name_selector_css = ('a')
login_org_selector = (By.CSS_SELECTOR, "a.fl")
login_org_dropdown = (By.CSS_SELECTOR, "div.one-line-ellipsis")
admin_drop_down = (By.ID, "admin")

"""
Tabs
"""
tab_elements = {"dashboard_tab" : (By.ID, "dashboard"),
                    "content_tab" : (By.ID, "content"),
                    "providers_tab" : (By.XPATH, "//a[.='Content Providers']"),
                    "systems_tab" : (By.ID, "systems"),
                    "systems_all_tab" : (By.ID, "registered"), 
                    "systems_by_environment_tab" : (By.ID, "env") ,
                    "activation_keys_tab" : (By.XPATH, "//a[.='Activation Keys']"),
                    "roles_tab" : (By.ID, "roles"),}
