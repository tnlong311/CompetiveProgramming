import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

lst = []
for k in range(n):
    lst.append([float(i) for i in input().split()])
    
def recur(step, n, m, result, cur, desired, lst):
    if (step == m-1):
        return lst[cur][desired]
    
    for next_cur in range(n):
        result += lst[cur][next_cur]*recur(step+1,n,m,result,next_cur, desired, lst)
        
    return result
        
for j in range(n):
    print(recur(0,n,m,0,0,j,lst))
    
    
