#!/usr/bin/env python


from unittestzero import Assert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from pages.locators import *

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
    
class Page(object):
    """
    Base class for all Pages; sets up the default page.
    
    :param base_url: url of the application.
    :param timeout: default is 10, can be overridden.
    :param project: Name of project to be tested (sam, headpin, cfse, katello)
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


    @property
    def is_the_current_page(self):
        """
        Returns True if page title matches expected page title.
        """
        myProject = BaseProductFactory.get(self.project)
        if myProject._page_title:
            WebDriverWait(self.selenium, 10).until(lambda s: self.selenium.title)
        Assert.equal(self.selenium.title, myProject._page_title,
                     "Expected page title: %s. Actual page title: %s" % (myProject._page_title, self.selenium.title))
        return True
    
    def jquery_wait(self, timeout=20):
        """
        For Active jQuery to complete, default timeout is 20 seconds.
        """
        WebDriverWait(self.selenium, timeout).until(lambda s: s.execute_script("return jQuery.active == 0"))
        
    @property
    def is_successful(self):
        """
        Returns True if test is successful resulting in the success notification locator being displayed.
        """
        self.selenium.implicitly_wait(4)
        return WebDriverWait(self.selenium, 6).until(lambda s: s.find_element(*success_notification_locator).is_displayed())
    
    @property
    def is_dialog_cleared(self):
        """
        Returns True if the success notification locator has cleared.
        """
        self.selenium.implicitly_wait(2)
        try:
            return WebDriverWait(self.selenium, 6).until_not(lambda s: s.find_element(*success_notification_locator).is_displayed())
        except Exception, e:
            return False
        finally:
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)
    
    @property
    def is_failed(self):
        """
        Returns True if the error notification locator is displayed.
        """
        self.selenium.implicitly_wait(4)
        try:
            return self.selenium.find_element(*error_notification_locator).is_displayed()
        except Exception, e:
            return False
        finally:
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)
        
    def get_url_current_page(self):
        """
        Returns the url of the current page.
        """
        return(self.selenium.current_url)
    
    def is_element_present(self, *locator):
        """
        Returns True if locator is present.
        """
        try:
            WebDriverWait(self.selenium, 5).until(lambda s: s.find_element(*locator))
            return True
        except Exception as e:
            return False
        
    
    def is_element_visible(self, *locator):
        """
        Returns True if locator is visible.
        """
        try:
            return WebDriverWait(self.selenium, 10).until(lambda s: s.find_element(*locator).is_displayed())
        except Exception as e:
            return False
    
    def is_element_editable(self, *locator):
        """
        Returns True if the element can be edited.
        """
        return WebDriverWait(self.selenium, 10).until(lambda s: s.find_element(*locator).is_enabled())
            
    def get_location(self, *locator):
        """
        Returns the location of locator.
        """
        try:
            return self.selenium.find_element(*locator).location
        except NoSuchElementException, ElementNotVisibleException:
            return False
        
    def click(self, *locator):
        """
        Executes a Left Mouse Click on locator.
        """
        WebDriverWait(self.selenium, 60).until(lambda s: s.find_element(*locator).is_displayed())
        click_locator = self.selenium.find_element(*locator)
        ActionChains(self.selenium).move_to_element(click_locator).\
            click().perform()
        self.jquery_wait()
    
    def send_text(self, text, *locator):
        """
        Sends text to locator, one character at a time.
        """
        input_locator = self.selenium.find_element(*locator)
        for c in text:
            input_locator.send_keys(c)
            
    def select(self, locatorid, value):
        """
        Selects options in locatorid by value.
        """
        Select(self.selenium.find_element_by_id(locatorid)).select_by_value(value)
                
    def return_to_previous_page(self):
        """
        Simulates a Back (Return to prior page).
        """
        self.selenium.back()
