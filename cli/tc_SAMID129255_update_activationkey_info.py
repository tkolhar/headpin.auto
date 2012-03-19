import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129255_update_activationkey_info(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
	        #create an activation_key
		eu().sam_create_activationkey(session, ee.keyname1, ee.default_env, ee.default_org)
		newdescription="update activation key %s to activation key %s" %(ee.keyname1, ee.keyname2)
		
		#create an environment
		eu().sam_create_env(session, ee.env1, ee.default_org, ee.prior_env)

                #update key info
		cmd="headpin -u admin -p admin activation_key update --org=%s --name=%s --new_name=%s --description='%s' --environment=%s" %(ee.default_org, ee.keyname1, ee.keyname2, newdescription, ee.env1)
		(ret,output)=session.get_command_status_output(cmd)

		logging.info("command of update key info: %s"%cmd)
		logging.info("result of update key info: %s"%str(ret))
		logging.info("output of update key info: %s"%str(output))

		if ret == 0 and "Successfully updated activation key" in output:
                        #check activationkey info update or not
                        cmd="headpin -u admin -p admin activation_key info --name=%s --org=%s"%(ee.keyname2,ee.default_org)
                        (ret,output)=session.get_command_status_output(cmd)

                        logging.info("command of list key info: %s"%cmd)
                        logging.info("result of list key info: %s"%str(ret))
                        logging.info("output of list key info: %s"%str(output))

                        if (ret == 0) and (ee.keyname2 in output) and (newdescription in output):
                                logging.info("It's successful to update activation key %s to activationkey %s" %(ee.keyname1, ee.keyname2))
			else:
				eu().sam_delete_activationkey(session, ee.keyname1, ee.default_org)
	                        raise error.TestFail("It's failed to update activation key %s."%ee.keyname1)
                else:
			eu().sam_delete_activationkey(session, ee.keyname1, ee.default_org)
                        raise error.TestFail("Test Failed - Failed to update activation key %s."%ee.keyname1)

        except Exception, e:
                logging.error(str(e))
                raise error.TestFail("Test Failed - error happened when do update activationkey:"+str(e))
        finally:
                eu().sam_delete_activationkey(session, ee.keyname2, ee.default_org)
                eu().sam_delete_env(session, ee.env1, ee.default_org)
                logging.info("=========== End of Running Test Case: %s ==========="%__name__)
