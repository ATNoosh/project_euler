import sys
import math

def is_prime(n): 
    if n < 2: 
        return 0
    for i in range(2,int(math.sqrt(float(n)))+1):
        if int(float(n)) % i == 0:
            return 0
    return 1

num = 10001
i=0
p=0
while 1==1:
    if is_prime(i)>0:
        p += 1
        if p==num:
            break
    i += 1

print(i)