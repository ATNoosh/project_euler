import time
import math


all_primes = [2]
last_prime_index = 1
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
    global all_primes, last_prime_index
    if last_prime_index < len(all_primes):
        last_prime_index +=1
        return all_primes[last_prime_index - 1]
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

def calculate_prim_arr():
    res = 1
    for p in prime_arr:
        res *= p[0] ** p[1]
    return res

for i in range(1,100000):
    print(i)
    all_primes.append(next_prime(all_primes[len(all_primes)-1]))


print(next_prime(17))
print(next_prime(37))
print(next_prime(37))
print(next_prime(37))
print(next_prime(37))
print(next_prime(37))
"""
f = open("all_primes.txt","w")
f.write(','.join(map(str,all_primes)))
f.close()
"""
"""st = time.time()
 
for i in range(500499):
    if i%1000==0:
        print(i)
        et = st
        st = time.time()
        print(st - et)
    next_min()
print(prime_arr)
final_num = calculate_prim_arr()
print(final_num)
print(final_num%500500507)"""