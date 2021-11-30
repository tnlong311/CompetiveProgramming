teams = int(input())

for i in range(teams):
    g, p = map(int, input().split())
    
    print("Team #%d"%(i+1))
    print("Games:",g)
    print("Points:",p)
    print("Possible records:")
    maxw = p//3
    while (maxw>=0):
        maxt = p-3*maxw
        l = g - maxt - maxw
#         print(maxw,maxt,l)
        if (l>=0 and (maxt+3*maxw) == p):
            print("%d-%d-%d" % (maxw,maxt,l))
            
        maxw -= 1
    print()