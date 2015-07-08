import memcache,time,pprint
mc = memcache.Client(["192.168.122.223:11211","192.168.122.186:11211"])

mc.set_multi({  "B1":2,
		"B2":3,
		"B3":4},
		key_prefix = "weather_")


#to get one key
print mc.get("weather_B1")

#to get all

print mc.get_multi(["B1","B2","B3"], key_prefix = "weather_")


