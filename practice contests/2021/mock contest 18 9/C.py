T = int(input())

for t in range(T):
    a = str(input()).strip()
    b = str(input()).strip()
    
    def count(a,b):
        l = int(len(a)/2)
        
        if a == b:
            return 0
        if not a[l] == b[l]:
            return -1
        
        com = ''
#         st = ''
        for i in range(l):
#             st += a[i]
            if (a[i] == b[i]) and (a[-(i+1)] == b[-(i+1)]):
                com += "1"
            elif (a[i] == b[-(i+1)]) and (a[-(i+1)] == b[i]):
                com += "0"
            else:
                return -1
#         print(st)
#         print(com)
        
        count = 1

        for i in range(len(com)-1):
            if not com[i] == com[i+1]:
                count += 1
                
        count += -int(com[0])
        
        return count
      
    print(count(a,b))
    
