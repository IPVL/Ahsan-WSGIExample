import memcache,time
mc = memcache.Client(["192.168.122.223:11211","192.168.122.186:11211"])
obj = {"name": "Solaiman", "lang": "Python"}
mc.set("some", obj, time=15)
print "Before passing 15 seconds:"
print mc.get("some") 
time.sleep(15)
#got expired after 15s
print "After passing 15 seconds"
print mc.get("some")

