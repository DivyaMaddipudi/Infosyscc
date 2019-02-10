def fib(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        x = fib(n-1) + fib(n-2)
        return x    
print(fib(6))

