import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129208_update_environment_info(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
		envname = ee.env1
		prior_env = ee.prior_env
		newprior_env = prior_env+"_New"
		default_org = ee.default_org

		#create two environments and check the environment info
		eu().sam_create_env(session, envname, default_org, prior_env)
        	eu().sam_create_env(session, newprior_env, default_org, prior_env)

		eu().sam_check_env(session, envname, default_org, prior_env, 'None')
		eu().sam_check_env(session, newprior_env, default_org, prior_env, 'None')

		#update environments info and check the environment info
		description="update environment %s" %(envname)
                cmd="headpin -u admin -p admin environment update --name=%s --org=%s --description='%s' --prior=%s"%(envname, default_org, description, newprior_env)
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of delete environment: %s"%cmd)
                logging.info("result of delete environment: %s"%str(ret))
                logging.info("output of delete environment: %s"%str(output))

                if ret == 0 and "Successfully updated environment" in output:

			eu().sam_check_env(session, envname, default_org, newprior_env, description)
                        logging.info("It's successful to update environment %s."%(envname))

                else:
			eu().sam_delete_env(session, envname, default_org)
                        raise error.TestFail("Test Failed - Failed to update environment %s."%envname)

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when do update environment:"+str(e))
	finally:
		eu().sam_delete_env(session, envname, default_org)
		eu().sam_delete_env(session, newprior_env, default_org)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)

