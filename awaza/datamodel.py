from riak import RiakClient, RiakNode, RiakObject
from riak.datatypes import Map
from random import randrange
import sys

client = RiakClient()

class User:
    def __init__(self, client, user_id):
        self.client = client
        self.user_id = str(user_id)
        bucket_str = 'trackers'
        bucket = self.client.bucket(bucket_str)

        # The Python client can use the new() function to automatically
        # detect that a map is being targeted by the client
        key = self.user_id
        existing_map = bucket.get(key)

        if existing_map.exists:
            print "User exists\n"
            self.tld_map = existing_map
        else:
            print "User do not exist. Creating\n"
            self.tld_map = bucket.new(key)
            self.tld_map.store()

    def visit_host(self, host, time):
    	self.tld_map.maps[str(extracthour(time))].counters[host].increment()
    	self.store()


def extract_hour(time):
    """
        Given format YYYYMMDDHH retrieves HH as integer
    """
    hour = int(time[-2] + time[-1])
    return(hour)

def extract_dom(host):
    """
        Given http://subdom.dom.ext/whatever extracts "dom.ext"
    """
    dom = host.split('.')[-2:]
    currenttld = dom[0] + '.' + dom[1]
    return currenttld

def get_random_host():
    hosts = ["elpais.com", "google.com", "raquel.com"]
    random_host = hosts[randrange(len(hosts))]

    return random_host

def create_all_user_entries(user_id, max_user_visits):
    user = User(client, user_id)
    for visit_hour in range(0,1):
        time = "20141214" + str(visit_hour).zfill(2)
        for visit_number in range(0, max_user_visits):
            host = get_random_host()
            print "hour " + time + ": " + host
            #user.visit_host(host, time)

def create_all_entries():
    """
        Defining maximum values for users ids and
        visits by user in an hour
    """
    max_user_id = 2
    max_user_visits = 5
    #for user_id in range(0, max_user_id)
    for user_id in range(0, 1):
      create_all_user_entries(0, max_user_visits)


def query_stats_by_user(user_id):
    pass

def query_stats():
    current_user_id = 0;
    query_stats_by_user(current_user_id)



if __name__ == '__main__':
	#usuario = User(client, '001')
    create_all_entries()
	#usuario.visit_host('elpais', 201412130000)
