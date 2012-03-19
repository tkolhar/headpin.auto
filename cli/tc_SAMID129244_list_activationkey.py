import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129244_list_activationkey(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)
	
	try:
	        #create an activationkey
        	eu().sam_create_activationkey(session, ee.keyname1, ee.default_env, ee.default_org)

		#list activationkey
		eu().sam_is_activationkey_exist(session, ee.keyname1, ee.default_org)

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when do list a user:"+str(e))
	finally:
		eu().sam_delete_activationkey(session, ee.keyname1, ee.default_org)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)
