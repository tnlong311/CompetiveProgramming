s = str(input())
n = int(input())

a = s[0]
b = s[1]

l = len(s)

for i in range(1,l-2):
    if s[i-1] <= s[i+1]:
        c = s[i-1]
    else:
        c = s[i+1]
        
    if s[i] == a:
        if c < b:
            b = c
    elif s[i] < a:
        a = s[i]
        b = c

if s[l-1] == a:
    if s[l-2] < b:
        b = s[l-2]
elif s[l-1] < a:
    a = s[l-1]
    b = s[l-2]
    
final = ""
for i in range(n//2):
    final += a
    final += b
    
if n%2 == 1:
    final += a

print(final)
        
