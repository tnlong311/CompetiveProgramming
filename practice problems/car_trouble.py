streets = int(input())
graph = []
for i in range(streets):
    graph.append([])

trapped = []
printId = []
for no in range(streets):
    inList = [int(i) for i in input().split()]
    
    printId.append(inList[0])
    
    if inList[1] == 0:
        trapped.append(inList[0])
    else:
        graph[inList[0]] = inList[2:]

reached = [True]
for i in range(streets-1):
    reached.append(False)

check = [0]
while len(check)>0:
    road = check.pop()
#     reached[road] = True
    
    for go in graph[road]:
        if not reached[go]:
            check.append(go)
            reached[go]=True

# print out answers
noProb = True
for i in trapped:
    print("TRAPPED",i)
    noProb = False


for i in printId:
    if not reached[i]:
        print("UNREACHABLE",i)
        noProb = False

if noProb:
    print("NO PROBLEMS")