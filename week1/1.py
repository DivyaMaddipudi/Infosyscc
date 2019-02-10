#file extension
'''n = input("enter file name with extension:")
f_ext = n.split('.')
x = f_ext[-1]
print(x)

#sum
n = input("enter one number:")
temp = n
temp1 = temp+temp
temp2 = temp+temp+temp
val = int(n)+int(temp1)+int(temp2)
print(val)

#Multiline comment

print("a string that you \"don\'t\" have to escape \n This \n is a ....... multi-line \n here doc string -------->")

#4
n = int(input("enter num"))
dif = n - 19
if(dif>0):
    print("value is ", 2 * dif)
else:
    print(dif)

#5
n = input("Enter string: ")
if(n[0:2] == "Is"):
    print("String is ", n)
else:
    n = "Is" + n
    print("String",n)

#9
import math 
n = int(input("enter value:"))
x= hex(n)
print("hexa decimal value is", x)

#10
import math 
n = int(input("enter value:"))
x= bin(n)
print("hexa decimal value is", x)

#7
import math 
n = input("enter character:")
x= ord(n)
print("ASCII value is", x)

#6
sec=int(input("enter the number of seconds:"))
if(sec >= 86400):
    m = sec/60
    h = m/60
    d = h/24
    print("Time in Minutes is ", m,"mins")
    print("Time in Hours is ", h,"hrs")
    print("Days is", d,"days")
else:
    print("Seconds can\'t redable")

#8
x = int(input("enter first num:"))
y = int(input("enter second num:"))
f1 = float(x)
f2 = float(y)
if(x>y):
    print("largest integer value",x)
else:
    print("largest integer value",y)
if(f1>f2):
    print("largest float value",f1)
else:
    print("largest float value",f2)'''
    