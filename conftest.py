#!/usr/bin/env python

import py

def pytest_runtest_setup(item):
    """ 
    pytest setup
    """
    pytest_mozwebqa = py.test.config.pluginmanager.getplugin("mozwebqa")
    pytest_mozwebqa.TestSetup.project = item.config.option.project
    pytest_mozwebqa.TestSetup.org = item.config.option.org
    pytest_mozwebqa.TestSetup.product_version = item.config.option.product_version
    pytest_mozwebqa.TestSetup.test_cleanup = item.config.option.test_cleanup

def pytest_addoption(parser):
    """ 
    Add option to the py.test command line, option is specific to 
    this project.
    """
    parser.addoption("--project",
                     action="store",
                     dest='project',
                     metavar='str',
                     default="katello",
                     help="Specify project - [sam|headpin|katello|cfse|aeolus|cfce]")

    parser.addoption("--org",
                     action="store",
                     dest='org',
                     metavar='str',
                     default="ACME_Corporation",
                     help="Specify an organization to use for testing, Default: ACME_Corporation")

    parser.addoption("--product_version",
                     action="store",
                     dest='product_version',
                     metavar='str',
                     default='1.1',
                     help="Product version number (string). Default: 1.1")

    parser.addoption("--test_cleanup",
                     action="store",
                     dest='test_cleanup',
                     metavar='bool',
                     default=False,
                     help="Boolean flag to trigger post-test data cleanup such as deleting users and other data.")

def pytest_funcarg__mozwebqa(request):
    pytest_mozwebqa = py.test.config.pluginmanager.getplugin("mozwebqa")
    return pytest_mozwebqa.TestSetup(request)
