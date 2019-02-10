'''#2
dic = { "name" : "Divya",
        "Dept" : "CSE",
        "Year" : 3
        }
print(dic)
dic.pop("Year")
print("Dictionary values after removing is", dic)

#3
count = 0
str = input("enter string:")
v = set("aeiouAEIOU")
for i in str:
    if i in v :
        count = count + 1
print(count)

#5
import re
str = "abbbabcbabbb"
val = re.match("abbb",str,re.I)
print(val.group())

#1
def cs(a,b):
    c = 0
    for i in range(a,b+1):
        j =1
        while j*j<=i:
            if j*j == i:
                c = c + 1
            j = j+1
        i = i+1
    return c
print(cs(9,25))'''

#4
try:
    n = 10
    a = []
    while n>0:
        dig = n%2
        a.append(dig)
        n= n//2
    a.reverse()
    print("binary equivalent")
    for i in a:
        print(i,end = "")
except IOError:
    print("error")
else:
    print("\nsuccessfull")
