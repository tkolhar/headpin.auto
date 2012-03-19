import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129205_list_all_environments(test, params, env):

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

		#list all environments
                cmd="headpin -u admin -p admin environment list --org=%s" %default_org
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of list environments: %s"%cmd)
                logging.info("result of list environments: %s"%str(ret))
                logging.info("output of list environments: %s"%str(output))

                if ret == 0 and envname in output:
                        logging.info("It's successful to list all environments.")
                else:
			raise error.TestFail("Test Failed - Failed to list all environments.")

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when do list all environments:"+str(e))
	finally:
		eu().sam_delete_env(session, envname, default_org)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)

