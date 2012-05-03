#!/usr/bin/env python

import mozwebqa

def pytest_runtest_setup(item):
    mozwebqa.TestSetup.project = item.config.option.project

def pytest_addoption(parser):
    parser.addoption("--project",
                     action="store",
                     dest='project',
                     metavar='str',
                     default="sam",
                     help="Specify project - [sam|headpin|katello|cfse]")

def pytest_funcarg__mozwebqa(request):
    return mozwebqa.TestSetup(request)
