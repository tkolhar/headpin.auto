#!/usr/bin/env python

import pytest
from unittestzero import Assert
from pages.aeolus.home import Home
from pages.aeolus.aeolus_page import Aeolus
from data.large_dataset import Admin
from data.assert_messages import *
import time
from pprint import pprint

class TestAdmin():

    @pytest.mark.user_admin
    @pytest.mark.aeolus_setup
    def test_create_users(self, mozwebqa):
        '''
        Create users
        '''
        home_page = Home(mozwebqa)

        assert home_page.login() == aeolus_msg['login']

        page = Aeolus(mozwebqa)

        for user in Admin.users:
            assert page.create_user(user) == "User registered!"

        # test cleanup
        if page.test_cleanup == True:
            for user in Admin.users:
                assert page.delete_user(user["username"]) == \
                       "User has been successfully deleted."

        if page.product_ver == '1.0.1':
            page.logout()
        else:
            assert page.logout() == "Aeolus Conductor | Login"
        time.sleep(3)

    @pytest.mark.skipif("Aeolus.product_ver == '1.0.1'")
    @pytest.mark.user_admin
    @pytest.mark.aeolus_setup
    def test_create_user_groups(self, mozwebqa):
        '''
        create user groups
        '''
        home_page = Home(mozwebqa)
        #assert home_page.login() == "Login successful!"
        home_page.login()

        page = Aeolus(mozwebqa)

        for user_group in Admin.user_groups:
            assert page.create_user_group(user_group) == "User Group added"

        # test cleanup
        if page.test_cleanup == True:
            for user_group in Admin.user_groups:
                assert page.delete_user_group(user_group["name"]) == \
                       "Deleted user group " + user_group["name"]

        assert page.logout() == "Aeolus Conductor | Login"

    @pytest.mark.skipif("Aeolus.product_ver == '1.0.1'")
    def test_add_users_to_user_groups(self, mozwebqa):
        home_page = Home(mozwebqa)
        assert home_page.login() == "Login successful!"

        page = Aeolus(mozwebqa)

        # move to aeolus_page.py
        # capture user IDs from "/users/" view
        for user in Admin.users:
            user["id"] = page.get_user_id(user["username"])

        # capture user_group IDs from "/user_groups/" view
        for user_group in Admin.user_groups:
            user_group["id"] = page.get_user_group_id(user_group["name"])

