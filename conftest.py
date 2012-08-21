#!/usr/bin/env python

import py

def pytest_runtest_setup(item):
    """ 
    pytest setup
    """
    pytest_mozwebqa = py.test.config.pluginmanager.getplugin("mozwebqa")
    pytest_mozwebqa.TestSetup.project = item.config.option.project
    pytest_mozwebqa.TestSetup.org = item.config.option.org
    pytest_mozwebqa.TestSetup.katello_url = item.config.option.katello_url
    pytest_mozwebqa.TestSetup.aeolus_url = item.config.option.aeolus_url

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

    parser.addoption("--org",
                     action="store",
                     dest='org',
                     metavar='str',
                     default="ACME_Corporation",
                     help="Specify an organization to use for testing, Default: ACME_Corporation")

    parser.addoption("--katello_url",
                     action="store",
                     dest='katello_url',
                     metavar='str',
                     default="https://localhost/katello",
                     help="Specify URL for katello instance - https://localhost/katello")

    parser.addoption("--aeolus_url",
                     action="store",
                     dest='aeolus_url',
                     metavar='str',
                     default="https://localhost/aeolus",
                     help="Specify URL for aeolus instance - https://localhost/aeolus")

def pytest_funcarg__mozwebqa(request):
    pytest_mozwebqa = py.test.config.pluginmanager.getplugin("mozwebqa")
    return pytest_mozwebqa.TestSetup(request)
