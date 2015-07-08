import memcache
client = memcache.Client([('127.0.0.1', 11211)])
sample_obj = {"name": "Soliman",
"lang": "Python"}
client.set("sample_user", sample_obj, time=150)
print "Stored to memcached, will auto-expire after 150 seconds"
print client.get("sample_user")
