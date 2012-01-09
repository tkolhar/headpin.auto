#!/usr/bin/env python 

import pytest
import sys
from unittestzero import Assert

#sys.path.append('../')
from pages.home import Home

xfail = pytest.mark.xfail
nondestructive = pytest.mark.nondestructive

class TestHome:  
    
    @nondestructive
    def test_Title(self, mozwebqa):
        home_page = Home(mozwebqa)