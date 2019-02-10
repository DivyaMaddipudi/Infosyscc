import random as rd

n = int(input("enter times"))
for i in range(0,n):
    if n == 0:
        print("enter q to exit")
        break
    else:
        x = rd.randrange(1,6)
        print(x)
