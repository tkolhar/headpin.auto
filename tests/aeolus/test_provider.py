#!/usr/bin/env python

import pytest
from unittestzero import Assert
from pages.aeolus.home import Home
from pages.aeolus.aeolus_page import Aeolus
from data.aeolus_data import Provider
import time
from pprint import pprint

class TestProvider():

    @pytest.mark.provider_admin
    @pytest.mark.aeolus_setup
    def test_create_provider_account(self, mozwebqa):
        '''
        Create provider account and test provider account connection
        key and cert upload not currently supported.
        requires manual OS intervention
        '''
        home_page = Home(mozwebqa)
        home_page.login()

        page = Aeolus(mozwebqa)

        # create provider account
        for account in Provider.accounts:
            page.create_provider_account(account)
            # TODO: assert return
            time.sleep(5)

        # test provider account
        for account in Provider.accounts:
            page.connection_test_provider_account(account)
            # TODO: assert return
            time.sleep(5)

        # test cleanup
        if page.test_cleanup in ['True', 'true', '1']:
            for account in Provider.accounts:
                page.delete_provider_account(account)
                # TODO: assert return
                time.sleep(5)

    def test_provider_connection(self, mozwebqa):
        '''
        test provider connection
        '''
        home_page = Home(mozwebqa)
        home_page.login()

        page = Aeolus(mozwebqa)

        for account in Provider.accounts:
            page.connection_test_provider(account)
            # TODO: assert return
            time.sleep(5)
