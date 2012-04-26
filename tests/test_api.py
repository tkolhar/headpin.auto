#!/usr/bin/env python

import pytest
from unittestzero import Assert
from api.api import ApiTasks

@pytest.mark.skip_selenium
class TestAPI:
    def test_ping(self,mozwebqa):
        #pytest.xfail("https://bugzilla.redhat.com/show_bug.cgi?id=784973")
        sysapi = ApiTasks(mozwebqa)
        
        response = sysapi.ping()[0]
        Assert.equal(response, 200)