#!/usr/bin/env python

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.page import Page
from pages.page import BaseProductFactory
import string
import random

# common locators
from pages.locators import *
from pages.katello.locators import *

###
#
# Defines test helper methods common for all sites
# Page-specific methods belong in individual pages
#
###

class Base(Page):
    """
    Tasks that are reusable through out the test suite are defined within.
    """
    @property
    def header(self):
        return Base.HeaderRegion(self.testsetup)

    def random_string(self):
        """
        Generates a random *alphanumeric* string between 4 and 6 characters
        in length.
        """
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for x in range(random.randint(4, 6)))

    @property
    def page_title(self):
        """
        Returns the page's title.
        """
        WebDriverWait(self.selenium, 20).until(lambda s: self.selenium.title)
        return self.selenium.title

    @property
    def redhat_logo_title(self):
        """
        Returns the title attribute for the Red Hat logo.
        """
        return self.selenium.find_element(*redhat_logo_link_locator).get_attribute('title')
    
    def enter_search_criteria(self, criteria):
        """
        Search for criteria
        :param criteria: string
        """
        self.send_text_and_wait(criteria + "\n", *search_input_locator)
###
#
# from page.py
#
###
    def click(self, *locator):
        """
        Executes a Left Mouse Click on locator.
        """
        WebDriverWait(self.selenium, 60).until(lambda s: s.find_element(*locator).is_displayed())
        click_locator = self.selenium.find_element(*locator)
        ActionChains(self.selenium).move_to_element(click_locator).\
            click().perform()
        
    def click_and_wait(self, *locator):
        self.click(*locator)
        self.jquery_wait()
        
    def click_by_text(self, css, name):
        _text_locator = (By.XPATH, "//%s[text() = '%s']" % (css, name))
        self.selenium.find_element(*_text_locator).click()
    
    def send_characters(self, text, *locator):
        WebDriverWait(self.selenium, 60).until(lambda s: s.find_element(*locator).is_enabled())
        input_locator = self.selenium.find_element(*locator)
        for c in text:
            input_locator.send_keys(c)
            
    def send_text(self, text, *locator):
        """
        Sends text to locator, one character at a time.
        """
        WebDriverWait(self.selenium, 60).until(lambda s: s.find_element(*locator).is_enabled())
        input_locator = self.selenium.find_element(*locator)
        input_locator.send_keys(text)
        
    def send_text_and_wait(self, text, *locator):
        self.send_text(text, *locator)
        self.jquery_wait()
            
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
        
    def mouse_to_element(self, *locator):
        WebDriverWait(self.selenium, 60).until(lambda s: s.find_element(*locator).is_displayed())
        element = self.selenium.find_element(*locator)
        ActionChains(self.selenium).move_to_element(element).perform()

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

###
#
# end from page.py
#
###

    # basic nav
    def go_to_home_page(self):
        # from --baseurl= arg
        self.selenium.get(self.base_url)

    def go_to_url(self, url):
        # pass in url
        self.selenium.get(url)
    def go_to_page_view(self, view):
        # pass in view, e.g. system for katello/system
        self.selenium.get(self.base_url + "/" + view)

    # click functions
    def click_next(self):
        """
        Click the *Next* button.
        """
        self.click(*next_button_locator)
        
    def click_close(self):
        """
        Click the *Close* button.
        """
        self.click(*close_item_locator)
        
    def click_remove(self):
        """
        Click on *Remove item* locator.
        """
        self.click(*remove_item_locator)

    def click_new(self):
        """
        Click on the *New item* locator.
        """
        self.click(*new_item_locator)
            
    def click_confirm(self):
        """
        Click on the *Confirm* locator.
        """
        self.click(*confirmation_yes_locator)
        
    def click_tab(self, tab):
        """
        Execute a left mouse click on `tab`.
        :param tab: str tab to click
        """
        self.click_and_wait(*tab_elements[tab])
    '''
    @property
    def redhat_logo_image_source(self):
        """
        Returns the src attribute for the Red Hat Logo image locator.
        """
        return self.selenium.find_element(*self._amo_logo_image_locator).get_attribute('src')
    '''
    # UI elements    
    def is_footer_version_text_visible(self):
        """
        Return True if the Footer version Text is visible.
        """
        return self.selenium.find_element(*footer_version_text_locator).text
    
    @property
    def is_redhat_logo_visible(self):
        """
        Return True if the appropriate logo is visible. ::
        
            This is dependent on the project name passed at runtime.
        """
        myProject = BaseProductFactory.get(self.project)
        if myProject._logo_locator:
            return self.is_element_visible(*myProject._logo_locator)
      
    def click_redhat_logo(self):
        """
        Will execute a left mouse click on the Logo locator.
        """
        self.click(*redhat_logo_link_locator)
        
    
    #def click_hello_link(self):
        """
        Will execute a left mouse click on the user name locator
        that appears after a user is logged in, also referred to as the
        hello link.
        """
        #self.click(*hello_link_locator)
    
    @property
    def is_sam_h1_visible(self):
        """
        Return True if the `<h1/>` Header is vibable.
        """
        return self.is_element_visible(*sam_h1_locator)
    
    def click_sam_h1(self):
        """
        Execute a left mouse click on the `<h1/>` header locator.
        """
        try:
            self.selenium.find_element(*sam_h1_locator).click()
            return True
        except:
            raise ("The header element should be visible, it's not, do something!") 
    
    @property
    def get_location_sam_h1(self):
        """
        Return the location of the `<h1/>` element.
        """
        return self.get_location(*sam_h1_locator)

    @property
    def current_page(self):
        """
        Return the text attribute of the current page.
        """
        return int(self.selenium.find_element(*current_page_locator).text)
    
    def is_activation_key_name_editable(self):
        """
        Returns True if the activation key name field is editable.
        """
        try:
            self.click(*tab_elements['systems_tab'])
            self.click(*new_item_locator)
        except Exception, e:
            return False
        return self.is_element_editable(*activation_key_new_name_locator)

    def is_system_tab_visible(self):
        """
        Returns True if the system tab is visible.
        """
        return self.is_element_visible(*tab_elements['systems_tab'])
    
    def is_organizations_tab_visible(self):
        """
        Returns True if organizations tab is displayed.
        """
        return self.is_element_visible(*tab_elements['organizations_tab'])
    
    def is_new_organization_visible(self):
        """
        Return True if the New Organization element is available on the
        organizations tab.
        """
        try:
            self.click(*tab_elements['organizations_tab'])
        except Exception, e:
            return False
        return self.is_element_visible(*new_item_locator)
    
    def is_new_organization_name_field_editable(self):
        """
        Return True if the New Organization name field is editable.
        """
        try:
            self.click(*tab_elements['organizations_tab'])
            self.click(*new_item_locator)
        except Exception, e:
            return False
        return self.is_element_editable(*organization_new_name_locator)
    
    def is_dashboard_subs_visible(self):
        """
        Return True if the Subscription Status window is visible on the Dashboard.
        """
        try:
            self.click(*tab_elements['dashboard_tab'])
        except Exception, e:
            return False
        return self.is_element_visible(*dashboard_subscriptions_locator)
    
    def is_new_key_visible(self):
        """
        Return True if the New Key element is available on the systems tab.
        """
        try:
            self.click(*tab_elements['systems_tab'])
        except Exception, e:
            return False
        return self.is_element_visible(*new_item_locator)

    def select_org(self, value):
        """
        Select an org from the available orgs.
        :param value: The org to look for, by text.
        """
        self.click(*login_org_dropdown)
        for org in self.selectable_orgs():
            if value in org.name:
                return org
        raise Exception('Organization not found: %s' % value)
    
    def selectable_orgs(self):
        """
        Iterate over the available orgs in the login org selector.
        """
        return [self.LoginOrgSelector(self.testsetup, element) 
                for element in self.selenium.find_elements(*login_org_selector)]
    
    class LoginOrgSelector(Page):
        _name_locator = (By.CSS_SELECTOR, 'a.fl.clear')
        
        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element
            
        @property
        def name(self):
            name_text = self._root_element.find_element(*self._name_locator).text
            return name_text
        
        @property
        def is_displayed(self):
            return self.is_element_visible(*self._name_locator)
        
        def click(self):
            self._root_element.find_element(*self._name_locator).click()
            
    class HeaderRegion(Page):
        """
        Define actions specific to the *Header* Region of the page.
        """
        
        def click_logout(self):
            """
            Execute a left mouse click on the logout element.
            """
            self.click(*logout_locator)

        @property
        def is_user_logged_in(self):
            """
            Return True if evidence exists that the user is logged in.
            """
            return self.is_element_visible(*account_controller_locator)
        
        def click_hello(self):
            """
            Execute a left mouse click on the hello link locator.
            """
            self.click(*account_controller_locator)
        
        def click_switcher(self):
            """
            Click the org switcher.
            """
            self.click(*org_switcher_locator)
        
        def click_org_from_switcher(self):
            """
            Execute a left mouse click on an org from the org switcher.
            """
            WebDriverWait(self.selenium, 20).until(lambda s: s.find_element(*org_switcher_org_locator).is_displayed())
            self.selenium.find_element(*org_switcher_org_locator).click()
        
        @property
        def get_text_from_switcher(self):
            """
            Returns the current text from the org switcher.
            """
            return self.selenium.find_element(*org_switcher_locator).text 
        
        def filter_org_in_switcher(self, criteria):
            """
            Filter the org out of the switcher that you wish to use.
            """
            self.send_text(criteria, *org_input_filter_locator)
            
        def click_filtered_result(self, criteria):
            """
            Execute a left mouse click on the filtered org.
            """
            _org_filtered_result_locator = (By.XPATH, "//a[contains(text(), '" + criteria + "')]")
            self.selenium.find_element(*_org_filtered_result_locator).click()
        
        def select_a_random_switcher_org(self):
            """
            Select a random org from the org switcher.
            """
            orgs = self.selenium.find_elements(*switcher_org_list_locator)
            org = orgs[random.randint(0, len(orgs)-1)]
            org.click()
            
        @property
        def is_dashboard_selected(self):
            """
            Return True if the dashboard tab is active and displayed.
            """
            return self.selenium.find_element(*dashboard_tab_active_locator).is_displayed()

            
