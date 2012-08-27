#!/usr/bin/env python

import pytest
from unittestzero import Assert
from pages.aeolus.home import Home
from pages.aeolus.aeolus_page import Aeolus
from data.aeolus_data import Provider
import time
from pprint import pprint

# TODO: move hard-coded assert messages

class TestProvider():

    @pytest.mark.provider_admin
    @pytest.mark.aeolus_setup
    def test_provider_connection(self, mozwebqa):
        '''
        test provider connection
        '''
        home_page = Home(mozwebqa)
        msg = home_page.login()
        assert msg == "Login successful!"

        page = Aeolus(mozwebqa)

        for account in Provider.accounts:
            msg = page.connection_test_provider(account)
            assert msg == "Successfully Connected to Provider"

    @pytest.mark.provider_admin
    @pytest.mark.aeolus_setup
    def test_create_provider_account(self, mozwebqa):
        '''
        Create provider account and test provider account connection
        '''
        home_page = Home(mozwebqa)
        msg = home_page.login()
        assert msg == "Login successful!"

        page = Aeolus(mozwebqa)

        # create provider account
        for account in Provider.accounts:
            msg = page.create_provider_account(account)
            assert msg == "Provider Account updated!"

        # test provider account
        for account in Provider.accounts:
            msg = page.connection_test_provider_account(account)
            assert msg == "Test Connection Success: Valid Account Details"

        # test cleanup
        if page.test_cleanup in ['True', 'true', '1']:
            for account in Provider.accounts:
                msg = page.delete_provider_account(account)
                assert msg == "Provider account was deleted!"

