n = int(input())
for i in range(n):
    c = int(input())
    d = [int(a) for a in input().split()]
    j = [int(a) for a in input().split()]
    
    d.sort()
    j.sort()
    
#     print(d,j)
    maxt = 0
    for k in range(c):
#         print("car:",d[k])
#         print("person:",j[-(4*k+1)])
        maxt = max(maxt, d[k] + j[-(4*k+1)])
        
    print("Trip #%d: %d" % (i+1,maxt))
    

