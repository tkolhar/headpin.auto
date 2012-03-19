import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129261_delete_pool_from_activationkey(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
                #create an activationkey
		eu().sam_create_activationkey(session, ee.keyname1, ee.default_env, ee.default_org)
		
		#add a pool to the activationkey
		poolid=eu().sam_add_pool_to_activationkey(session, ee.default_org, ee.keyname1)
		
		#delete a pool from the activationkey
		if poolid:
			cmd="headpin -u admin -p admin activation_key update --org=%s --name=%s --remove_subscription=%s"%(ee.default_org, ee.keyname1, poolid)
			(ret,output)=session.get_command_status_output(cmd)

			logging.info("command of remove a pool from an activationkey: %s"%cmd)
			logging.info("result of remove a pool from activationkey: %s"%str(ret))
			logging.info("output of remove a pool from activationkey: %s"%str(output))
			if ret == 0 and "Successfully updated activation key [ %s ]"%(ee.keyname1) in output:
				#check whether the pool is not in the key
				cmd="headpin -u admin -p admin activation_key info --name=%s --org=%s"%(ee.keyname1, ee.default_org)
				(ret,output)=session.get_command_status_output(cmd)

				logging.info("command of check activationkey info: %s"%cmd)
				logging.info("result of check activationkey info: %s"%str(ret))
				logging.info("output of check activationkey info: %s"%str(output))
				if ret == 0 and (poolid not in output):
					logging.info("It's successful to remove pool '%s' from activationkey '%s'."%(poolid, ee.keyname1))
				else:
					raise error.TestFail("It's failed to remove a pool from activationkey '%s'."%ee.keyname1)
			else:
				raise error.TestFail("Test Failed - Failed to remove a pool from activationkey '%s'."%ee.keyname1)
		else:
			raise error.TestFail("Test Failed - The pool to be removed from activationkey '%s' is not exist."%ee.keyname1)
	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when do remove a pool from an activationkey:"+str(e))
	finally:
		eu().sam_delete_activationkey(session, ee.keyname1, ee.default_org)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)
