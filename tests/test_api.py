#!/usr/bin/env python

import pytest
from unittestzero import Assert
from pages.api import apiTasks

@pytest.mark.skip_selenium
class TestAPI:
    def test_ping(self,mozwebqa):
        sysapi = apiTasks(mozwebqa)
        
        response = sysapi.ping()[0]
        Assert.equal(response, 200)