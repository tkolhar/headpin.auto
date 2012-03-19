import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129300_get_katello_status(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
		#Get the status of the katello server
		cmd="headpin -u admin -p admin ping"
		(ret,output)=session.get_command_status_output(cmd)

		logging.info("command of get katello server status: %s"%cmd)
		logging.info("result of get katello server status: %s"%str(ret))
		logging.info("output of get katello server status: %s"%str(output))

		if (ret == 0) and ("candlepin_auth" in output) and ("elasticsearch" in output) and ("katello_jobs" in output):
			logging.info("It's successful to get katello server status.")
		else:
			raise error.TestFail("It's failed to get katello server status.")

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when ping katello server:"+str(e))
	finally:
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)
