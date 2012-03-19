import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129295_save_option(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
		#save a option
		optionname="option_name1"
		optionvalue="option_value1"
		eu().sam_save_option(session, optionname, optionvalue)

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when save a option:"+str(e))
	finally:
		eu().sam_remove_option(session, optionname)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)

