n = int(input())
r = input().split()

r.append(0)


visited = []
position = []
result = []
for i in range(n+1):
    visited.append(False)
    position.append(-1)
    result.append(0)

marker = n
counter = 0
for i in range(n-1,-1,-1):
    counter += 1
    number = r[i]
    
    if number < 0:
        if visited[-number]:
        
        else:
            visited[-number] = True
    
    
    
    
    if number > 0:
        step = counter - result[marker]
    elif visited[-number]:
        marker = visited_p[-number]
        step = counter - result[marker]
        update_visited
    else:
        step = counter - result[marker]
        visited[-number] = True
        visited_p[-number] = counter
    
    result.append(step)

for i in range(n,0,-1):
    print(result[i])