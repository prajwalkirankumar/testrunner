from security.ldapGroupBase import ldapGroupBase
from security.rbac_base import RbacBase
from newupgradebasetest import NewUpgradeBaseTest
from basetestcase import BaseTestCase
from membase.api.rest_client import RestConnection, RestHelper
from remote.remote_util import RemoteMachineShellConnection, RemoteUtilHelper
from security.ldapGroupBase import ldapGroupBase
from security.rbacmain import rbacmain
from threading import Thread


class ldapgrpupgrade(NewUpgradeBaseTest):
    user_list_ldap = [{'id': 'preupgradeldap1', 'password': 'password', 'name': 'preupgradeldap1'},
                      {'id': 'preupgradeldap2', 'password': 'password', 'name': 'preupgradeldap2'},
                      {'id': 'preupgradeldap3', 'password': 'password', 'name': 'preupgradeldap3'}]

    user_list_builtin = [{'id': 'preupgradeint1', 'password': 'password', 'name': 'preupgradeldap1'},
                         {'id': 'preupgradeint2', 'password': 'password', 'name': 'preupgradeldap2'},
                         {'id': 'preupgradeint3', 'password': 'password', 'name': 'preupgradeldap3'}]

    user_role_list_ldap = [{'id': 'preupgradeldap1', 'name': 'preupgradeldap1', 'roles': 'cluster_admin:admin'},
                           {'id': 'preupgradeldap2', 'name': 'preupgradeldap2', 'roles': 'cluster_admin:admin'},
                           {'id': 'preupgradeldap3', 'name': 'preupgradeldap3', 'roles': 'cluster_admin:admin'}]

    user_role_list_builtin = [
        {'id': 'preupgradeint1', 'name': 'preupgradeldap1', 'password': 'password', 'roles': 'cluster_admin:admin'},
        {'id': 'preupgradeint2', 'name': 'preupgradeldap2', 'password': 'password', 'roles': 'cluster_admin:admin'},
        {'id': 'preupgradeint3', 'name': 'preupgradeldap3', 'password': 'password', 'roles': 'cluster_admin:admin'}]

    user_list_builtin_postupgrade = [{'id': 'postupgradeint1', 'password': 'password', 'name': 'postupgradeldap1'},
                                     {'id': 'postupgradeint2', 'password': 'password', 'name': 'postupgradeldap2'},
                                     {'id': 'postupgradeint3', 'password': 'password', 'name': 'postupgradeldap3'}]

    user_role_list_builtin_postupgrade = [
        {'id': 'postupgradeint1', 'name': 'postupgradeldap1', 'password': 'password', 'roles': 'cluster_admin:admin'},
        {'id': 'postupgradeint2', 'name': 'postupgradeldap2', 'password': 'password', 'roles': 'cluster_admin:admin'},
        {'id': 'postupgradeint3', 'name': 'postupgradeldap3', 'password': 'passwrod', 'roles': 'cluster_admin:admin'}]

    user_list_ldap_postupgrade = ['postupgrade_ldap1', 'postupgrade_ldap2', 'postupgrade_ldap3', 'postupgrade_ldap4',
                                  'postupgrade_ldap5']

    user_list_builtin_postupgrade = ['postupgrade_builtin1', 'postupgrade_builtin2', 'postupgrade_builtin3',
                                     'postupgrade_builtin4', 'postupgrade_builtin5']

    def setUp(self):
        super(ldapgrpupgrade, self).setUp()
        self.initial_version = self.input.param("initial_version", '5.5.4-4338')
        self.upgrade_version = self.input.param("upgrade_version", "6.5.0-3084")

    def pre_upgrade_settings(self):
        # Create a set of users - local and external users
        rest = RestConnection(self.master)
        rbacmain().setup_auth_mechanism(self.servers, 'ldap', rest)
        for user in self.user_list_ldap:
            RbacBase().create_user_source([user], 'ldap', self.master)
        # RbacBase().create_user_source(self.user_list_builtin, 'builtin', self.master)
        RbacBase().add_user_role(self.user_role_list_ldap, rest, source='ldap')
        RbacBase().add_user_role(self.user_role_list_builtin, rest, source='builtin')

        for ldapuser, builtinuser in zip(self.user_list_ldap, self.user_list_builtin):
            result = ldapGroupBase().check_permission(ldapuser['id'], self.master)
            self.assertTrue(result)
            result = ldapGroupBase().check_permission(builtinuser['id'], self.master)
            self.assertTrue(result)

    def post_upgrade_settings(self):
        from security.ldapGroupBase import ldapGroupBase
        rest = RestConnection(self.master)

        ldapGroupBase().create_ldap_config(self.master)

        # Create a set of user - ldap and external users
        RbacBase().create_user_source(self.user_list_builtin_postupgrade, 'builtin', self.master)
        RbacBase().add_user_role(self.user_role_list_builtin_postupgrade, rest, source='builtin')

        # Create ldap group
        LDAP_GROUP_DN = "ou=Groups,dc=couchbase,dc=com"
        ldapGroupBase().create_group_ldap('test_ldap_grp_post_upgrade', self.user_list_ldap_postupgrade, self.master)
        group_dn = 'cn=testgrp,' + LDAP_GROUP_DN
        ldapGroupBase().add_role_group('test_grp_post_upgrade', ['cluster_admin'], group_dn, self.master)
        # Create local group and users
        ldapGroupBase().create_int_group('test_builtin_grp_post_upgrade', self.user_list_builtin_postupgrade,
                                         ['cluster_admin'], ['cluster_admin'], self.master)

        for user in self.user_list_ldap:
            print
            user
            result = ldapGroupBase().check_permission(user['id'], self.master)
            self.assertTrue(result)

        for user in self.user_list_builtin:
            print
            user
            result = ldapGroupBase().check_permission(user['id'], self.master)
            self.assertTrue(result)

        for user in self.user_list_ldap_postupgrade:
            result = ldapGroupBase().check_permission(user, self.master)
            self.assertFalse(result)

        for user in self.user_list_builtin_postupgrade:
            result = ldapGroupBase().check_permission(user, self.master)
            self.assertFalse(result)

        # Post upgrade use pre upgrade users to different group, to see how it works
        # Give lower role to group and check
        LDAP_GROUP_DN = "ou=Groups,dc=couchbase,dc=com"
        ldapGroupBase().create_group_ldap('test_ldap_grp_post_upgrade_old_users', [self.user_list_ldap[0]['id']],
                                          self.master, user_creation=False)
        for i in range(1, len(self.user_list_ldap)):
            ldapGroupBase().update_group('test_ldap_grp_post_upgrade_old_users', self.user_list_ldap[i]['id'], 'Add',
                                         self.master)
        group_dn = 'cn=test_ldap_grp_post_upgrade_old_users,' + LDAP_GROUP_DN
        ldapGroupBase().add_role_group('test_grp_post_upgrade', ['cluster_admin'], group_dn, self.master)

        # Create local group and users
        ldapGroupBase().create_int_group('test_builtin_grp_post_upgrade_old_users', [self.user_list_builtin[0]['id']],
                                         ['cluster_admin'], ['cluster_admin'], self.master, user_creation=False)

        for i in range(1, len(self.user_list_builtin)):
            print
            self.user_list_builtin[i]['id']
            ldapGroupBase().add_int_user_role(self.user_list_builtin[i]['id'],
                                              'test_builtin_grp_post_upgrade_old_users', self.master)

        '''
        for user in self.user_list_ldap:
            result = ldapGroupBase().check_permission(user['id'],self.master)
            self.assertTrue(result)

        for user in self.user_list_builtin:
            result = ldapGroupBase().check_permission(user['id'],self.master)
            self.assertTrue(result)
        '''

    def tearDown(self):
        super(ldapgrpupgrade, self).tearDown()

    def upgrade_all_nodes(self):
        servers_in = self.servers[1:]
        self._install(self.servers)
        self.cluster.rebalance(self.servers, servers_in, [])
        self.pre_upgrade_settings()

        upgrade_threads = self._async_update(upgrade_version=self.upgrade_version, servers=self.servers)
        for threads in upgrade_threads:
            threads.join()

        self.post_upgrade_settings()

    def upgrade_half_nodes(self):
        serv_upgrade = self.servers[2:4]
        servers_in = self.servers[1:]
        self._install(self.servers)
        self.cluster.rebalance(self.servers, servers_in, [])
        self.user_role = self.input.param('user_role', None)
        self.setup_4_1_settings()

        upgrade_threads = self._async_update(upgrade_version=self.upgrade_version, servers=serv_upgrade)
        for threads in upgrade_threads:
            threads.join()

        status, content, header = rbacmain(self.master)._retrieve_user_roles()
        self.assertFalse(status,
                         "Incorrect status for rbac cluster in mixed cluster {0} - {1} - {2}".format(status, content,
                                                                                                     header))

        for server in serv_upgrade:
            status, content, header = rbacmain(server)._retrieve_user_roles()
            self.assertFalse(status, "Incorrect status for rbac cluster in mixed cluster {0} - {1} - {2}".format(status,
                                                                                                                 content,
                                                                                                                 header))

