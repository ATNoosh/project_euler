import sys
import math

def is_prime(n): 
    if n < 2: 
        return 0
    for i in range(3,int(math.sqrt(float(n)))+1,2):
        if int(float(n)) % i == 0:
            return 0
    if n % 2 == 0:
        return 0
    return 1

def number_of_divisors(n):
    divisors = 0
    for i in range(1,n + 1):
        if n % i == 0:
            divisors += 1
            print(i)
    return divisors

def next_prime(n):
    if n == 2:
        return 3
    while 1 == 1:
        n += 2
        if is_prime(n):
            return n


number_of_divisors(500500507)