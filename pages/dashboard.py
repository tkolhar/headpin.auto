#!/usr/bin/env python

from selenium.webdriver.common.by import By
from pages.base import Base
from pages.locators import *

class Dashboard(Base):
    """
    Test Features of the Dashboard
    """
    @property
    def is_dashboard_dropbutton_present(self):
        return self.is_element_present(*dashboard_dropbutton_locator)
    
    @property
    def is_dashboard_subscriptions_present(self):
        return self.is_element_present(*dashboard_subscriptions_locator)
    
    @property
    def is_dashboard_notificaitons_present(self):
        return self.is_element_present(*dashboard_nofications_locator)
    