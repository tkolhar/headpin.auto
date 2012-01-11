#!/usr/bin/env python

from selenium.webdriver.common.by import By
from pages.base import Base

class Dashboard(Base):
    '''
    Test Features of the Dashboard
    '''
    _dashboard_dropbutton_locator = (By.XPATH, "//div[contains(@class, 'dropbutton')]")
    _dashboard_subscriptions_locator = (By.XPATH, "//div[@id='dashboard_subscriptions']")
    _dashboard_nofications_locator = (By.XPATH, "//div[@id='dashboard_notifications']")
    
    @property
    def is_dashboard_dropbutton_present(self):
        return self.is_element_present(*self._dashboard_dropbutton_locator)
    
    @property
    def is_dashboard_subscriptions_present(self):
        return self.is_element_present(*self._dashboard_subscriptions_locator)
    
    @property
    def is_dashboard_notificaitons_present(self):
        return self.is_element_present(*self._dashboard_nofications_locator)
    