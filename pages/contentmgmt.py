#!/usr/bin/env python

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from pages.base import Base
from pages.page import Page
import time

class ContentManagementTab(Base):
    _cm_subscriptions_tab_locator = (By.CSS_SELECTOR, "a[href='#tabs-1']")
    _cm_import_history_tab_locator = (By.CSS_SELECTOR, "a[href='#tabs-3']")
    _input_provider_manifest_locator = (By.CSS_SELECTOR, "input#provider_contents")
    _provider_manifest_upload_locator = (By.CSS_SELECTOR, "a#upload_submit")
    _provider_manifest_force_locator = (By.CSS_SELECTOR, "input#force_import")
    _content_table_content_locator = (By.CSS_SELECTOR, "td")
    _cm_content_providers_tab_locator = (By.ID, "providers")
    _content_providers_list_locator = (By.CLASS_NAME, "third_level")
    _redhat_content_provider_locator = (By.XPATH, "//a[.='Red Hat Content Provider']")
    
    
    def click_content_providers(self):
        WebDriverWait(self.selenium, 10).until(lambda s: s.find_element(*self._cm_content_providers_tab_locator).is_displayed())
        self.selenium.find_element(*self._cm_content_providers_tab_locator).click()
        
    def select_redhat_content_provider(self):
        self.selenium.find_element(*self._redhat_content_provider_locator).click()
    
    def enter_manifest(self, manifest_file_location):
        self.send_text(manifest_file_location, *self._input_provider_manifest_locator)
        self.click(*self._provider_manifest_upload_locator)
        """
        manifest_location = self.selenium.find_element(*self._input_provider_manifest_locator)
        manifest_location.send_keys(manifest_file_location)
        upload_locator = self.selenium.find_element(*self._provider_manifest_upload_locator)
        ActionChains(self.selenium).move_to_element(upload_locator).\
            click().perform()
        """
     
    @property    
    def get_content_table_text(self):
        return self.selenium.find_element(*self._content_table_content_locator).text
    
    def click_force(self):
        self.selenium.find_element(*self._provider_manifest_force_locator).click()
        