import sys
import math

def is_prime(n): 
    if n < 2: 
        return 0
    for i in range(2,int(math.sqrt(float(n)))+1):
        if int(float(n)) % i == 0:
            return 0
    return 1

from itertools import product
from itertools import permutations

li = ['1', '3', '7', '9']
s = 0 # 2 is circular prime but 1 is not prime 
for i in range(1,7): # 1 to 1000000
    for comb in product(li, repeat=i):
        shouldCount = 1
        for comb2 in [''.join(p) for p in permutations(comb)]:
            if is_prime(int(''.join(p))) == 0:
                shouldCount = 0
                break
        if shouldCount == 1:
            print(''.join(comb))
            s += 1

print(s)
