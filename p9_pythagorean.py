endNum = 1000
shouldBreak = 0
for a in range(1,endNum):
    for b in range(a+1,endNum):
        for c in range(b+1,endNum):
            if a*a + b*b == c*c and a + b + c == endNum:
                shouldBreak = 1
                break
        if shouldBreak > 0:
            break
    if shouldBreak > 0:
        break

if shouldBreak > 0:
    print(a)
    print(b)
    print(c)
else:
    print("Not found!")