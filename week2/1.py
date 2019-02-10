'''
n = int(input("enter number"))
for i in range(0,n):
    print(i*i)'''

#2
'''l = ["Infosys","campus","connect"]
print("list iteration")
for i in l:
    print(i)
l1 = ("Infosys","campus","connect")
print("\n Tuple iteration")
for i in l1:
    print(i)
s = "Infosys"
print("string iteration")
for i in s:
    print(i)

x = {
    "xyz":123,
    "abc":345
}
for  i,j in x.items():
    print(i,j)'''



#3
"""
n = int(input("enter the size:"))
for i in range(0,n):
    print("\n")
    for j in range(0, i+1):
        print(i+1, end = "")"""

#4
"""n= input("enter string")
for letter in n:
    if letter != 's' and letter != 'c':
        print(letter, end = " ")"""

#5

"""count = 0
lis = ['abc', 'xyz', 'aba', '1221', 'aca']
for i in lis:
    if i[0] == i[-1]:
        count = count +1
print(count)"""

#6
"""t = (10,'hi',10,'hello','hi')
l = set(t)
print(tuple(l))"""

#7
'''s = {"hi", "hello", "10", "hi","10"}
print(s)'''

#8

"""dic1 = {
    1:10,
    2:20
}
dic2 = {
    3:30,
    4:40
}
dic3 = {
    5:50,
    6:60
}

dic1.update(dic2)
dic1.update(dic3)
print(dic1)"""

#9

"""x = [[1,2],
     [3,4]]

y = [[1,2],
     [3,4]]

re = [[0,0],
      [0,0]]

res = [[0,0],
       [0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        re[i][j] = x[i][j] + y[i][j]
        for k in range(len(y)):
            res[i][j] += x[i][k]*y[k][j]

print("addition\n")
for r in re:
    print(r)
print("multiplication\n")
for r in res:
    print(r)"""

#10
"""def evenDigits(lower,upper):
    for i in range(lower,upper+1):
        if (i% 2 == 0):
            j = str(i)
            print(",".join(j))
evenDigits(2000,3000)"""


# 12
#f = open(r"C:\Users\divya\Desktop\InfosysCampusConnect\filestext\file.txt","r")
#wc = {}
#for word in f.read().split():
#    if word not in wc:
#        wc[word]=1
#    else:
#        wc[word] += 1
#for k,v in wc.items():
#    print(k,v)



#"testList = [lambda x: x ** 2,  lambda x: x ** 3,   lambda x: x ** 4]
#for test in testList:
   # print(test(3))"
