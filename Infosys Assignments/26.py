jc = {"john", "jack", "jill", "joe"}
pc = {"jake", "john", "eric", "jill"}
x = len(pc)
print("no of students in pc is:", x)
y = jc.intersection(pc)
print("only java students",y)
z = jc.intersection(pc)
print("only python students", z)
both = pc.union(jc)
print("both java and python", both)
