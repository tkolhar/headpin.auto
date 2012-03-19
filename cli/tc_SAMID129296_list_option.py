import sys, os, subprocess, commands
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129296_list_option(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
		#save 2 options
		optionname1="option_name1"
		optionvalue1="option_value1"
		optionname2="option_name2"
		optionvalue2="option_value2"
		eu().sam_save_option(session, optionname1, optionvalue1)
		eu().sam_save_option(session, optionname2, optionvalue2)

		#list options
                cmd="headpin -u admin -p admin client saved_options"
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of list option: %s"%cmd)
                logging.info("result of list option: %s"%str(ret))
                logging.info("output of list option: %s"%str(output))

                if ret == 0 and (optionname1 in output) and (optionvalue1 in output) and (optionname2 in output) and (optionvalue2 in output):
                        logging.info("It's successful to list the options.")
                else:
                        raise error.TestFail("Test Failed - Failed to list the options.")

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when list the options:"+str(e))
	finally:
		eu().sam_remove_option(session, optionname1)
		eu().sam_remove_option(session, optionname2)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)

