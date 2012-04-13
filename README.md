Automation testing framework for Katello and Headpin projects:  
 
 * https://fedorahosted.org/candlepin/wiki/headpin/Headpin  
 * https://fedorahosted.org/katello/wiki

Test use Mozilla's AMO methodology: https://github.com/mozilla/Addon-Tests

# REQUIRES
 * selenium
 * mozwebqa
 * pytest==2.2.3
 * pytest-xdist==1.6
 * BeautifulSoup==3.2.0
 * pytest-mozwebqa==0.7.1
 * unittestzero

You can run: ``pip-python install -r ./requirements.txt`` from the root of the project.

So far only selenium standalone testing has been verified:

On Linux, start your selenium server:  
``java -jar /path/to/your/selenium/selenium-serr-standalone-2.16.1.jar \``
``-firefoxProfileTemplate /path/to/ff_profile/.mozilla/firefox/[profile]/``

# RUN TESTS
 * For a single test suite, use:  
``py.test --browsername=firefox --platform=Linux --browserver=11 \``
``--baseurl=SERVER_FQDN/[sam|cfse|katello|headpin] -q [tests/suite_to_run.py]``

 * For a specific test, use:  
``py.test --browsername=firefox --platform=Linux --browserver=11 \``
``--baseurl=SERVER_FQDN/[sam|cfse|katello|headpin] -q [tests/suite_to_run.py] -k [name_of_test_to_run]``
