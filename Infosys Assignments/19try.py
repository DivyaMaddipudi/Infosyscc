accept = input("enter string:")
x = accept.replace(" ","")
res = x[::2]
print("resultant_output",res)
exp = res[::-1]
print("expected_output",exp)

