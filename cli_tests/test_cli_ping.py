#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.ping import Ping

xfail = pytest.mark.xfail

class TestPing:
    
    def test_ping(self):
        ping = Ping()
        
        out, err = ping.ping_error()
        Assert.equal(err, None)
        