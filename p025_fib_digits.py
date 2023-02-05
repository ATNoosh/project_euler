import sys
import math
import decimal
decimal.getcontext().prec = 100

fib = lambda n: int(math.sqrt(5)**(-1)*(((1+math.sqrt(5))/2)**int(n) - ((1-math.sqrt(5))/2)**int(n)))

i = 50
while 1 == 1:
    f = fib(i)
    if len(str(f))>1000:
        break
    s = f
    i += 1

print(fib(50))