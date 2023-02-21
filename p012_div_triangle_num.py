import math
prime_arr = [[2, 1]]
all_primes = []
next_prime_index = 1
def load_big_prime_array():
    global all_primes
    f = open("p500_primes.txt", "r")
    lines = f.readlines()
    f.close()
    for i in range(0, len(lines)):
        all_primes.append(int(lines[i]))



def next_min():
    global all_primes,next_prime_index,prime_arr
    next_p = [all_primes[next_prime_index],1]
    i = 0
    for p in prime_arr:
        new_multiplier = (p[0]) ** (p[1]+1)
        if new_multiplier < next_p[0]:
            prime_arr[i] = [p[0],p[1]+1]
            return
        i += 1
    next_prime_index += 1
    prime_arr.append(next_p)


def number_of_divisors():
    divisors = 1
    for p in prime_arr:
        divisors *= (p[1]+1)
    return divisors


def is_triangle_number():
    num = 1
    for p in prime_arr:
        num *= (p[0])**(p[1])
    print(prime_arr)
    print(num)
    print(number_of_divisors())
    sqt = math.sqrt(8*num + 1)
    if sqt == math.ceil(sqt):
        return 1
    return 0
   
def num_of_divisors(n):
    divisors_count = 0
    for i in range(1,n+1):
        if n % i == 0:
            divisors_count += 1
        
    return divisors_count  

def get_factors(n):
    factors = []
    tmp = n
    all_primes_counter = 0
    factors_prime_counter = -1
    while(1==1):
        if tmp < 2:
            break
        if tmp % all_primes[all_primes_counter] == 0:
            tmp /= all_primes[all_primes_counter]
            if len(factors)>0 and factors[factors_prime_counter][0] == all_primes[all_primes_counter]:
                factors[factors_prime_counter][1] += 1
            else:
                factors.append([all_primes[all_primes_counter],1])
                factors_prime_counter += 1
        else:
            all_primes_counter += 1

    return factors

def num_of_divisors_opt(n):
    factors = get_factors(n)
    print(factors)
    divs = 1
    for factor in factors:
        divs *= (factor[1]+1)
    
    return divs

load_big_prime_array()

"""
i = 1
while 1==1:
    next_min()
    i += 1
    if(is_triangle_number()==1):
        print("-------------")
    if(i == 15):
        break

print(prime_arr)
print(number_of_divisors())
for i in range(1,20):
    print('-------')
    print(i)
    print(((i*(i+1))/2))
    print(num_of_divisors(int((i*(i+1))/2)))

i = 1
while 1==1:
    if num_of_divisors_opt(int((i*(i+1))/2)) > 5:
        print(i)
        print(int((i*(i+1))/2))
        break
    i += 1

print(num_of_divisors_opt(100))
"""
i = 1
while 1==1:
    if num_of_divisors_opt(int((i*(i+1))/2)) > 500:
        print(i)
        print(int((i*(i+1))/2))
        break
    i += 1