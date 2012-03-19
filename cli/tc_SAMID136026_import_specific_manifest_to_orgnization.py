import sys, os, subprocess, commands, time
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID136026_import_specific_manifest_to_orgnization(test, params, env):

	vm = env.get_vm(params["main_vm"])
	vm.verify_alive()
	timeout = int(params.get("login_timeout", 360))
	session = vm.wait_for_login(timeout=timeout)

	logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

	try:
                #[A]Prepare test data
                kvm_test_dir = os.path.join(os.environ['AUTODIR'],'tests/kvm/tests')
                content_script_path=os.path.join(kvm_test_dir,'samtest')
                vm.copy_files_to(content_script_path, "/tmp")

		#create an org
		orgname = ee.org1 + time.strftime('%Y%m%d%H%M%S')
		eu().sam_create_org(session, orgname)

		#import a manifest to the org
                manifest="/tmp/samtest/%s"%ee.specific_manifest
		eu().sam_import_manifest_to_org(session, manifest, orgname, ee.default_provider)		

	except Exception, e:
		logging.error(str(e))
		raise error.TestFail("Test Failed - error happened when do import a specific manifest to an org:"+str(e))
	finally:
		eu().sam_delete_org(session, orgname)
		logging.info("=========== End of Running Test Case: %s ==========="%__name__)
