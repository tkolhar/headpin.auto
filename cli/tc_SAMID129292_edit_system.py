import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129292_edit_system(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
		#register a system
		eu().sam_create_system(session, ee.systemname1, ee.default_org, ee.default_env)

		#Edit a system's name, description and location.
		description_new="Edited the system"
		location_new="location_new"
                cmd="headpin -u admin -p admin system update --name=%s --org=%s --new-name=%s --description='%s' --location=%s"%(ee.systemname1, ee.default_org, ee.systemname2, description_new, location_new)
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of register system: %s"%cmd)
                logging.info("result of register system: %s"%str(ret))
                logging.info("output of register system: %s"%str(output))

                if ret == 0 and "Successfully updated system" in output:
                        logging.info("It's successful to updated the system '%s'."%(ee.systemname1))

			#check system info
			eu().sam_list_system_detail_info(session, ee.systemname2, ee.default_org, ee.default_env, [ee.systemname2, ee.default_org, description_new, location_new])

                else:
			eu().sam_unregister_system(session, ee.systemname1, ee.default_org)
                        raise error.TestFail("Test Failed - Failed to updated the system '%s'."%(ee.systemname1))

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when register a system:"+str(e))
	finally:
		eu().sam_unregister_system(session, ee.systemname2, ee.default_org)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)

