accept = input("enter string")
x = accept.replace(" ","")
for i in range(len(x)):
    if i%2 == 0:
        res = x[i]
        print(res, end="")
print(res[0])
