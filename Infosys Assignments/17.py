s1 = input("string1:")
s2 = input("string2:")
result = "" 
for i in s1:
    if (i.isupper()):
        result = result+i
for i in s2:
    if (i.isupper()):
        result = result + i
print("string 1:", s1)
print("string 2:",s2)

print(result)
        
        

