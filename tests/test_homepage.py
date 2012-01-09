#!/usr/bin/env python 

import pytest
from unittestzero import Assert
import xmlrunner
import sys
from pages.home import Home

xfail = pytest.mark.xfail
nondestructive = pytest.mark.nondestructive

class TestHome:
        
    def test_Title(self):
        home_page = Home(self.base_url)
        
    @nondestructive  
    def tearDown(self):
        self.driver.close()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../junitreport'))
