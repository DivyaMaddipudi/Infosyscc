while True:
    print("Enter 'x' for exit")
    string = input("enter string")
    x = string.upper()
    if string == 'x':
        break
    else:
        for i in x:
            s1 = input("enter character")
            val = x.count(s1)
            print(val,s1)
