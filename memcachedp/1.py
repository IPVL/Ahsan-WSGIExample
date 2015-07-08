import memcache
mc = memcache.Client(["192.168.122.223:11211","192.168.122.186:11211"])
mc.set("some", 1)
print mc.get("some")






