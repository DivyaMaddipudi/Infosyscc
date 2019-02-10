from heapq import nlargest
stu = {
    "john" : 86.5,
    "jack" : 91.2,
    "jill" : 84.5,
    "harry" : 72.1,
    "joe" : 80.5
    }
for key,value in stu.items():
    print(key, value)
two_largest = nlargest(2, stu, key = stu.get)
print("two top valus", two_largest)
for values in stu.values():
    res = 0
    res = res + values
print(res)
