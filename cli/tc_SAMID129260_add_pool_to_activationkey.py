import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129260_add_pool_to_activationkey(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
                #create an activationkey
		eu().sam_create_activationkey(session, ee.keyname1, ee.default_env, ee.default_org)
		
		#add a pool to the activationkey
		eu().sam_add_pool_to_activationkey(session, ee.default_org, ee.keyname1)

        except Exception, e:
                logging.error(str(e))
                raise error.TestFail("Test Failed - error happened when do add a pool to an activationkey:"+str(e))
        finally:
                eu().sam_delete_activationkey(session, ee.keyname1, ee.default_org)
                logging.info("=========== End of Running Test Case: %s ==========="%__name__)
