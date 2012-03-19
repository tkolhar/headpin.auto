import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129193_check_user_detail_info(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
		#create a user
		eu().sam_create_user(session, ee.username1ss, ee.password1ss, ee.email1)

		#check user detail info
                cmd="headpin -u admin -p admin user info --username=%s" %(ee.username1ss)
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of check user detail info: %s"%cmd)
                logging.info("result of check user detail info: %s"%str(ret))
                logging.info("output of check user detail info: %s"%str(output))

                if (ret == 0) and (ee.username1ss in output) and (ee.email1 in output):
                        logging.info("It's successful to check user %s detail info."%(ee.username1ss))
                else:
                        raise error.TestFail("It's failed to check user %s detail info."%(ee.username1ss))
                        
	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when do check a user detail info:"+str(e))
	finally:
		eu().sam_delete_user(session, ee.username1ss)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)

