#!/usr/bin/env python

import pytest
from unittestzero import Assert
from commands.ping import Ping

class TestPing:
    
    def test_ping(self):
        ping = Ping()
        
        out, err = ping.ping_error()
        Assert.equal(err, "None")
        