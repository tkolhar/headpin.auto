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
    
    def enter_manifest(self,manifest_file_location="/var/tmp/sam_manifest_1.zip"):
        manifest_location = self.selenium.find_element(*self._input_provider_manifest_locator)
        manifest_location.send_keys(manifest_file_location)
        upload_locator = self.selenium.find_element(*self._provider_manifest_upload_locator)
        ActionChains(self.selenium).move_to_element(upload_locator).\
            click().perform()
        time.sleep(10)
     
    @property    
    def get_content_table_text(self):
        return self.selenium.find_element(*self._content_table_content_locator).text
        