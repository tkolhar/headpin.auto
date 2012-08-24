#!/usr/bin/env python

from unittestzero import Assert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
import time

###
#
# Used to setup page. File should rarely change.
# Test helper methods belong in base.py
#
###

class EnvironmentNotSetException(Exception):
    """
    Returns an Exception for Environment Not Set.
    """
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
    
class ElementNotFound(Exception):
    """
    Returns an Exception for Element Not Found.
    """
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
  
class BaseProductFactory(object):
    """
    Factory for supported products
    """
    @classmethod
    def get(self, project):
        """
        Get the project class by project
        returns projectClass.
        """
        projectClass = None
        if project == "sam":
            projectClass = SamProduct()
        if project == "headpin":
            projectClass = HeadpinProduct()
        if project == "katello":
            projectClass = KatelloProduct()
        if project == "aeolus":
            projectClass = AeolusProduct()
        return projectClass

class BaseProduct(object):
    """
    Base class for all Products
    """
    def __init__(self):
        """
        Default values for all products; likely won't be used
        as we focus on the differences.
        """
        pass
   
class SamProduct(BaseProduct):
    """
    Elements that are specific to SAM.
    """
    _page_title = "Subscription Asset Manager - Subscription Management"
    _logo_locator = (By.XPATH, "//img[contains(@src, 'rh-logo.png')]")
    _footer = "Subscription Asset Manager Version:"
    
class HeadpinProduct(BaseProduct):
    """
    Elements specific to Headpin.
    """
    _page_title = "Headpin - Open Source Subscription Management"
    _logo_locator = (By.XPATH, "//img[contains(@src, 'logo.png')]")
    
class KatelloProduct(BaseProduct):
    """
    Elements specific to Katello
    """
    _page_title = "Katello - Open Source Systems Management"
    _logo_locator = (By.XPATH, "//img[contains(@src, 'logo.png')]")
    #print "importing katello locators..................."
    #from pages.katello import locators as loc

class AeolusProduct(BaseProduct):
    """
    Elements specific to Katello
    """
    #_page_title = "Katello - Open Source Systems Management"
    #_logo_locator = (By.XPATH, "//img[contains(@src, 'logo.png')]")
    #from pages.aeolus import locators as loc
    
class Page(object):
    """
    Base class for all Pages; sets up the default page.
    
    :param base_url: url of the application.
    :param timeout: default is 10, can be overridden.
    :param project: Name of project to be tested (sam, headpin, cfse, katello)
    :param org: org selector for katello
    """
    def __init__(self, testsetup):
        '''
        Constructor
        '''
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout
        self.project = testsetup.project
        self.org = testsetup.org

