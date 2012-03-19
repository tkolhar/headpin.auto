import sys, os, subprocess, commands, string, re, random
import logging
from autotest_lib.client.common_lib import error

class ent_utils:

	# ========================================================
	# 	'SAM Server' Test Common Functions
	# ========================================================


        def sam_create_user(self, session, username, password, email):
                #create user with username, password and email address
                cmd="headpin -u admin -p admin user create --username=%s --password=%s --email=%s"%(username, password, email)
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of create user: %s"%cmd)
                logging.info("result of create user: %s"%str(ret))
                logging.info("output of create user: %s"%str(output))

                if (ret == 0) and ("Successfully created user" in output):
                        logging.info("It's successful to create user %s with password %s and email %s."%(username, password, email))
                else:
                        raise error.TestFail("Test Failed - Failed to create user %s with password %s and email %s."%(username, password, email))

        def sam_is_user_exist(self, session, username):
                # check a user exist or not                    
                cmd="headpin -u admin -p admin user list"
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of list user: %s"%cmd)
                logging.info("result of list user: %s"%str(ret))
                logging.info("output of list user: %s"%str(output))

                if (ret == 0) and (username in output):
                        logging.info("User %s exists."%(username))
                        return True
                else:
                        logging.info("User %s does not exist."%(username))
                        return False


        def sam_delete_user(self, session, username):
                #delete user with username
                if self.sam_is_user_exist(session, username):
                        cmd="headpin -u admin -p admin user delete --username=%s"%(username)
                        (ret,output)=session.get_command_status_output(cmd)

                        logging.info("command of delete user: %s"%cmd)
                        logging.info("result of delete user: %s"%str(ret))
                        logging.info("output of delete user: %s"%str(output))

                        if (ret == 0) and ("Successfully deleted user" in output):
                                logging.info("It's successful to delete user %s."%(username))
                        else:
                                raise error.TestFail("Test Failed - Failed to delete user %s."%(username))
                else:
                        logging.info("User %s to be deleted does not exist."%(username))

        def sam_create_org(self, session, orgname):
                #create organization with orgname
                cmd="headpin -u admin -p admin org create --name=%s"%(orgname)
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of create organization: %s"%cmd)
                logging.info("result of create organization: %s"%str(ret))
                logging.info("output of create organization: %s"%str(output))

                if ret == 0 and "Successfully created org" in output:
                        logging.info("It's successful to create organization %s."%orgname)
                else:
                        raise error.TestFail("Test Failed - Failed to create organization %s."%orgname )


        def sam_is_org_exist(self, session, orgname):
                #check an organization existing or not
                cmd="headpin -u admin -p admin org list"
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of list organization: %s"%cmd)
                logging.info("result of list organization: %s"%str(ret))
                logging.info("output of list organization: %s"%str(output))

                if ret == 0 and orgname in output:
                        logging.info("Organization %s exists."%orgname)
                        return True
                else:
                        logging.info("Organization %s does not exist."%orgname)
                        return False

        def sam_delete_org(self, session, orgname):
                #delete an existing organization
                if self.sam_is_org_exist(session, orgname):
                        cmd="headpin -u admin -p admin org delete --name=%s"%(orgname)
                        (ret,output)=session.get_command_status_output(cmd)

                        logging.info("command of delete organization: %s"%cmd)
                        logging.info("result of delete organization: %s"%str(ret))
                        logging.info("output of delete organization: %s"%str(output))

                        if ret == 0 and "Successfully deleted org" in output:
                                logging.info("It's successful to delete organization %s."%orgname)
                        else:
                                raise error.TestFail("Test Failed - Failed to delete organization %s."%orgname)
                else:
                        logging.info("Org %s to be deleted does not exist."%(orgname))

        def sam_create_env(self, session, envname, orgname, priorenv):
                ''' create environment belong to organizaiton with prior environment. '''

                cmd="headpin -u admin -p admin environment create --name=%s --org=%s --prior=%s"%(envname, orgname, priorenv)
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of create environment: %s"%cmd)
                logging.info("result of create environment: %s"%str(ret))
                logging.info("output of create environment: %s"%str(output))

                if ret == 0:
                        logging.info("It's successful to create environment '%s' - belong to organizaiton '%s' with prior environment '%s'."%(envname, orgname, priorenv))
                else:
                        raise error.TestFail("Test Failed - Failed to create environment '%s' - belong to organizaiton '%s' with prior environment '%s'."%(envname, orgname, priorenv) )

        def sam_check_env(self, session, envname, orgname, priorenv, desc='None'):
		''' check environment info. '''

                cmd="headpin -u admin -p admin environment info --name=%s --org=%s" %(envname, orgname)
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of check environment detail info: %s"%cmd)
                logging.info("result of check environment detail info: %s"%str(ret))
                logging.info("output of check environment detail info: %s"%str(output))

                if (ret == 0) and (envname in output) and (orgname in output) and (priorenv in output) and (desc in output):
                        logging.info("It's successful to check environment detail info.")
                else:
			raise error.TestFail("Test Failed - Failed to check environment detail info.")

        def sam_is_env_exist(self, session, envname, orgname):
                ''' check if an environment of one org existing or not. '''

                cmd="headpin -u admin -p admin environment list --org=%s" %orgname
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of list environment: %s"%cmd)
                logging.info("result of list environment: %s"%str(ret))
                logging.info("output of list environment: %s"%str(output))

                if ret == 0 and envname in output:
                        logging.info("Environment %s exists."%envname)
                        return True
                else:
                        logging.info("Environment %s does not exist."%envname)
                        return False

        def sam_delete_env(self, session, envname, orgname):
                ''' delete an existing environment. '''

                if self.sam_is_env_exist(session, envname, orgname):
                        cmd="headpin -u admin -p admin environment delete --name=%s --org=%s"%(envname, orgname)
                        (ret,output)=session.get_command_status_output(cmd)

                        logging.info("command of delete environment: %s"%cmd)
                        logging.info("result of delete environment: %s"%str(ret))
                        logging.info("output of delete environment: %s"%str(output))

                        if ret == 0 and "Successfully deleted environment" in output:
                                logging.info("It's successful to delete environment %s."%envname)
                        else:
                                raise error.TestFail("Test Failed - Failed to delete environment %s."%envname)
                else:
                        logging.info("Environment %s to be deleted does not exist."%(envname))

	def sam_create_activationkey(self, session, keyname, envname, orgname):
                #create an activationkey
                cmd="headpin -u admin -p admin activation_key create --name=%s --org=%s --env=%s"%(keyname, orgname, envname)
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of create activationkey: %s"%cmd)
                logging.info("result of create activationkey: %s"%str(ret))
                logging.info("output of create activationkey: %s"%str(output))

                if ret == 0 and "Successfully created activation key" in output:
                        logging.info("It's successful to create activationkey %s belong to organizaiton %s environment %s."%(keyname, orgname, envname))
                else:
                        raise error.TestFail("Test Failed - Failed to create activationkey %s belong to organizaiton %s environment %s."%(keyname, orgname, envname))

	def sam_is_activationkey_exist(self, session, keyname, orgname):
                #check an activationkey of one org existing or not
                cmd="headpin -u admin -p admin activation_key list --org=%s" %orgname
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of list activationkey: %s"%cmd)
                logging.info("result of list activation_key: %s"%str(ret))
                logging.info("output of list activation_key: %s"%str(output))

                if ret == 0 and keyname in output:
                        logging.info("Activationkey %s exists."%keyname)
                        return True
                else:
                        logging.info("Activationkey %s doesn't exist."%keyname)
                        return False

	def sam_delete_activationkey(self, session, keyname, orgname):
                #delete an existing activation key
                if self.sam_is_activationkey_exist(session, keyname, orgname):
                        cmd="headpin -u admin -p admin activation_key delete --name=%s --org=%s"%(keyname, orgname)
                        (ret,output)=session.get_command_status_output(cmd)

                        logging.info("command of delete activationkey: %s"%cmd)
                        logging.info("result of delete activationkey: %s"%str(ret))
                        logging.info("output of delete activationkey: %s"%str(output))

                        if ret == 0 and "Successfully deleted activation key" in output:
                                logging.info("It's successful to delete activation key %s."%keyname)
                        else:
                                raise error.TestFail("Test Failed - Failed to delete activation key %s."%keyname)
                else:
                        logging.info("Activationkey %s to be deleted doesn't exist."%(keyname))

        def sam_save_option(self, session, optionname, optionvalue):
                ''' save an option. '''

                cmd="headpin -u admin -p admin client remember --option=%s --value=%s"%(optionname, optionvalue)
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of save option: %s"%cmd)
                logging.info("result of save option: %s"%str(ret))
                logging.info("output of save option: %s"%str(output))

                if ret == 0 and "Successfully remembered option [ %s ]"%(optionname) in output:
                        logging.info("It's successful to save the option '%s'."%optionname)
                else:
                        raise error.TestFail("Test Failed - Failed to save the option '%s'."%optionname)

        def sam_remove_option(self, session, optionname):
                ''' remove an option. '''

                cmd="headpin -u admin -p admin client forget --option=%s"%optionname
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of save option: %s"%cmd)
                logging.info("result of save option: %s"%str(ret))
                logging.info("output of save option: %s"%str(output))

                if ret == 0 and "Successfully forgot option [ %s ]"%(optionname) in output:
                        logging.info("It's successful to remove the option '%s'."%optionname)
                else:
                        raise error.TestFail("Test Failed - Failed to remove the option '%s'."%optionname)

	def sam_add_pool_to_activationkey(self, session, orgname, keyname):
		#find a pool belonging to the key's org
		cmd="curl -u admin:admin -k https://localhost/headpin/api/owners/%s/pools |python -mjson.tool|grep 'pools'|awk -F'\"' '{print $4}'"%(orgname)
		(ret,output)=session.get_command_status_output(cmd)

		logging.info("command of find an available pool: %s"%cmd)
		logging.info("result of find an available pool: %s"%str(ret))
		logging.info("output of find an available pool: %s"%str(output))

		if ret == 0 and "pools" in output:
			poollist=self.__parse_sam_avail_pools(session, output)

	                #get an available entitlement pool to subscribe with random.sample
			poolid = random.sample(poollist, 1)[0]
			logging.info("It's successful to find an available pool '%s'."%(poolid))

			#add a pool to an activationkey
			cmd="headpin -u admin -p admin activation_key update --org=%s --name=%s --add_subscription=%s"%(orgname, keyname, poolid)
			(ret,output)=session.get_command_status_output(cmd)

			logging.info("command of add a pool to an activationkey: %s"%cmd)
			logging.info("result of add a pool to an activationkey: %s"%str(ret))
			logging.info("output of add a pool to an activationkey: %s"%str(output))
			if ret == 0 and "Successfully updated activation key [ %s ]"%(keyname) in output:
				#check whether the pool is in the key
				cmd="headpin -u admin -p admin activation_key info --name=%s --org=%s"%(keyname, orgname)
				(ret,output)=session.get_command_status_output(cmd)

				logging.info("command of check activationkey info: %s"%cmd)
				logging.info("result of check activationkey info: %s"%str(ret))
				logging.info("output of check activationkey info: %s"%str(output))
				if ret == 0 and poolid in output:
					logging.info("It's successful to add pool '%s' to activationkey '%s'."%(poolid, keyname))
					return poolid
				else:
					raise error.TestFail("It's failed to add a pool to activationkey '%s'."%keyname)
			else:
				raise error.TestFail("Test Failed - Failed to add a pool to activationkey '%s'."%keyname)
		else:
			raise error.TestFail("Test Failed - Failed to find an available pool")

	def __parse_sam_avail_pools(self, session, output):
		datalines = output.splitlines()
		poollist = []
		# pick up pool lines from output
		data_segs = []
		for line in datalines:
			if "/pools/" in line:
				data_segs.append(line)
		
		# put poolids into poolist
		for seg in data_segs:
			pool=seg.split("/")[2]
			poollist.append(pool)
		return poollist

	def sam_import_manifest_to_org(self, session, filepath, orgname, provider):
		#import a manifest to an organization
		cmd="headpin -u admin -p admin provider import_manifest --org=%s --name='%s' --file=%s"%(orgname, provider, filepath)
		(ret,output)=session.get_command_status_output(cmd)

		logging.info("command of import manifest: %s"%cmd)
		logging.info("result of import manifest: %s"%str(ret))
		logging.info("output of import manifest: %s"%str(output))

		if ret == 0 and "Manifest imported" in output:
			logging.info("It's successful to import manifest to org '%s'."%orgname)
		else:
			raise error.TestFail("Test Failed - Failed to import manifest to org '%s'."%orgname)

	def sam_is_product_exist(self, session, productname, provider, orgname):
		#check whether a product is in the product list of an org
		cmd="headpin -u admin -p admin product list --org=%s --provider='%s'"%(orgname, provider)
		(ret,output)=session.get_command_status_output(cmd)

		logging.info("command of list products of an organization: %s"%cmd)
		logging.info("result of list products of an organization: %s"%str(ret))
		logging.info("output of list products of an organization: %s"%str(output))

		if ret == 0 and productname in output:
			logging.info("The product '%s' is in the product list of org '%s'."%(productname, orgname))
			return True
		else:
			logging.info("The product '%s' isn't in the product list of org '%s'."%(productname, orgname))
			return False

	def sam_create_system(self, session, systemname, orgname, envname):
		#get environment id of envname
		cmd="curl -u admin:admin -k https://localhost/headpin/api/organizations/%s/environments/|python -mjson.tool|grep -C 2 '\"name\": \"%s\"'"%(orgname, envname)
		(ret,output)=session.get_command_status_output(cmd)

		logging.info("command of get environment id: %s"%cmd)
		logging.info("result of get environment id: %s"%str(ret))
		logging.info("output of get environment id: %s"%str(output))
		
		if ret == 0 and envname in output:
			#get the env id from output
			envid=self.__parse_env_output(session, output)
			
			if envid != "":
				#create a new system using candlepin api
				cmd="curl -u admin:admin -k --request POST --data '{\"name\":\"%s\",\"cp_type\":\"system\",\"facts\":{\"distribution.name\":\"Red Hat Enterprise Linux Server\",\"cpu.cpu_socket(s)\":\"1\",\"virt.is_guest\":\"False\",\"uname.machine\":\"x86_64\"}}' --header 'accept: application/json' --header 'content-type: application/json' https://localhost/headpin/api/environments/%s/systems|grep %s"%(systemname,envid,systemname)

				logging.info("command of create a system: %s"%cmd)
				(ret,output)=session.get_command_status_output(cmd)

				logging.info("result of create a system: %s"%str(ret))
				logging.info("output of create a system: %s"%str(output))

				if ret == 0 and systemname in output:
					logging.info("It's successful to create system '%s' in org '%s'."%(systemname, orgname))
				else:
					raise error.TestFail("Test Failed - Failed to create system '%s' in org '%s'."%(systemname, orgname))
			else:
				raise error.TestFail("Test Failed - Failed to get envid of env '%s' from org '%s'."%(envname, orgname))
		else:
			raise error.TestFail("Test Failed - Failed to get env info from org '%s'."%orgname)

	def __parse_env_output(self, session, output):
		datalines = output.splitlines()
		envid=""
		for line in datalines:
			if "\"id\"" in line:
				envid=line.split(":")[1].split(",")[0].strip()
				break
		return envid

        def sam_list_system(self, session, orgname, systemname):
		''' list system and then check system list. '''

                cmd="headpin -u admin -p admin system list --org=%s" %(orgname)
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of list system: %s"%cmd)
                logging.info("result of list system: %s"%str(ret))
                logging.info("output of list system: %s"%str(output))

                if (ret == 0) and (systemname in output):
                        logging.info("It's successful to list system '%s'."%systemname)
                else:
			raise error.TestFail("Test Failed - Failed to list system '%s'."%systemname)

        def sam_is_system_exist(self, session, orgname, systemname):
		''' check if the system exists. '''

                cmd="headpin -u admin -p admin system list --org=%s" %(orgname)
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of list system: %s"%cmd)
                logging.info("result of list system: %s"%str(ret))
                logging.info("output of list system: %s"%str(output))

                if (ret == 0) and (systemname in output):
                        logging.info("The system '%s' exists."%systemname)
			return True
                else:
                        logging.info("The system %s does not exist."%systemname)
                        return False

        def sam_list_system_detail_info(self, session, systemname, orgname, envname, checkinfolist):
		''' list system info. '''

                cmd="headpin -u admin -p admin system info --name=%s --org=%s --environment=%s" %(systemname, orgname, envname)
                (ret,output)=session.get_command_status_output(cmd)

                logging.info("command of list system detail info: %s"%cmd)
                logging.info("result of list system detail info: %s"%str(ret))
                logging.info("output of list system detail info: %s"%str(output))

                if (ret == 0):
			for i in checkinfolist:
				if i in output:
					logging.info("The info '%s' is in command output."%i)
				else:
					raise error.TestFail("Test Failed - Failed to list system detail info - the info '%s' is not in command output."%i)

			logging.info("It's successful to list system detail info.")
                else:
			raise error.TestFail("Test Failed - Failed to list system detail info.")

        def sam_unregister_system(self, session, systemname, orgname):
                ''' unregister a system. '''

		if self.sam_is_system_exist(session, orgname, systemname):
		        cmd="headpin -u admin -p admin system unregister --name=%s --org=%s"%(systemname, orgname)
		        (ret,output)=session.get_command_status_output(cmd)

		        logging.info("command of register system: %s"%cmd)
		        logging.info("result of register system: %s"%str(ret))
		        logging.info("output of register system: %s"%str(output))

		        if ret == 0 and "Successfully unregistered System [ %s ]"%systemname in output:
		                logging.info("It's successful to unregister the system '%s' - belong to organizaiton '%s'."%(systemname, orgname))
		        else:
		                raise error.TestFail("Test Failed - Failed to unregister the system '%s' - belong to organizaiton '%s'."%(systemname, orgname))
                else:
                        logging.info("System '%s' to be unregistered does not exist."%(systemname))

	def sam_listavailpools(self,session, systemname, orgname):
		''' list available subscriptions. '''
		cmd="headpin -u admin -p admin system subscriptions --org=%s --name=%s --available"%(orgname, systemname)
		(ret,output)=session.get_command_status_output(cmd)

		logging.info("command of list available pools: %s"%cmd)
		logging.info("result of list available pools: %s"%str(ret))
		logging.info("output of list available pools: %s"%str(output))

		if ret == 0 and "PoolId" in output:
			logging.info("The available pools are listed successfully.")
			pool_list = self.__parse_sam_avail_pools_cli(session,output)
			return pool_list
		else:
			raise error.TestFail("Test Failed - Failed to list available pools.")
			return None

	def __parse_sam_avail_pools_cli(self,session, output):
		datalines = output.splitlines()
		pool_list = []
		# split output into segmentations for each pool
		data_segs = []
		segs = []
		for line in datalines:
			if "PoolId:" in line:
				segs.append(line)
			elif segs:
				segs.append(line)
			if "MultiEntitlement:" in line:
				data_segs.append(segs)
				segs = []
		# parse detail information for each pool
		for seg in data_segs:
			pool_dict = {}
			for item in seg:
				keyitem = item.split(":")[0]
				valueitem = item.split(":")[1].strip()
				pool_dict[keyitem] = valueitem
			pool_list.append(pool_dict)
		return pool_list

	def sam_subscribetopool(self, session, systemname, orgname, poolid):
		''' subscribe to an available subscription. '''
		cmd="headpin -u admin -p admin system subscribe --name=%s --org=%s --pool=%s"%(systemname, orgname, poolid)
		(ret,output)=session.get_command_status_output(cmd)

		logging.info("command of subscribe to a pool: %s"%cmd)
		logging.info("result of subscribe to a pool: %s"%str(ret))
		logging.info("output of subscribe to a pool: %s"%str(output))

		if ret == 0 and "Successfully subscribed System" in output:
			logging.info("The available pool is subscribed successfully.")
		else:
			raise error.TestFail("Test Failed - Failed to subscribe to available pool %s."%poolid)

	def sam_listconsumedsubscrips(self, session, systemname, orgname, poolname):
		''' list consumed subscriptions. '''
		cmd="headpin -u admin -p admin system subscriptions --org=%s --name=%s "%(orgname, systemname)
		(ret,output)=session.get_command_status_output(cmd)

		logging.info("command of list consumed subscriptions: %s"%cmd)
		logging.info("result of list consumed subscriptions: %s"%str(ret))
		logging.info("output of list consumed subscriptions: %s"%str(output))

		if ret == 0 and poolname in output:
			logging.info("The consumed subscriptions are listed successfully.")
			return True
		else:
			logging.info("No consumed subscriptions are listed.")
			return False
