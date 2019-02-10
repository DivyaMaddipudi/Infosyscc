bill = int(input("enter  the bill amount"))
cus_id = int(input("enter customer id"))
if cus_id>=101 and cus_id<=1001:
    print("valid customerid")
    if bill >= 1000:
        discount_bill = bill - ((5/100)*bill)
        print("bill after discount", discount_bill)
    elif ((bill>=500)and(bill<1000)):
        discount_bill = bill - ((2/100)*bill)
        print("bill after discount", discount_bill)
    else:
        discount_bill = bill - ((5/100)*bill)
        print("bill after discount", discount_bill)
else:
    print("invalid")

