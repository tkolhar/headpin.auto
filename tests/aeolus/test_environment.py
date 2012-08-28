#!/usr/bin/env python

import pytest
from unittestzero import Assert
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
        msg = home_page.login()
        assert msg == "Login successful!"

        page = Aeolus(mozwebqa)

        for environment in Environment.pool_family_environments:
            msg = page.new_environment(environment)
            assert msg == "Pool family was added."

        # test cleanup
        if page.test_cleanup in ['True', 'true', '1']:
            for environment in Environment.pool_family_environments:
                msg = page.delete_environment(environment)
                assert msg == "Pool Family was deleted!"

    def test_new_pool(self, mozwebqa):
        '''
        create new pools
        '''
        home_page = Home(mozwebqa)
        msg = home_page.login()
        assert msg == "Login successful!"

        page = Aeolus(mozwebqa)

        for pool in Environment.pools:
            msg = page.new_pool(pool)
            assert msg == "Pool added."

       # test cleanup
        if page.test_cleanup in ['True', 'true', '1']:
            for pool in Environment.pools:
                msg = page.delete_pool(pool)
                assert msg == "Pool %s was deleted." % pool["name"]

    def test_new_catalog(self, mozwebqa):
        '''
        create new catalogs
        '''
        home_page = Home(mozwebqa)
        msg = home_page.login()
        assert msg == "Login successful!"

        page = Aeolus(mozwebqa)

        for catalog in Environment.catalogs:
            msg = page.new_catalog(catalog)
            assert msg == "Catalog created!"

        # test cleanup
        if page.test_cleanup in ['True', 'true', '1']:
            for catalog in Environment.catalogs:
                msg = page.delete_catalog(catalog)
                assert msg == "Catalog deleted!"
