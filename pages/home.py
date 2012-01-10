#!/usr/bin/env python

from selenium.webdriver.common.by import By

from pages.page import Page
from pages.base import Base

class Home(Base):
    _page_title = "Subscription Asset Manager - Subscription Management"
    _username_text_field = (By.ID, "username")
    _password_text_field = (By.ID, "password")
    _login = (By.NAME, "commit")

    def __init__(self, testsetup, open_url=True):
        ''' Gets page ready for testing '''
        Base.__init__(self, testsetup)
        if open_url:
            print('Will get %s' % self.base_url)
            self.selenium.get(self.base_url)
        
