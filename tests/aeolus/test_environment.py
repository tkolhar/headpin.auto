#!/usr/bin/env python

import pytest
#from unittestzero import Assert
from pages.aeolus.home import Home
from pages.aeolus.aeolus_page import Aeolus
from data.aeolus_data import Environment
import time
from pprint import pprint

class TestEnvironment():

    @pytest.mark.environment
    @pytest.mark.aeolus_setup
    def test_new_environment_pool_family(self, mozwebqa):
        '''
        create new environments or pool families
        '''
        home_page = Home(mozwebqa)
        assert home_page.login() == "Login successful!"

        page = Aeolus(mozwebqa)

        for environment in Environment.pool_family_environments:
            assert page.new_environment(environment) == "Pool family was added."

        # test cleanup
        if page.test_cleanup == True:
            for environment in Environment.pool_family_environments:
                assert page.delete_environment(environment) == \
                       "Pool Family was deleted!"
        assert page.logout() == "Aeolus Conductor | Login"

    def test_new_pool(self, mozwebqa):
        '''
        create new pools
        '''
        home_page = Home(mozwebqa)
        assert home_page.login() == "Login successful!"

        page = Aeolus(mozwebqa)

        for pool in Environment.pools:
            assert page.new_pool(pool) == "Pool added."

       # test cleanup
        if page.test_cleanup == True:
            for pool in Environment.pools:
                assert page.delete_pool(pool) == \
                       "Pool %s was deleted." % pool["name"]

    def test_new_catalog(self, mozwebqa):
        '''
        create new catalogs
        '''
        home_page = Home(mozwebqa)
        assert home_page.login() == "Login successful!"

        page = Aeolus(mozwebqa)

        for catalog in Environment.catalogs:
            assert page.new_catalog(catalog) == "Catalog created!"

        # test cleanup
        if page.test_cleanup == True:
            for catalog in Environment.catalogs:
                assert page.delete_catalog(catalog) == "Catalog deleted!"

        assert page.logout() == "Aeolus Conductor | Login"

