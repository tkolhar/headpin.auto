from pages.base import Base
''' 
THIS IS THE SIMPLIFIED FORMAT FOR THE PURPOSES OF THIS CHALLENGE.
THINGS CAN AND LIKELY SHOULD CHANGE IF PYTHON / PYTEST ARE SELECTED.

THIS IS USING THE PYTEST PARAMTERIZED APPROACH TO DRIVING TESTS WITH
DATA.

USE THE FOLLOWING DICTIONARIES FOR REFERENCE ONLY, _NOT_ FOR
ACTUAL LOGIC.

####
# Used as a reference for now, likely won't be used in code
####
resource_types = [ roles, users, activation_keys, organizations, environments, providers, all]

verbs = {'roles' : ['create', 'delete', 'update', 'read'],
            'users': ['create', 'delete', 'update', 'read'], 
            'activation_keys': ['manage_all', 'read_all'],
            'organizations': [create, delete, delete_systems, update, update_systems, read,
                                    read_systems, register_systems, delete_systems], 
            'environments': [update_systems, read_contents, read_systems, register_systems,
                                   delete_systems], 
            'providers': [update, read]}
'''
###
# DO NOT EDIT HERE
###

def pytest_generate_tests(metafunc):
    """
    Parse the data provided in scenarios.
    """
    idlist = []
    argvalues = []
    for scenario in metafunc.cls.scenarios:
        idlist.append(scenario[0])
        items = scenario[1].items()
        argnames = [x[0] for x in items]
        argvalues.append(([x[1] for x in items]))
    metafunc.parametrize(argnames, argvalues, ids=idlist)
###
# EDIT BELOW
# ADD NEW SCENARIOS
###

scenario1 = ('ACME_Manage_Keys', { 'org': 'ACME_Corporation', 
                                   'perm_name': 'ManageAcmeCorp', 
                                   'resource': 'activation_keys',
                                   'verbs': ('manage_all',),
                                   'allowed': (Base.is_system_tab_visible,
                                               Base.is_new_key_visible,
                                               Base.is_activation_key_name_editable),
                                   'disallowed': (Base.is_dashboard_subs_visible,)})
scenario2 = ('Global_Read_Only', { 'org': 'Global Permissions', 
                                   'perm_name': 'ReadOnlyGlobal', 
                                   'resource': 'organizations', 
                                   'verbs': ('read','create'),
                                   'allowed': (Base.is_organizations_tab_visible,
                                               Base.is_new_organization_visible,
                                               Base.is_new_organization_name_field_editable),
                                   'disallowed': (Base.is_system_tab_visible,
                                                  Base.is_new_key_visible)})

