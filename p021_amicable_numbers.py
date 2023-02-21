def sum_divisors(n):
    sum = 0
    for i in range(1,int(n/2) + 1):
        if n % i == 0:
            sum += i
    return sum

def is_amicable(n):
    tmp = sum_divisors(n)
    return n == sum_divisors(tmp) and tmp != n

sm = 0

for i in range(1,10000):
    if is_amicable(i):
        sm += i
        print(i)
        print(sum_divisors(i))

print(sm)