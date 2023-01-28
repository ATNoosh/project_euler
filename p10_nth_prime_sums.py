import sys
import math

def is_prime(n): 
    if n < 2: 
        return 0
    for i in range(2,int(math.sqrt(float(n)))+1):
        if int(float(n)) % i == 0:
            return 0
    return 1

num = 2000000
i = 1
s = 0
for i in range(1,num):
    if is_prime(i):
        s += i

print(s)