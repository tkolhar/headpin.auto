import sys, os, subprocess, commands, random
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129290_unsubscribe_subscription(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
		#register a system
		eu().sam_create_system(session, ee.systemname1, ee.default_org, ee.default_env)

		#list available subscriptions
		availpoollist = eu().sam_listavailpools(session, ee.systemname1, ee.default_org)

		#get an available entitlement pool to subscribe with random.sample
		availpool = random.sample(availpoollist, 1)[0]
		poolid = availpool["PoolId"]
		poolname = availpool["PoolName"]

		#subscribe to the pool
		eu().sam_subscribetopool(session, ee.systemname1, ee.default_org, poolid)
		
		#unsubscribe the subscription
		if eu().sam_listconsumedsubscrips(session, ee.systemname1, ee.default_org, poolname):
			cmd="headpin -u admin -p admin system unsubscribe --org=%s --name='%s' --all"%(ee.default_org, ee.systemname1)
			(ret,output)=session.get_command_status_output(cmd)

			logging.info("command of import manifest: %s"%cmd)
			logging.info("result of import manifest: %s"%str(ret))
			logging.info("output of import manifest: %s"%str(output))

			if ret == 0 and "Successfully unsubscribed System" in output:
				logging.info("It's successful to unsubscribe subscriptions.")
			else:
				raise error.TestFail("Test Failed - Failed to unsubscribe subscriptions.")
		else:
			raise error.TestFail("Test Failed - Failed to list consumed subscriptions.")

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when subscribe to a pool:"+str(e))
	finally:
		eu().sam_unregister_system(session, ee.systemname1, ee.default_org)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)
