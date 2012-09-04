#!/usr/bin/env python

import pytest
#from unittestzero import Assert
from pages.aeolus.home import Home
from pages.aeolus.aeolus_page import Aeolus
from data.aeolus_data import Provider
import time
from pprint import pprint

class TestProvider():

    @pytest.mark.provider_admin
    @pytest.mark.aeolus_setup
    def test_provider_connection(self, mozwebqa):
        '''
        test provider connection
        '''
        home_page = Home(mozwebqa)
        assert home_page.login() == "Login successful!"

        page = Aeolus(mozwebqa)

        for account in Provider.accounts:
            assert page.connection_test_provider(account) == \
                   "Successfully Connected to Provider"

        assert page.logout() == "Aeolus Conductor | Login"

    @pytest.mark.provider_admin
    @pytest.mark.aeolus_setup
    def test_create_provider_account(self, mozwebqa):
        '''
        Create provider account and test provider account connection
        '''
        home_page = Home(mozwebqa)
        assert home_page.login() == "Login successful!"

        page = Aeolus(mozwebqa)

        # create provider account
        for account in Provider.accounts:
            if account["type"] == "ec2":
                account = page.update_ec2_acct_credentials_from_config(account)
            assert page.create_provider_account(account) == \
                   "Account %s was added." % account["provider_account_name"]

        # test provider account
        for account in Provider.accounts:
            assert page.connection_test_provider_account(account) == \
                   "Test Connection Success: Valid Account Details"

        # test cleanup
        if page.test_cleanup == True:
            for account in Provider.accounts:
                assert page.delete_provider_account(account) == \
                       "Provider account was deleted!"

        assert page.logout() == "Aeolus Conductor | Login"

