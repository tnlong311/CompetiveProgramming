T = int(input())
for t in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    
    gt = [1]
    for i in range(2,n+1):
        gt.append(gt[i-1]*i)
    
    b = []
    unique = []
    for num in a:
        
        i = 0
        lap = True
        while i < len(b):
            if num == b[i]:
                