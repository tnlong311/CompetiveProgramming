lst = []
lines = int(input())
for i in range(0,lines):
    inpu = input()
    inpu = inpu.lower()
    lst.append(inpu)


result = []

for i in lst:
    alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    for char in i:
        alphabet.discard(char)

    last = ''
    alphabetLst = sorted(alphabet)
    for j in alphabetLst:
        last += j
    
    result.append(last)

for i in result:
    if len(i) == 0:
        print('pangram')
    else:
        print('missing ' + i)
    
    
       
