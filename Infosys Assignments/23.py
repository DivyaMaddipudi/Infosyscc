cus_det = {
    1001: "john",
    1004: "jill",
    1005: "joe",
    1003: "jack" }
print("customer details are:", cus_det)
print("length is ",len(cus_det))
for key in cus_det:
    sorted(cus_det[key])
print("name in ascending order is",cus_det)
cus_det.pop(1005)
print("after deleting 1005 updated dic is", cus_det)
cus_det[1003]= "Marry"
print("updated 1003 to marry", cus_det)
if 1002 in cus_det:
    print("exists")
else:
    print("doesnot exist")
    
