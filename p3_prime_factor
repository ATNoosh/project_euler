import sys
import math

def is_prime(n): 
    if n < 2: 
        return 0
    for i in range(2,int(math.sqrt(float(n)))+1):
        if int(float(n)) % i == 0:
            return 0
    return 1

num = 600851475143
big_div = -1
for i in range(int(math.sqrt(float(num)))+1,2,-1):
    if num%i==0 and is_prime(i)>0:
        big_div=i
        break

print(big_div)