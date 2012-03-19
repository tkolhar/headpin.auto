import sys, os, subprocess, commands, time
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129543_import_two_manifests_to_two_orgs(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
		#create two org
		orgname1 = ee.org1 + time.strftime('%Y%m%d%H%M%S')
		eu().sam_create_org(session, orgname1)
		orgname2 = orgname1 + "1"
		eu().sam_create_org(session, orgname2)

		#import a manifest to orgname1
                manifest1="/tmp/samtest/%s"%ee.manifest1
		eu().sam_import_manifest_to_org(session, manifest1, orgname1, ee.default_provider)		

		#import another manifest from another distributor to orgname2
                manifest2="/tmp/samtest/%s"%ee.specific_manifest
		eu().sam_import_manifest_to_org(session, manifest2, orgname2, ee.default_provider)		

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when do import two manifests from different distributors to two orgs:"+str(e))
	finally:
		eu().sam_delete_org(session, orgname1)
		eu().sam_delete_org(session, orgname2)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)
