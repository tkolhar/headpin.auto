#!/usr/bin/env python

import py

def pytest_runtest_setup(item):
    """ 
    pytest setup
    """
    pytest_mozwebqa = py.test.config.pluginmanager.getplugin("mozwebqa")
    pytest_mozwebqa.TestSetup.project = item.config.option.project

def pytest_addoption(parser):
    """ 
    Add option to the py.test command line, option is specific to 
    this project.
    """
    parser.addoption("--project",
                     action="store",
                     dest='project',
                     metavar='str',
                     default="sam",
                     help="Specify project - [sam|headpin|katello|cfse]")

def pytest_funcarg__mozwebqa(request):
    pytest_mozwebqa = py.test.config.pluginmanager.getplugin("mozwebqa")
    return pytest_mozwebqa.TestSetup(request)