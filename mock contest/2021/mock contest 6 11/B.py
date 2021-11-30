a = str(input())
b = str(input())

both = 0
up = 0
down = 0
for i in range(len(a)):
    if a[i] == "#":
        if b[i] == "#":
            both += 1
        else:
            up += 1
    elif b[i] == "#":
        if a[i] == "#":
            both += 1
        else:
            down += 1
            
if (not both == 0) or ((up == 0 or down == 0) and (up+down+both >0)):
    print('YES')
    p1 = ''
    p2 = ''
    for i in range(up):
        p1 += "#"
        p2 += "."
    for i in range(both):
        p1 += "#"
        p2 += "#"
    for i in range(down):
        p1 += "."
        p2 += "#"
        
    left = len(a)-up-down-both
    for i in range(left):
        p1+= "."
        p2 += "."
    
    print(p1)
    print(p2)
else:
    print('NO')

        