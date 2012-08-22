#!/usr/bin/env python

from pages.base import Base
#from pages.page import Page
from pages.aeolus.locators import *
import time

class Aeolus(Base):

    @property
    def header_text(self):
        return self.selenium.find_element(*header_locator).text

    def login(self, user, password):
        '''
        login
        '''
        # consider using send_characters if reliability is an issue
        self.send_text(user, *username_text_field)
        self.send_text(password, *password_text_field)
        self.selenium.find_element(*login_locator).click()


