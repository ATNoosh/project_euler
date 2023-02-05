import math
def num_of_divs(n):
    d = 0
    for i in range(1 , n / 2 + 1):
        if n % i == 0:
            d += 1
    return d
arr = [2,3,5,7,11,13,17,19]
def num_of_divs_greater_than500(n):
    d = 0
    for i in arr:
        if n % i != 0:
            return 0
    return 1

i = 4400
s = 0
while 1==1:
    i += 1
    s = i*(i+1)/2
    if num_of_divs_greater_than500(s) > 0:
        break
    if i>1000000: break
    
print(i)
print(num_of_divs(i))
print(num_of_divs_greater_than500(i))
print(num_of_divs_greater_than500(241604*(241604+1)/2))
print((241604*(241604+1)/2))
print(num_of_divs(241604*(241604+1)/2))