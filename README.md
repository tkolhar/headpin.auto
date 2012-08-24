Automation testing framework for Aeolus, Katello and Headpin projects:  
 
 * http://aeolusproject.org/
 * http://katello.org
   (Note: Headpin is a lite version of Katello)

Tests use Mozilla's AMO methodology: https://github.com/mozilla/Addon-Tests

# DOCUMENTATION

Check out some cool documentation I started for a "challenge" that 
uses the same structure and helper methods found here.

http://eanxgeek.github.com/katello_challenge/index.html

# REQUIRES
 * selenium
 * pytest==2.2.3
 * pytest-xdist==1.6
 * pytest-mozwebqa==0.7.1
 * unittestzero

You can run: ``pip-python install -r ./requirements.txt`` from the root of the project.

So far only selenium standalone testing has been verified:

On Linux, start your selenium server:
NOTE: This step is optional if you are using the instructions below.
``java -jar /path/to/your/selenium/selenium-X.Y.jar \``
``-firefoxProfileTemplate /path/to/ff_profile/.mozilla/firefox/[profile]/``

# RUN TESTS
NOTE: [project] == aeolus|katello|sam|cfse

 * For a single test suite, use:  
``py.test --driver=firefox --baseurl=https://[SERVER_FQDN]/[project]`` 
``--project=[project] --org=[orgname [DEFAULT: ACME_Corporation]]``
``
/tests/[project]/suite_to_run.py]``

 * For a specific test, use:  
``py.test --driver=firefox --baseurl=https://[SERVER_FQDN]/[project]`` 
``--project=[project] --org=[orgname [DEFAULT: ACME_Corporation]]``
``[tests/[project]/suite_to_run.py] -k [name_of_test_to_run]``

 * To run all tests for a project
 ``py.test --driver=firefox --baseurl=https://[SERVER_FQDN]/[project]`` 
 ``--project=[project]`` --org=[orgname [DEFAULT: ACME_Corporation]]``
 ``tests/[project]``
