string = "divya"
def rev(string):
    if len(string) == 0:
        return string
    else:
        return string[-1] + rev(string[:-1])
print("original string is:",string)
print(rev("divya"))
