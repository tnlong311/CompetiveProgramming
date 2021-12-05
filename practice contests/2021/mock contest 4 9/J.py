import timeit
start = timeit.default_timer()


n = int(input())

# fact =[1,1]
# for i in range(2,2501):
#     fact.append(i*fact[-1])

for test in range(n):
#     print("yooo",n)
    a, b, c = map(int, input().split())
    al = [int(k) for k in input().split()]
    bl = [int(k) for k in input().split()]
    cl = [int(k) for k in input().split()]

#     print(al, bl, cl)
    numA = 1
    numB=1
    numC=1
    for j in al:
#         numA = numA*fact[j]
        numA = numA*j
    for j in bl:
        numB = numB*j
#         numB = numB*fact[j]
    for j in cl:
        numC = numC*j
#         numC = numC*fact[j]

    maxi = max(numA, max(numB,numC))
    cnt = 0
    result = ""
    if (maxi == numA):
        cnt+=1
        result = "A"
    if (maxi == numB):
        cnt+=1
        result = "B"
    if (maxi == numC):
        cnt+=1
        result = "C"
    
    if (cnt ==1):
        print("Case #%d: %s" % (test+1,result))
    else:
        print("Case #%d: TIE" % (test+1))
          
stop = timeit.default_timer()
print('Time: ', stop - start)

