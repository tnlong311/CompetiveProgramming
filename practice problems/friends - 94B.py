m = int(input())

graph = []
for i in range(5):
    graph.append([0,0,0,0,0])

for pair in range(m):
    p1, p2 = map(int,input().split())
    graph[p1-1][p2-1] = 1
    graph[p2-1][p1-1] = 1

check = False
print(graph)
for val in [0,1]:
    print('iteration #',val)
    for i in range(5):
        visited = []
        for k in range(5):
            visited.append(False)
            
        visited[i] = True
        for j in range(5):
            if (not visited[j]) and (graph[i][j] == val):
                visited[j] = True
                for k in range(5):
                    print('i: %d, j: %d, k: %d' %(i,j,k))
                    print(visited)
                    if (not visited[k]) and (graph[j][k] == val):
                        if k == i:
#                             print('i: %d, j: %d, k: %d' %(i,j,k))
                            check = True
                            break
            if check:
                break
if check:
    print('WIN')
else:
    print('FAIL')