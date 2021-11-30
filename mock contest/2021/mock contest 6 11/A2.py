n = int(input())
r = [int(i) for i in input().split()]

m = 0
result = []
r.append(0)

count = 0
for i in range(n-1,-1,-1):
    num = r[i]
    count += 1
    
    if num < 0:
        for j in range(i+1, n-m+1):
            if -num == r[j]:
                m = n-j
                break
    
    step = count - m
    result.append(step)
    
st = ""
for i in range(n-1,-1,-1):
    st += str(result[i]) + " "
    
print(st[:-1])