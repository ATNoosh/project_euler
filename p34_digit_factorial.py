import math

def sum_digit_factorial(n):
    n = str(n)
    s = 0
    for i in n:
        s += math.factorial(int(i))
    
    return s
count = 0
s = 0
for i in range(1,2177280):#after this number if all digit be 9, sum of factorials is less than the number
    tmp = sum_digit_factorial(i)
    if i == tmp:
        count += 1
        s += i
        print(i)

print(s)