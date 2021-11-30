n,m = map(int, input().split())
p1 = []
p2 = []
for h in range(n):
    p1.append(int(input()))
for k in range(m):
    p2.append(int(input()))

p1.sort()
p2.sort()

w = 0
i = 0
for j in range(m):
    while i < n:
        can = p1[i]
        paint = p2[j]
        if can >= paint:
            w += can - paint
            break
        else:
            i += 1
            
print(w)