import sys, os, subprocess, commands, time
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129298_list_products(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
		#create an org
		orgname = ee.org1 + time.strftime('%Y%m%d%H%M%S')
		eu().sam_create_org(session, orgname)

		#import a manifest to the org
		manifest="/tmp/samtest/%s"%ee.manifest1
		eu().sam_import_manifest_to_org(session, manifest, orgname, ee.default_provider)
	
	        #list products
		product1=ee.manifest1_product1
		product2=ee.manifest1_product2
		if eu().sam_is_product_exist(session, product1, ee.default_provider, orgname) and eu().sam_is_product_exist(session, product2, ee.default_provider, orgname):
			logging.info("It's successful to list products of org '%s'."%orgname)
		else:
			raise error.TestFail("Test Failed - Failed to list products of the org '%s'."%orgname)

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when do list products:"+str(e))
	finally:
		eu().sam_delete_org(session, orgname)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)
