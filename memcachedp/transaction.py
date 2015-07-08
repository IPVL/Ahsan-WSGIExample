#For one client

import memcache,time
mc = memcache.Client(["192.168.122.223:11211","192.168.122.186:11211"])
print "starts"
mc.set("test",0)
for i in range(1000000): 
    mc.incr("test")


#For another client

import memcache,time
mc = memcache.Client(["192.168.122.223:11211","192.168.122.186:11211"])
time.sleep(10)
print "starts"
mc.set("test",0)
for i in range(1000000): 
    mc.incr("test")


# Usually after running mc.get("test") the transaction problem becomes apparent

import memcache,time
mc = memcache.Client(["192.168.122.223:11211","192.168.122.186:11211"])
print mc.get("test")
