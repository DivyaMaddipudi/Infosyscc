prev = 1
pprev = -1
n = int(input("enter range"))
for fib in range(1,n+1):
    pprev = prev
    prev = fib
    fib = prev + pprev
    print(fib)
