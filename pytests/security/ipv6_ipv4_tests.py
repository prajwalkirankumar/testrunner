from basetestcase import BaseTestCase
from security.IPv6_IPv4_grub_level import IPv6_IPv4
from remote.remote_util import RemoteMachineShellConnection, RemoteUtilHelper

class ipv6_ipv4_tests(BaseTestCase):
    REST_PORT = "8091"
    REST_SSL_PORT = "18091"
    N1QL_PORT = "8093"
    N1QL_SSL_PORT = "18093"
    FTS_PORT = "8094"
    FTS_SSL_PORT = "18094"
    ANALYTICS_PORT = "8095"
    ANALYTICS_SSL_PORT = "18095"
    EVENTING_PORT = "8096"
    EVENTING_SSL_PORT = "18096"
    NSERV_PORT = "21100"
    NSERV_SSL_PORT = "21150"
    KV_PORT = "11210"
    KV_SSL_PORT = "11207"
    INDEXER_PORT = "9102"
    LOG_PATH = "/opt/couchbase/var/lib/couchbase/logs"
    BLOCK_PORTS_FILE_PATH = "pytests/security/block_ports.py"
    
    def _port_map_(self):
        return IPv6_IPv4(self.servers).retrieve_port_map()

    def setUp(self):
        super(ipv6_ipv4_tests,self).setUp()
        self.addr_family = self.input.param("addr_family","ipv4")
        nodes_obj = IPv6_IPv4(self.servers)
        if self.upgrade_addr_family is None:
            nodes_obj.set_addr_family(self.addr_family)
        nodes_obj.transfer_file(self.BLOCK_PORTS_FILE_PATH)
        self.mode = self.input.param("mode",None)

    def kill_all_python_processes(self):
        for server in self.servers:
            shell = RemoteMachineShellConnection(server)
            shell.execute_command("pkill python")
            shell.disconnect()

    def tearDown(self):
        self.kill_all_python_processes()
        IPv6_IPv4(self.servers).delete_files()
        super(ipv6_ipv4_tests,self).tearDown()

    def test_services(self):
        self.log.info("ENTERING TESTS")
        servs_inout = self.servers[1:4]
        services_in = []
        for service in self.services_in.split("-"):
            services_in.append(service.split(":")[0])
        rebalance = self.cluster.async_rebalance(self.servers[:self.nodes_init], servs_inout, [],
                                                 services=services_in)
        rebalance.result()
        self.sleep(20)

        if self.addr_family == "ipv4":
            suffix1 = "4"
            suffix2 = ""
        elif self.addr_family == "ipv6":
            suffix1 = "6"
            suffix2 = "6"

        # Check NS Server Ports
        self.log.info("Checking NS Server Ports")
        self.check_ports_for_service([self.NSERV_PORT, self.NSERV_SSL_PORT], self.servers)
        query_str1 = "Failed to start dist inet" + suffix2 + "_tcp_dist on port 21100"
        query_str2 = "Failed to start dist inet" + suffix2 + "_tls_dist on port 21150"
        self.check_ports_on_blocking([self.NSERV_PORT], self.master, [query_str1], "debug.log")
        self.sleep(10)

        kv_node = self.get_nodes_from_services_map(service_type='kv')
        if kv_node is not None:
            self.log.info("Checking KV Ports")
            self.check_ports_for_service([self.KV_PORT, self.KV_SSL_PORT], [kv_node])
            query_str1 = "CRITICAL Failed to create required IPv" + suffix1 + " socket for \"*:11210\""
            query_str2 = "CRITICAL Failed to create required IPv" + suffix1 + " socket for \"*:11207\""
            self.check_ports_on_blocking([self.KV_PORT], kv_node, [query_str1], "debug.log")
            self.check_ports_on_blocking([self.KV_SSL_PORT], kv_node, [query_str2], "debug.log")
            self.sleep(10)

        index_node = self.get_nodes_from_services_map(service_type='index')
        if index_node is not None:
            self.log.info("Checking Indexer Ports")
            self.check_ports_for_service([self.INDEXER_PORT], [index_node])
            query_str = "Error in creating TCP Listener: listen tcp" + suffix1 + " :9102: bind: address already in use"
            self.check_ports_on_blocking([self.INDEXER_PORT], index_node, [query_str], "indexer.log")
            self.sleep(10)

        n1ql_node = self.get_nodes_from_services_map(service_type='n1ql')
        if n1ql_node is not None:
            self.log.info("Checking N1QL Ports")
            self.check_ports_for_service([self.N1QL_PORT,self.N1QL_SSL_PORT],[n1ql_node])
            query_str1 = "Failed to start service: listen tcp" + suffix1 + " :8093: bind: address already in use"
            query_str2 = "Failed to start service: listen tcp" + suffix1 + " :18093: bind: address already in use"
            self.check_ports_on_blocking([self.N1QL_PORT],n1ql_node,[query_str1],"query.log")
            self.check_ports_on_blocking([self.N1QL_SSL_PORT],n1ql_node,[query_str2],"query.log")
            self.sleep(10)

        eventing_node = self.get_nodes_from_services_map(service_type='eventing')
        if eventing_node:
            self.log.info("Checking Eventing Ports")
            self.check_ports_for_service([self.EVENTING_PORT,self.EVENTING_SSL_PORT], [eventing_node])
            query_str1 = "listen tcp" + suffix1 + " :8096: bind: address already in use"
            query_str2 = "listen tcp" + suffix1 + " :18096: bind: address already in use"
            self.check_ports_on_blocking([self.EVENTING_PORT], eventing_node, [query_str1],"eventing.log")
            self.check_ports_on_blocking([self.EVENTING_SSL_PORT], eventing_node, [query_str2],"eventing.log")
            self.sleep(10)

        cbas_node = self.get_nodes_from_services_map(service_type='cbas')
        if cbas_node is not None:
            self.log.info("Checking CBAS Ports")
            self.check_ports_for_service([self.ANALYTICS_PORT], [cbas_node])
            if suffix1 == "4":
                ip = " 127.0.0.1"
            else:
                ip = " [::1]"
            query_str1 = "listen tcp" + suffix1 + ip + ":8095: bind: address already in use"
            query_str2 = "listen tcp" + suffix1 + ip + ":18095: bind: address already in use"
            self.check_ports_on_blocking([self.ANALYTICS_PORT], cbas_node, [query_str1], "analytics_info.log")
            self.check_ports_on_blocking([self.ANALYTICS_SSL_PORT], cbas_node, [query_str2], "analytics_info.log")
            self.sleep(10)

        fts_node = self.get_nodes_from_services_map(service_type='fts')
        if fts_node is not None:
            self.log.info("Checking FTS Ports")
            self.check_ports_for_service([self.FTS_PORT,self.FTS_SSL_PORT], [fts_node])
            query_str1 = "listen tcp" + suffix2 + " 0.0.0.0:8094: bind: address already in use"
            query_str2 = "listen tcp" + suffix2 + " :18094: bind: address already in use"
            self.check_ports_on_blocking([self.FTS_PORT],fts_node,[query_str1],"fts.log")
            self.check_ports_on_blocking([self.FTS_SSL_PORT],fts_node,[query_str2],"fts.log")
            self.sleep(10)

    def verify_logs_wrapper(self,node,logfile,query_strs):
        remote_client = RemoteMachineShellConnection(node)
        output = remote_client.read_remote_file(self.LOG_PATH, logfile)
        logic = self.verify_logs(output, query_strs)
        remote_client.disconnect()
        self.assertTrue(logic, "search string {0} not present in {1}".format(query_strs,logfile))

    def verify_logs(self, logs=[], verification_string=[]):
        logic = True
        for check_string in verification_string:
            check_presence = False
            for val in logs:
                if check_string in val:
                    check_presence = True
            logic = logic and check_presence
        return logic

    def check_ports_on_blocking(self,ports,nodes,query_strs,logfile):
        nodes_obj = IPv6_IPv4([nodes])
        addr_family = nodes_obj.get_addr_family()
        shell = RemoteMachineShellConnection(nodes)
        shell.delete_file(self.LOG_PATH,logfile)
        pids = nodes_obj.block_ports(ports,addr_family)
        self.sleep(20)
        found = self.verify_logs_wrapper(nodes,logfile,query_strs)
        nodes_obj.unblock_ports(pids)
        shell.disconnect()
        return found

    def check_ports_for_service(self,ports,nodes):
        nodes_obj = IPv6_IPv4(nodes)
        cluster_setting = nodes_obj.get_addr_family()

        for port in ports:
            mappings = self._port_map_()[self.mode][cluster_setting]
            self.log.info("{0} {1} {2} Details".format(port,self.mode,cluster_setting))
            if self.mode == "pure_ipv4" or self.mode == "pure_ipv6":
                self.assertEquals(nodes_obj.check_ports([port],cluster_setting),mappings[0],"mapping is {0}".format(mappings[0]))
            elif self.mode == "hostname":
                self.assertEquals(nodes_obj.check_ports([port],cluster_setting),mappings[0] if cluster_setting=="ipv4" else mappings[1])
            # elif self.mode == "ipv4_ipv6":
            #     self.assertEquals(nodes_obj.check_ports([port],cluster_setting),mappings[0] if cluster_setting=="ipv4" else mappings[1])