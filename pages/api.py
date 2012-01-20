#!/usr/bin/env python

from pages.base import Base
import katello.client.core.repo
from katello.client.core.repo import Create
from katello.client.cli.admin import AdminCLI
from katello.client.api.utils import get_organization, get_product, get_repo, get_environment
from katello.client.api.repo import RepoAPI
from katello.client.api.organization import OrganizationAPI
from katello.client.api.environment import EnvironmentAPI
from katello.client.api.provider import ProviderAPI
from katello.client.api.product import ProductAPI
from katello.client.api.user import UserAPI
from katello.client.api.system import SystemAPI
import random

class apiTasks(Base):
    def create_new_system(self, name, org):
        ENVIRONMENTS = ["DEV", "TEST", "STAGE", "PROD"]
        randenv = random.choice(ENVIRONMENTS)
        
        admin = AdminCLI()
        admin.setup_parser()
        admin.opts, admin.args = admin.parser.parse_args([])
        admin.setup_server()
        admin._username = "admin"
        admin._password = "admin"
        
        systemapi = SystemAPI()
        system = systemapi.register(name, org, randenv, [], "system")
            
    def create_org(self, name):
        admin = AdminCLI()
        admin.setup_parser()
        admin.opts, admin.args = admin.parser.parse_args([])
        admin.setup_server()
        admin._username = "admin"
        admin._password = "admin"
            
        orgapi = OrganizationAPI()
        orgapi.create(name, "description")
        
    def create_envs(self, org):
        ENVIRONMENTS = ["DEV", "TEST", "STAGE", "PROD"]
        
        admin = AdminCLI()
        admin.setup_parser()
        admin.opts, admin.args = admin.parser.parse_args([])
        admin.setup_server()
        admin._username = "admin"
        admin._password = "admin"
        
        envapi = EnvironmentAPI()
        
        lockerId = get_environment(org, "Locker")["id"]
        envids = [lockerId]
        
        for x in range(len(ENVIRONMENTS)):
            existing_env = get_environment(org, ENVIRONMENTS[x])
            if not existing_env:
                e = envapi.create(org, ENVIRONMENTS[x], "Desc", envids[x])
                envids.append(e["id"])
            else:
                envids.append(existing_env["id"])  