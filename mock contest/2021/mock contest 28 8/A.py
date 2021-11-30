n, m = map(int, input().split())

def find_u(n):
    return pow(2,n)-2
    
# construct 2xm
i = 2
p = 6
u = find_u(2)
while i<m:
    p = u + (p-u)*2
    i +=1
#construct nxm

j=2
u = find_u(m)
while j<n:
    p = u + (p-u)*2
    j +=1

print(p)