import math

def is_balanced(n):
    return sum_digits(str(n)[0:math.ceil(len(n)/2)]) == sum_digits(str(n)[math.floor(len(n)/2):len(n)])

def sum_digits(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s

s = 0
arr = []
for i in range(1,10000000):
    if(is_balanced(str(i))):
        arr.append(i)
        s+=int(i)
f = open('p217.txt','w')
f.writelines('\n'.join(map(str,arr)))
f.close()
print(s)