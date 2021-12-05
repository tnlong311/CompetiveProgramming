T = int(input())
for t in range(T):
    l1, r1, p1, d1 = map(int, input().split())
    l2, r2, p2, d2 = map(int, input().split())
    k = int(input())
    
    c1 = -1
    c2 = -1
    if (l1 <= l2):
        if (r1 >= r2):
            c1 = l2
            c2 = r2
        elif r1 >= l2:
            c1 = l2
            c2 = r1
    elif (l1 <= r2):
        if r1 >= r2:
            c1 = l1
            c2 = r2
        else:
            c1 = l1
            c2 = r1
    
    if (c1 == -1) or (c2 == -1):
        print(0)
        continue
    
    i = 0
    count = 0
    while i<k:            
        i += 1
        if d1 == 0:
            if p1 == l1:
                d1 = 1
                p1 += 1
            else:
                p1 += -1
        else:
            if p1 == r1:
                d1 = 0
                p1 += -1
            else:
                p1 += 1 
        if d2 == 0:
           if p2 == l2:
               d2 = 1
               p2 += 1
           else:
               p2 += -1
        else:
            if p2 == r2:
               d2 = 0
               p2 += -1
            else:
                p2 += 1
                
        if (p1 == p2):
           count += 1

    print(count)
        
     
     
     