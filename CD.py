import time
start_time = time.time()

while True:
    first, second = map(int,input().split())
    if first == 0 and second == 0:
        break
    
#     jack, jill = [], []
    jack = []
    
    for i in range(first):
        jack.append(int(input()))
    
    cd = 0
    i=0
    for j in range(second):
        jill = int(input())
#         print("jill at:",jill)
        
        while i < len(jack):
#             print("i: ",i," jack: ",jack[i])
            if jack[i] == jill:
                cd +=1
                i += 1
                break
            elif jack[i] < jill:
                i +=1
            else:
                break
        
#     i=0
#     j=0
#     cd=0
#     lenJack = len(jack)
#     lenJill = len(jill)
# 
#     while i<lenJack and j<lenJill:
#         if jack[i] == jill[j]:
#             cd+=1
#             j+=1
#             i+=1
#         elif jack[i] > jill[j]:
#             j+=1
#         else:
#             i+=1
# 
    print(cd)
    
print("--- %s seconds ---" % (time.time() - start_time))
