import sys
import math

def is_prime(n): 
    if n < 2: 
        return 0
    for i in range(2,int(math.sqrt(float(n)))+1):
        if int(float(n)) % i == 0:
            return 0
    return 1

def number_of_divisors(n):
    divisors = 0
    for i in range(1,n + 1):
        if n % i == 0:
            divisors += 1
    return divisors

def next_prime(n):
    if n == 2:
        return 3
    while 1 == 1:
        n += 2
        if is_prime(n):
            return n

prime_arr = [[2, 1]]

def next_min():
    global prime_arr
    next_p = [next_prime(prime_arr[len(prime_arr)-1][0]),1]
    i = 0
    for p in prime_arr:
        new_multiplier = p[0] ** (2**math.log(p[1]+1,2))
        if new_multiplier < next_p[0]:
            prime_arr[i] = [p[0],(2**(1 + math.log(p[1]+1,2))-1)]
            return
        i += 1
    prime_arr.append(next_p)
    

next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)
next_min()
print(prime_arr)