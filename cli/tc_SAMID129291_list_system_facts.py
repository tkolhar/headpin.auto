import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129291_list_system_facts(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
		#register a system
		eu().sam_create_system(session, ee.systemname1, ee.default_org, ee.default_env)

	        #list system facts
		cmd="headpin -u admin -p admin system facts --name=%s --org=%s --environment=%s" %(ee.systemname1, ee.default_org, ee.default_env)
		(ret,output)=session.get_command_status_output(cmd)

		logging.info("command of list system facts: %s"%cmd)
		logging.info("result of list system facts: %s"%str(ret))
		logging.info("output of list system facts: %s"%str(output))

		if (ret == 0) and ("Cpu.cpu Socket(s)" in output) and ("Distribution.name" in output) and ("Uname.machine" in output) and ("Virt.is Guest" in output):
			logging.info("It's successful to list system facts.")
		else:
			raise error.TestFail("It's failed to list system facts.")

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when do list system facts:"+str(e))
	finally:
		eu().sam_unregister_system(session, ee.systemname1, ee.default_org)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)
