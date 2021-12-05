n = int(input())

xd = dict()
yd = dict()

l = []

for i in range(n):
    a,b = map(int, input().split())
    l.append([a,b])

for i in range(n):
    x = l[i][0]
    y = l[i][1]
    
    if x in xd:
        if y in xd[x]:
            xd[x][y] += 1
        else:
            xd[x][y] = 1
    else:
        xd[x] = {y: 1}

for i in range(n):
    y = l[i][1]
    
    if y in yd:
        yd[y] += 1  
    else:
        yd[y] = 1

cnt = 0
both_cnt = 0

for k_dict in xd.values():
    x_cnt = 0
    
    for k in k_dict.values():
        x_cnt += k
        both_cnt += k*(k-1)/2
    
    cnt += x_cnt*(x_cnt-1)/2

for k in yd.values():
    cnt += k*(k-1)/2

cnt = cnt - both_cnt

print(int(cnt))

print(xd)
print(yd)
print(both_cnt)
    

# l = []
# s = set()
# for i in range(n):
#     a,b = map(int, input().split())
#     l.append([a,b])
#     s.add(i)
#     
# xd = dict()
# yd = dict()
# 
# r = set()
# for i in range(n):
#     v = l[i][0]
#  
#     if v in xd:
#         s.remove(i)
#         r.add(xd[v][1])
#         xd[v][0] += 1
#     else:
#         xd[v] = [1,i]
# 
# for j in s:
#     v = l[j][1] 
#     if v in yd:
#         yd[v] += 1
#     else:
#         yd[v] = 1
# 
# cnt = 0
# for i in xd.values():
#     value = i[0]
#     cnt += value*(value-1)/2
#     
# for i in yd.values():
#     print("yo:",i)
#     cnt += i*(i-1)/2
# 
# print(xd)
# print(yd)
# print(int(cnt))