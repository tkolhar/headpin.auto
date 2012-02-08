#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the redhat Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.redhat.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is redhat WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# redhat.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Bebe <florin.strugariu@softvision.ro>
#                 Alex Rodionov <p0deje@gmail.com>
#                 Teodosia Pop <teodosia.pop@softvision.ro>
#                 Alex Lakatos <alex@greensqr.com>
#                 Eric L Sammons <elsammons@gmail.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
#from pyvirtualdisplay import Display

from unittestzero import Assert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
import os


class Page(object):
    '''
    Base class for all Pages
    '''

    def __init__(self, testsetup):
        '''
        Constructor
        '''
        self.testsetup = testsetup
        testsetup.base_url = os.environ.get("HEADPIN_SERVER")
        self.base_url = testsetup.base_url
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout
        self.product = os.environ.get("PRODUCT")

    @property
    def is_the_current_page(self):
        if self.product == "SAM":
            if self._sam_page_title:
                WebDriverWait(self.selenium, 10).until(lambda s: self.selenium.title)
            Assert.equal(self.selenium.title, self._sam_page_title,
                         "Expected page title: %s. Actual page title: %s" % (self._sam_page_title, self.selenium.title))
        elif self.product == "HEADPIN":
            if self._headpin_page_title:
                WebDriverWait(self.selenium, 10).until(lambda s: self.selenium.title)
            Assert.equal(self.selenium.title, self._headpin_page_title,
                         "Expected page title: %s. Actual page title: %s" % (self._headpin_page_title, self.selenium.title))
        return True

    def get_url_current_page(self):
        return(self.selenium.current_url)

    def is_element_present(self, *locator):
        self.selenium.implicitly_wait(30)
        try:
            self.selenium.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)

    def is_element_visible(self, *locator):
        WebDriverWait(self.selenium, 10).until(lambda s: self.is_element_present(*locator))
        #self.selenium.implicitly_wait(30)
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except NoSuchElementException, ElementNotVisibleException:
            return False
        
    def get_location(self, *locator):
        try:
            return self.selenium.find_element(*locator).location
        except NoSuchElementException, ElementNotVisibleException:
            return False
        
    def return_to_previous_page(self):
        self.selenium.back()
