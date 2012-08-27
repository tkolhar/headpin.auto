#!/usr/bin/env python

import pytest
from unittestzero import Assert
from pages.aeolus.home import Home
from pages.aeolus.aeolus_page import Aeolus
from data.aeolus_data import Admin
import time
from pprint import pprint

# TODO: move hard-coded assert messages

class TestAdmin():

    @pytest.mark.user_admin
    @pytest.mark.aeolus_setup
    def test_create_user(self, mozwebqa):
        '''
        Create users
        '''
        home_page = Home(mozwebqa)
        msg = home_page.login()
        assert msg == "Login successful!"

        page = Aeolus(mozwebqa)

        for user in Admin.users:
            msg = page.create_user(user)
            assert msg == "User registered!"

        # test cleanup
        if page.test_cleanup in ['True', 'true', '1']:
            for user in Admin.users:
                msg = page.delete_user(user["username"])
                #assert msg == "Deleted user " + user["username"]
                assert msg == "User has been successfully deleted."

    @pytest.mark.user_admin
    @pytest.mark.aeolus_setup
    def test_create_user_groups(self, mozwebqa):
        '''
        create user groups
        '''
        home_page = Home(mozwebqa)
        msg = home_page.login()
        assert msg == "Login successful!"

        page = Aeolus(mozwebqa)

        for user_group in Admin.user_groups:
            msg = page.create_user_group(user_group)
            assert msg == "User Group added"

        # test cleanup
        if page.test_cleanup in ['True', 'true', '1']:
            for user_group in Admin.user_groups:
                msg = page.delete_user_group(user_group["name"])
                assert msg == "Deleted user group " + user_group["name"]

