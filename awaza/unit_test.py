from riak import RiakClient, RiakNode, RiakObject
import unittest
import datamodel

client = RiakClient()
test_user = datamodel.User(client, '001')

class SimpleTestCase(unittest.TestCase):
	def setUp(self):
		client = RiakClient()
		test_user = datamodel.User(client, '001')

class TestSequenceFunctions(SimpleTestCase):
    def test_visit_host(self):
        test_var1 = test_user.tld_map.maps['2014122915'].counters['elpais.com'].value + 1
        test_user.visit_host('elpais.com', '2014122915')
        bucket_test = client.bucket_type('maps').bucket('trackers')
        existing_map = bucket_test.get('001')
        test_var2 = test_user.tld_map.maps['2014122915'].counters['elpais.com'].value
        self.assertEqual(test_var1,test_var2, str(test_var1)+'Visit host fails'+str(test_var2))
    def test_remove_visits(self):
    	test_var1 = test_user.tld_map.maps['2014122915'].counters['elpais.com'].value + 1
        test_user.remove_visits('2014122915')
        bucket_test = client.bucket_type('maps').bucket('trackers')
        existing_map = bucket_test.get('001')
        test_var2 = test_user.tld_map.maps['2014122915'].counters['elpais.com'].value
    	self.assertEqual(0,test_var2, str(test_var1)+'Visit host fails'+str(test_var2))


suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)