import time

print(time.time())
print(time.localtime())
print(time.localtime(time.time()))
print(time.asctime())
mytime = (2019,2,5,19,10,20,0,0,0)
print(time.localtime(time.mktime(mytime)))