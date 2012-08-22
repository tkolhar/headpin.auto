#!/usr/bin/env python

import pytest
from unittestzero import Assert
from pages.aeolus.home import Home
from pages.aeolus.aeolus_page import Aeolus
import time

class TestAeolus():

    @pytest.mark.demo
    def test_login_and_nav(self, mozwebqa):
        '''
        Login and nav to random pages
        '''
        home_page = Home(mozwebqa)
        home_page.login()

        page = Aeolus(mozwebqa)
        workflow = ['users', 'providers', 'permissions', 'pool_families', 'logout']
        for view in workflow:
            page.go_to_page_view(view)
        time.sleep(1)
