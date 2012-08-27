#!/usr/bin/env python 

import pytest
from unittestzero import Assert
from pages.katello.home import Home
from pages.katello.systems import SystemsTab
#from api.api import ApiTasks
import time

@pytest.mark.destructive
class TestSysWorkflow:
    
    @pytest.mark.katello_workflow
    def test_create_tdl(self, mozwebqa):
        '''
        Create TDL name and description, then remove
        '''
        home_page = Home(mozwebqa)
        home_page.login()

        page = SystemsTab(mozwebqa)
        #page.click(*login_org_selector)
        #page.click_by_text('a', 'redhat')
        page.go_to_page_view("system_templates")

        template_name = 'My System ' + str(time.time())
        template_description = 'My template description'
        page.create_system_template(template_name, template_description)
        page.click_by_text('span', template_name)
        page.remove_sys_template()

# download manifest cmd:
# curl -u <user>:<pass> --insecure -X GET https://subscription.rhn.redhat.com/subscription/consumers/<uuid>/export > manifest.zip
# example: curl -u aweiteka:ilikechicken -X GET https://subscription.rhn.redhat.com/subscription/consumers/da6b17d6-c838-4a67-bd23-76f08e1415bd/export  --insecure > manifest.zip
