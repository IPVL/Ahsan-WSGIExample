import memcache

#Different type of values can be stored
#test & test2
mc = memcache.Client(["192.168.122.223:11211","192.168.122.186:11211"])
lst =["apple", "orange", "cherry"]
dicta = {"name": "x","job":"y","age":30}
tupl = ("name","x")
lstoftupl = [("name","x"),("job","y"),("age",10)] 
mc.set("some", lst)
print mc.get("some")
mc.set("some",lstoftupl)
print mc.get("some")
mc.set("some",dicta)
print mc.get("some")






