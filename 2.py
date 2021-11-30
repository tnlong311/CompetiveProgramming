lst =[]
for i in range(1,11):
    lst.append(int(input()))

modSet = set()
for i in lst:
    modSet.add(i%42)

print(len(modSet))

