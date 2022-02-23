def dis(a,b):
    x = ord(a)
    y = ord(b)
    print(min(abs(x-y),26-abs(x-y)))