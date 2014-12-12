from riak import RiakClient, RiakNode, RiakObject
from random import randrange
import sys

def register(host,user_id,time):
	currenttld = extractdom(host)
	riakclient = RiakClient()
	#bucket : trackers, key:user_id, object:json map
	str_bucket = 'trackers'
	bucket = riakclient.bucket(str_bucket)

	str_key = user_id
	obj = RiakObject(riakclient, bucket, str_key)
    obj.content_type = 'text/plain'
    #todo creación del map
    obj.data = 'prueba'
    obj.store()

def extracthour(time):
	hour = int(time[-2] + time[-1])
	return(hour)

def getdata(user_id):
	objget = bucket.get(user_id)
	return(objget.data)
	#todo extraer del object data los tlds de la hora dada

def extractdom(host):
    dom = host.split('.')[-2:]
    currenttld = dom[0] + '.' + dom[1]
    return currenttld


if __name__ == '__main__':
    register('aa.bb.cc.d','userA','2014121102')
    register('pp.com','userB','2014121104')
~                                                         