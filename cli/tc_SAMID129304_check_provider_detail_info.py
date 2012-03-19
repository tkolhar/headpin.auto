import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129304_check_provider_detail_info(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
	        #check provider detail info
		cmd="headpin -u admin -p admin provider info --org=%s --name='%s'" %(ee.default_org,ee.default_provider)
		(ret,output)=session.get_command_status_output(cmd)

		logging.info("command of check provider detail info: %s"%cmd)
		logging.info("result of check provider detail info: %s"%str(ret))
		logging.info("output of check provider detail info: %s"%str(output))

		if (ret == 0) and ("Name:        %s"%ee.default_provider in output) and ("Url:         %s"%ee.default_provider_repo_url in output):
			logging.info("It's successful to check provider detail info.")
		else:
			raise error.TestFail("It's failed to check provider detail info.")

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when do check provider detail info:"+str(e))
	finally:
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)
