def fib():
    pprev = 0
    prev = 1
    n = int(input("enter number"))
    for term in range(1,n+1):
        term = prev + pprev
        pprev = prev
        prev = term
        print("fib values are:", term)
fib()
