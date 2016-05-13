from tuqquery.tuq import QueryTests
from remote.remote_util import RemoteMachineShellConnection
from membase.api.rest_client import RestConnection
from membase.api.exception import CBQError

class SysCatalogTests(QueryTests):

    def setUp(self):
        super(SysCatalogTests, self).setUp()

    def suite_setUp(self):
        super(SysCatalogTests, self).suite_setUp()

    def tearDown(self):
        super(SysCatalogTests, self).tearDown()

    def suite_tearDown(self):
        super(SysCatalogTests, self).suite_tearDown()

    def test_sites(self):
        self.query = "SELECT * FROM system:datastores"
        result = self.run_cbq_query()
        host = (self.master.ip, self.input.tuq_client)[self.input.tuq_client and "client" in self.input.tuq_client]
        if self.version == 'sherlock':
            host ='127.0.0.1'
        for res in result['results']:
            self.assertEqual(res['datastores']['id'], res['datastores']['url'],
                             "Id and url don't match")
            self.assertTrue(res['datastores']['url'].find(host) != -1,
                            "Expected: %s, actual: %s" % (host, result))

    def test_pools(self):
        self.query = "SELECT * FROM system:namespaces"
        result = self.run_cbq_query()

        host = '127.0.0.1'
        if self.input.tuq_client and "client" in self.input.tuq_client:
            host = self.input.tuq_client.client
        for res in result['results']:
            
            self.log.info(res)
            self.assertEqual(res['namespaces']['id'], res['namespaces']['name'],
                        "Id and url don't match")
            self.assertTrue(res['namespaces']['datastore_id'].find(host) != -1 or\
                            res['namespaces']['datastore_id'].find(self.master.ip) != -1,
                            "Expected: %s, actual: %s" % (host, result))

    def test_negative_buckets(self):
        queries_errors = {'SELECT * FROM system:keyspaces' : ('Invalid fetch value <nil> of type %!T(MISSING)', 5030)}
        self.negative_common_body(queries_errors)

    def test_buckets(self):
        self.query = "SELECT * FROM system:keyspaces"
        result = self.run_cbq_query()
        buckets = [bucket.name for bucket in self.buckets]
        self.log.info(result)
        self.assertFalse(set(buckets) - set([b['keyspaces']['id'] for b in result['results']]),
                        "Expected ids: %s. Actual result: %s" % (buckets, result))
        self.assertFalse(set(buckets) - set([b['keyspaces']['name'] for b in result['results']]),
                        "Expected names: %s. Actual result: %s" % (buckets, result))
        pools = self.run_cbq_query(query='SELECT * FROM system:namespaces')
        self.assertFalse(set([b['keyspaces']['namespace_id'] for b in result['results']]) -\
                        set([p['namespaces']['id'] for p in pools['results']]),
                        "Expected pools: %s, actual: %s" % (pools, result))
        self.assertFalse(set([b['keyspaces']['datastore_id'] for b in result['results']]) -\
                        set([p['namespaces']['datastore_id'] for p in pools['results']]),
                        "Expected site_ids: %s, actual: %s" % (pools, result))

    def test_prepared_buckets(self):
        for bucket in self.buckets:
            self.query = "SELECT * FROM system:keyspaces"
            self.prepared_common_body()

    def test_memcached_buckets(self):
        self.query = "SELECT * FROM system:keyspaces"
        result = self.run_cbq_query()
        print result
        self.assertTrue(result['metrics']['resultCount'] ==2)
        self.query = "SELECT count(*) FROM system:keyspaces"
        result = self.run_cbq_query()
        self.assertTrue(result['metrics']['resultCount'] ==2)