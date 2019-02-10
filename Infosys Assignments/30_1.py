def fun(n):
    #m = int(input("enter range"))
    if n == 1:
        return 1
    else:
        x =  fun(n-1)
        res = 3 * x
        return res
print(fun(3))

dic = {
    "name":"cse",
    "value": 100,
    "dept":"computer"
}
dic.popitem()
print("values present:",dic)
