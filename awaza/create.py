from riak import RiakClient, RiakNode, RiakObject
from random import randrange
import sys


tlds =[]
if __name__ == '__main__':
    riakclient = RiakClient()
    print('tlds inserted:')
    str_bucket = 'tld'
    for i in range(1000):
        str_key = str(i)
        bucket = riakclient.bucket(str_bucket)
        obj = RiakObject(riakclient, bucket, str_key)
        obj.content_type = 'text/plain'
        obj.data = 'dom' + str(i) + '.com'
        obj.store()
#j        objget = bucket.get(str_key)
 #       print(objget.data)
        objget = bucket.get(obj.data)
        print(objget.data)

    sys.exit(0)
