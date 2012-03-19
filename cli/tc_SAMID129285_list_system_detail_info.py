import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129285_list_system_detail_info(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
		#register a system
		eu().sam_create_system(session, ee.systemname1, ee.default_org, ee.default_env)

		#check system info
		eu().sam_list_system_detail_info(session, ee.systemname1, ee.default_org, ee.default_env, [ee.systemname1, ee.default_org])

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when do list system detail info:"+str(e))
	finally:
		eu().sam_unregister_system(session, ee.systemname1, ee.default_org)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)

