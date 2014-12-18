from riak import RiakClient, RiakNode, RiakObject
from riak.datatypes import Map
from random import randrange
import sys

client = RiakClient()
MAXDATE = 99999999
MINDATE = 00000000

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
        #self.maxdate = 99999999
        #self.mindate = 00000000
        self.user_id = str(user_id)
        bucket_str = 'trackers'
        bucket = self.client.bucket_type('maps').bucket(bucket_str)
        key = self.user_id
        existing_map = bucket.get(key)
        self.tld_map = existing_map

    def visit_host(self, host, time):
        """
            Insert a visit to the host at the user's map
        """
        hour = str(extract_hour(time))
        dom = extract_dom(host)
        #if distance(maxdate)
        #if time < self.maxdate:
        self.tld_map.maps[time].counters[dom].increment()
    	self.tld_map.store()

    def remove_visit(self, host, time):
        """
            Remove a visit to the host at the user's map
        """
        self.tld_map.maps[time].clear()



def get_random_host(max_doms):
    """
        Given a number of doms, XX, return domXX.com
    """
    random_host = "dom_" + str(randrange(max_doms)).zfill(3) + ".com"
    return random_host

def create_all_user_entries(user_id, max_doms, max_user_visits):
    """
        Given max_user_visits and a user, do random visits to the listed hosts till arrive to max_user_visits
    """
    user = User(client, user_id)
    for visit_hour in range(0,23):
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
    max_user_id = 10
    max_doms = 1000
    max_user_visits = 5
    for user_id in range(0, max_user_id):
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
    return current24
    

def query_stats():
    current_user_id = 0;
    user_dict = query_stats_by_user(client, current_user_id)

def cleaner(client, users):
    for i in range(users):
        pass
def reader(client, n, users, tlds, times):
    #todo date
    for i in range(n):
        pass
def writer():
    pass
if __name__ == '__main__':
	#usuario = User(client, '001')
    #create_all_entries()
    query_stats()
	#usuario.visit_host('elpais', 201412130000)
