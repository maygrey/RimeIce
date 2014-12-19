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

    def remove_visits(self, time):
        """
            Remove a map of visits at "time" from the user's map
        """  
        del self.tld_map.maps[time]
        self.tld_map.store()

def get_random_host(max_doms):
    """
        Given a number of doms, XX, return domXX.com
    """
    random_host = "dom_" + str(randrange(max_doms)).zfill(3) + ".com"
    return random_host

def create_all_user_entries(user_id, max_doms, max_user_visits):
    """
        Given max_user_visits and a user, do random visits to 
        the listed hosts till arrive to max_user_visits
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
    max_doms = 100
    max_user_visits = 5
    for user_id in range(0, max_user_id):
      create_all_user_entries(0, max_doms, max_user_visits)


def query_stats_by_user(client, user_id):
    """
        Request(read) the last 24 hours counters of user_id
    """
    user = User(client, user_id)
    counter = 0
    print(user.tld_map.value)
    current24 = {}
    for key in user.tld_map.value:
        for tld in user.tld_map.value[key]:
            #print(user.tld_map.value[key][tld])
            if current24.has_key(tld):
                current24[tld[0]] += 1
                #print(current24[tld])
            else :
                current24[tld[0]] = 1
                print(current24)
    return current24
    
def query_stats():
    """
        generic stats query
    """
    current_user_id = 0;
    user_dict = query_stats_by_user(client, current_user_id)

def reader(client, n, users, date):
    """
        Generic read of n users
    """
    #todo date
    key = randrange(10)
    usertemp = []
    for i in range(n):
        usertemp[i] = User(client,i)
    return usertemp

def writer(client, n, users, tlds, time):
    """
        write a number of users visits on random user_id 
        random domain(tld) and random date (time)
    """
    for i in range(n):
        date = "20141218" + str(randrange(23)).zfill(2)
        key = randrange(users)
        tld = "dom" + str(randrange(tlds)) + ".com"
        usertemp = User(client, key)
        usertemp.visit_host(tld, date)
    
def parse_read_args():
    if len(sys.argv) != 4:
        print("Bad read  arguments number")
    count = int(sys.argv[2])
    max_user_id = int(sys.argv[3])
    max_domain_id = int(sys.argv[4])
    return count, max_user_id, max_domain_id

def parse_write_args():
    if len(sys.argv) != 6:
        print("Bad write arguments number")
    count = int(sys.argv[2])
    max_user_id = int(sys.argv[3])
    max_domain_id = int(sys.argv[4])
    date = sys.argv[5]
    return count, max_user_id, max_domain_id, date

if __name__ == '__main__':
	#usuario = User(client, '001')
    #create_all_entries()
    #query_stats()
	#usuario.visit_host('elpais', 201412130000)
    """

    """
    if len(sys.argv) < 2:
        print("Bad num of parameters")
        sys.exit(0)
    if (sys.argv[1] != "Read") and (sys.argv[1] != "Write"):
         print
    if sys.argv[1] == "Read":
        parsed_args = parse_read_args()
        reader (client, parsed_args[0], parsed_args[1], parsed_args[2])
    elif sys.argv[1] == "Write":
        parsed_args = parse_write_args()
        writer(client, parsed_args[0], parsed_args[1], parsed_args[2], parsed_args[3])




