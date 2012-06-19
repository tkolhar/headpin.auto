#!/usr/bin/env python

import pytest
from unittestzero import Assert
from api.api import ApiTasks

@pytest.mark.skip_selenium
class TestAPI:
    @pytest.mark.bugzilla(784973)
    def test_ping(self,mozwebqa):
        sysapi = ApiTasks(mozwebqa)
        
        response = sysapi.ping()[0]
        Assert.equal(response, 200)