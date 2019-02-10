n = int(input("enter the range:"))
pprev = -1
prev = 1
for term in range(0,n+1):
    term = prev + pprev
    pprev = prev
    prev = term
    print(term)

