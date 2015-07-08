import memcache,time,pprint
mc = memcache.Client(["192.168.122.223:11211","192.168.122.186:11211"])

#prints necessary information
pprint.pprint(mc.get_stats())

#deletes all in memcache 

mc.flush_all()
