#!/usr/bin/env python


from unittestzero import Assert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
import os
import urlparse

class EnvironmentNotSetException(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
    
class ElementNotFound(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
  
class BaseProductFactory(object):
    '''
    Factory for products
    '''
    @classmethod
    def get(self, project):
        projectClass = None
        if project == "sam":
            projectClass = SamProduct()
        if project == "headpin":
            projectClass = HeadpinProduct()
        if project == "katello":
            projectClass = KatelloProduct()
        return projectClass

class BaseProduct(object):
    '''
    Base class for all Products
    '''
    def __init__(self):
        ''' do nothing '''
        pass
   
class SamProduct(BaseProduct):
    _page_title = "Subscription Asset Manager - Subscription Management"
    _logo_locator = (By.XPATH, "//img[contains(@src, '/sam/images/rh-logo.png')]")
    _footer = "Subscription Asset Manager Version:"
    
class HeadpinProduct(BaseProduct):
    _page_title = "Headpin - Open Source Subscription Management"
    _logo_locator = (By.XPATH, "//img[contains(@src, '/headpin/images/rh-logo.png')]")
    
class KatelloProduct(BaseProduct):
    _page_title = "Katello - Open Source Systems Management"
    _logo_locator = (By.XPATH, "//img[contains(@src, '/katello/images/logo.png')]")
    
class Page(object):
    '''
    Base class for all Pages
    '''
    def __init__(self, testsetup):
        '''
        Constructor
        '''
        self.testsetup = testsetup
        #if not os.environ.get("APP_SERVER"):
        #    raise EnvironmentNotSetException('APP_SERVER environment variable not set!')
            #sys.exit(-1)
        #testsetup.base_url = os.environ.get("APP_SERVER")
        self.base_url = testsetup.base_url
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout
        self.project = testsetup.project

    @property
    def is_the_current_page(self):
        myProject = BaseProductFactory.get(self.project)
        if myProject._page_title:
            WebDriverWait(self.selenium, 10).until(lambda s: self.selenium.title)
        Assert.equal(self.selenium.title, myProject._page_title,
                     "Expected page title: %s. Actual page title: %s" % (myProject._page_title, self.selenium.title))
        return True
    
    def jquery_wait(self, timeout=20):
        WebDriverWait(self.selenium, timeout).until(lambda s: s.execute_script("return jQuery.active == 0"))
        
    @property
    def is_successful(self):
        #self.jquery_wait()
        self.selenium.implicitly_wait(4)
        try:
            return self.selenium.find_element(*self._success_notification_locator).is_displayed()
        except Exception, e:
            return False
        finally:
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)
    
    @property
    def is_dialog_cleared(self):
        self.selenium.implicitly_wait(2)
        try:
            return WebDriverWait(self.selenium, 6).until_not(lambda s: s.find_element(*self._success_notification_locator).is_displayed())
        except Exception, e:
            return False
        finally:
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)
    
    @property
    def is_failed(self):
        #self.jquery_wait()
        self.selenium.implicitly_wait(4)
        try:
            return self.selenium.find_element(*self._error_notification_locator).is_displayed()
        except Exception, e:
            return False
        finally:
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)
        
    def get_url_current_page(self):
        return(self.selenium.current_url)
    
    def is_element_present(self, *locator):
        try:
            WebDriverWait(self.selenium, 5).until(lambda s: s.find_element(*locator))
            return True
        except Exception as e:
            return False
        
    
    def is_element_visible(self, *locator):
        try:
            return WebDriverWait(self.selenium, 10).until(lambda s: s.find_element(*locator).is_displayed())
        except Exception as e:
            return False
        
    def get_location(self, *locator):
        try:
            return self.selenium.find_element(*locator).location
        except NoSuchElementException, ElementNotVisibleException:
            return False
        
    def return_to_previous_page(self):
        self.selenium.back()
