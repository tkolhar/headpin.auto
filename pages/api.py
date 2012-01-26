#!/usr/bin/env python

from pages.base import Base
import base64
import httplib
import urllib
import random
import os
import urlparse

try:
   import json
except ImportError:
   import simplejson as json


class apiTasks(Base):
    
    def __init__(self, mozwebqa):
        default_headers = {'Accept': 'application/json',
                           'content-type': 'application/json',
                           'User-Agent': 'katello-cli/0.1'}
        self.port = 443
        self.path_prefix = "/headpin/api"
        self.host = urlparse.urlparse(os.environ.get("HEADPIN_SERVER")).netloc
        self.headers = {}
        self.headers.update(default_headers)
        
    def set_basic_auth_credentials(self, username, password):
        raw = ':'.join((username, password))
        encoded = base64.encodestring(raw)[:-1]
        self.headers['Authorization'] = 'Basic ' + encoded

    def _process_response(self, response):
        response_body = response.read()
        try:
            response_body = json.loads(response_body, encoding='utf-8')
        except:
            pass
        
        return (response.status, response_body, response.getheaders())

    def _https_connection(self):
        return httplib.HTTPSConnection(self.host, self.port)

    def _build_url(self, path, queries=()):
        if not path.startswith(self.path_prefix):
            path = '/'.join((self.path_prefix, path))
        path = urllib.quote(str(path))
        queries = urllib.urlencode(queries)
        if queries:
           path = '?'.join((path, queries))
        return path

    def _prepare_body(self, body, multipart):
        content_type = 'application/json'
        if multipart:
            content_type, body = self._encode_multipart_formdata(body)
        elif not isinstance(body, (type(None), int, file)):
            body = json.dumps(body)
        
        return (content_type, body)
    
    def _request(self, method, path, queries=(), body=None, multipart=False, customHeaders={}):
        
        connection = self._https_connection()
        url = self._build_url(path,queries)
        content_type, body = self._prepare_body(body, multipart)
        
        self.headers['content-type'] = content_type
        self.headers['content-length'] = str(len(body) if body else 0)
        connection.request(method, url, body=body, headers=dict(self.headers.items() + customHeaders.items()))
        return self._process_response(connection.getresponse())
    
    def _GET(self, path, queries=(), customHeaders={}):
        return self._request('GET', path, queries, customHeaders=customHeaders)
    
    def _POST(self, path, body, multipart=False, customHeaders={}):
        return self._request('POST', path, body=body, multipart=multipart, customHeaders=customHeaders)
    
    def _environment_by_name(self, org, envName):
        path = "organizations/%s/environments" % org
        envs = self._GET(path, {"name": envName})[1]
        if len(envs) > 0:
           return str(envs[0]['id'])
        else:
           return None

    def create_new_system(self, name, org, username='admin', password='admin'):
        #ENVIRONMENTS = ["DEV", "TEST", "STAGE", "PROD"]
        
        ENVIRONMENTS = ["DEV"]
        env_name = random.choice(ENVIRONMENTS)
        self.set_basic_auth_credentials(username, password)
        
        path = "/environments/%s/systems" % self._environment_by_name(org, env_name)
        sysdata = {
                   "name" : name,
                   "cp_type" : "system",
                   "facts" : {
                              "distribution.name": "Fedora",
                              "cpu.cpu_socket(s)" : "1"}}
        
        return self._POST(path, sysdata)[1]
'''            
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
  
    def create_user(self, name, password, email):
        admin = AdminCLI()
        admin.setup_parser()
        admin.opts, admin.args = admin.parser.parse_args([])
        admin.setup_server()
        admin._username = "admin"
        admin._password = "admin"
        
        userapi = UserAPI()
        u = userapi.create(name, password, email, False)
'''