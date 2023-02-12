import math

def sum_of_square_divisors(n):
    res = 0
    for i in range(1,n + 1):
        if n % i == 0:
            res += i**2
    return res

for i in range(1,64000000):
    sum_square = sum_of_square_divisors(i)
    if(math.sqrt(sum_square) == math.ceil(math.sqrt(sum_square))):
        print(i)