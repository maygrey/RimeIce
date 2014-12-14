from riak import RiakClient, RiakNode, RiakObject
from riak.datatypes import Map
import sys

client = RiakClient()

class User:
    def __init__(self, user_id):
        bucket = client.bucket('trackers')
        key = user_id

        # The Python client can use the new() function to automatically
        # detect that a map is being targeted by the client
        tld_map = bucket.new(key)

        self.tld_map.store()

    def visit_host(self, host, time):
    	self.tld_map.maps[str(extracthour(time))].counters[host].increment()
    	self.store()

if __name__ == '__main__':
	usuario = User('001')
	usuario.visit_host('elpais', 201412130000)
	pass