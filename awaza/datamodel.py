from riak import RiakClient, RiakNode, RiakObject
from riak.datatypes import Map
from random import randrange
import sys

client = RiakClient()

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

class User:
    def __init__(self, client, user_id):
        self.client = client
        self.user_id = str(user_id)
        bucket_str = 'trackers'
        bucket = self.client.bucket_type('maps').bucket(bucket_str)

        print self.user_id
        # The Python client can use the new() function to automatically
        # detect that a map is being targeted by the client
        key = self.user_id
        existing_map = bucket.get(key)
        self.tld_map = existing_map

        """if existing_map.exists:
            print "User exists\n"
            self.tld_map = existing_map
        else:
            print "User do not exist. Creating\n"
            self.tld_map = bucket.new(key)
            #self.tld_map = Map(bucket, key)
        """
    def visit_host(self, host, time):
        """
            Insert a visit to the host at the user's map
        """
        print time
        hour = str(extract_hour(time))
        print hour
        dom = extract_dom(host)
        print dom
    	#self.tld_map.maps[hour].counters[host].increment()
        self.tld_map.maps[time].counters[dom].increment()
    	self.tld_map.store()

def get_random_host(max_doms):
    """
        Given a number of doms, XX, return domXX.com
    """
    #hosts = ["elpais.com", "google.com", "raquel.com"]
    #random_host = hosts[randrange(len(hosts)     )]
    random_host = "dom_" + str(randrange(max_doms)).zfill(3) + ".com"
    return random_host

def create_all_user_entries(user_id, max_doms, max_user_visits):
    """
        Given max_user_visits and a user, do random visits to the listed hosts till arrive to max_user_visits
    """
    user = User(client, user_id)
    for visit_hour in range(0,1):
        time = "20141214" + str(visit_hour).zfill(2)
        for visit_number in range(0, max_user_visits):
            host = get_random_host(max_doms)
            print "hour " + time + ": " + host
            user.visit_host(host, time)

def create_all_entries():
    """
        Defining maximum values for users ids and
        visits by user in an hour
    """
    max_user_id = 2
    max_doms = 1000;
    max_user_visits = 5
    #for user_id in range(0, max_user_id)
    for user_id in range(0, 1):
      create_all_user_entries(0, max_doms, max_user_visits)


def query_stats_by_user(client, user_id):
    user = User(client, user_id)
    print(user.tld_map.value)
    current24 = {}
    for key in user.tld_map.value:
        for tld in user.tld_map.value[key]:
            print(user.tld_map.value[key][tld])
            if current24.has_key(tld):
                current24[tld[0]] += 1
                print(current24)
            else :
                current24[tld[0]] = 1
                print(current24)
    yield current24
    

def query_stats():
    current_user_id = 0;
    user_dict = query_stats_by_user(client, current_user_id)




if __name__ == '__main__':
	#usuario = User(client, '001')
    #create_all_entries()
    query_stats()
	#usuario.visit_host('elpais', 201412130000)
