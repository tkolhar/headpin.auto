import sys, os, subprocess, commands, random
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129289_list_consumed_subscription(test, params, env):

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

		#list consumed subscriptions
		if eu().sam_listconsumedsubscrips(session, ee.systemname1, ee.default_org, poolname):
			logging.info("It's successful to list consumed subscriptions.")
		else:
			raise error.TestFail("Test Failed - Failed to list consumed subscriptions.")

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when list consumed subscriptions:"+str(e))
	finally:
		eu().sam_unregister_system(session, ee.systemname1, ee.default_org)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)
