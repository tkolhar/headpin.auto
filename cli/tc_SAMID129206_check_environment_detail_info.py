import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129206_check_environment_detail_info(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
		envname = ee.env1
		prior_env = ee.prior_env
		default_org = ee.default_org

		#create an environment
		eu().sam_create_env(session, envname, default_org, prior_env)

		#check environment info
		eu().sam_check_env(session, envname, default_org, prior_env, 'None')

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when do check environment detail info:"+str(e))
	finally:
		eu().sam_delete_env(session, envname, default_org)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)

