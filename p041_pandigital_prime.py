import math
from itertools import permutations

def is_prime(n): 
    if n < 2: 
        return 0
    for i in range(2,int(math.sqrt(float(n)))+1):
        if int(float(n)) % i == 0:
            return 0
    return 1

main_str = ["1","2","3","4","5","6","7"] # because sigma(1,9) and sigma(1,8) are divisible by 3

prm = permutations(main_str)
for i in list(prm):
    if is_prime(int("".join(i)))==1:
        print("".join(i))