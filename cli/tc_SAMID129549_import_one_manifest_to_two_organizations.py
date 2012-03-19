import sys, os, subprocess, commands, time
import logging
from autotest_lib.client.common_lib import error
from autotest_lib.client.bin import utils
from autotest_lib.client.virt import virt_test_utils, virt_utils
from autotest_lib.client.tests.kvm.tests.ent_utils import ent_utils as eu
from autotest_lib.client.tests.kvm.tests.ent_env import ent_env as ee

def run_tc_SAMID129549_import_one_manifest_to_two_organizations(test, params, env):

        vm = env.get_vm(params["main_vm"])
        vm.verify_alive()
        timeout = int(params.get("login_timeout", 360))
        session = vm.wait_for_login(timeout=timeout)

        logging.info("=========== Begin of Running Test Case: %s ==========="%__name__)

        try:
                #create two orgs
                orgname1 = ee.org1 + time.strftime('%Y%m%d%H%M%S')
                eu().sam_create_org(session, orgname1)
		orgname2 = orgname1 + "1"
		eu().sam_create_org(session, orgname2)

                #import a manifest to the org1
                manifest="/tmp/samtest/%s"%ee.manifest1
                eu().sam_import_manifest_to_org(session, manifest, orgname1, ee.default_provider)

                #import the manifest to another org
                cmd="headpin -u admin -p admin provider import_manifest --org=%s --name='%s' --file=%s"%(orgname2, ee.default_provider, manifest)
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of import manifest: %s"%cmd)
                logging.info("result of import manifest: %s"%str(ret))
                logging.info("output of import manifest: %s"%str(output))

        except Exception, e:

                if "Timeout expired while waiting for shell command to complete:" in str(e):

                        if "Manifest import for provider [ %s ] failed"%ee.default_provider in str(e):
				logging.info(str(e))
                                logging.info("It's successful to verify that one manifest can't be imported to two orgs.")
                        else:
				logging.error(str(e))
                                raise error.TestFail("Test Failed - One manifest shouldn't be imported to two orgs.")
                else:
			logging.error(str(e))
                        raise error.TestFail("Test Failed - error happened when do import one manifest to two orgs:"+str(e))
        finally:
                eu().sam_delete_org(session, orgname1)
                eu().sam_delete_org(session, orgname2)
                logging.info("=========== End of Running Test Case: %s ==========="%__name__)
