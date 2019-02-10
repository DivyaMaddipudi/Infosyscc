s = "jaaj"
def fun(s):
    if len(s) == 0:
        return s
    else:
        global x
        x = s[-1]+fun(s[:-1])
        return x
print(fun("jaaj"))
if(s == x):
    print("palindrome")
else:
    print("not")
