def Invalidate(memcache):
    memcache.delete("KEY")

import memcache,time,pprint,threading
mc = memcache.Client(["192.168.122.223:11211","192.168.122.186:11211"])
Inv = Invalidate(mc)
thread = threading.Thread(Inv)
thread.start()

if not mc.gets("KEY"):
    result = 50 # This is slow, so it should be cached
    thread = threading.Thread(Inv)
    thread.start()
    print mc.cas("KEY", result)
