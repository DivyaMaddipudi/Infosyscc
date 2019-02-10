l1 = ["sofaset", "diningtable", "tvstand", "cupboard"]
print("items available are: ",l1)
l2= [20000,8500,4599,13920]
req = input("enter the furniture:")
quantity = int(input("enter quantity:"))
bill = 0
if quantity > 0 and req in l1:
    l = l1.index(req)
    bill = l2[l] * quantity
    print(bill)
elif req not in  l1:
    print("invalid furniture and bill is",0)
    
