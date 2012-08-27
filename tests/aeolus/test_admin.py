#!/usr/bin/env python

import pytest
from unittestzero import Assert
from pages.aeolus.home import Home
from pages.aeolus.aeolus_page import Aeolus
from data.aeolus_data import Admin
import time
from pprint import pprint

class TestAdmin():

    @pytest.mark.user_admin
    @pytest.mark.aeolus_setup
    def test_create_user(self, mozwebqa):
        '''
        Create users
        '''
        home_page = Home(mozwebqa)
        home_page.login()

        page = Aeolus(mozwebqa)

        for user in Admin.users:
            page.create_user(user)

        # test cleanup
        if page.test_cleanup in ['True', 'true', '1']:
            for user in Admin.users:
                page.delete_user(user["username"])

    @pytest.mark.user_admin
    @pytest.mark.aeolus_setup
    def test_create_user_groups(self, mozwebqa):
        '''
        create user groups
        '''
        home_page = Home(mozwebqa)
        home_page.login()

        page = Aeolus(mozwebqa)

        for user_group in Admin.user_groups:
            page.create_user_group(user_group)
            page.go_to_page_view("user_groups/new")

        # test cleanup
        if page.test_cleanup in ['True', 'true', '1']:
            for user_group in Admin.user_groups:
                page.delete_user_group(user_group["name"])

