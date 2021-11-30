n = int(input())
b = str(input())
a = str(input())

check = True
if (n%2 == 0):
    for i in range(len(b)):
        if (not a[i] == b[i]):
            check = False
else:
    for i in range(len(b)):
        if (a[i] == b[i]):
            check = False

if check:
    print("Deletion succeeded")
else:
    print("Deletion failed")
