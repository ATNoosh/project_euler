import sys
import math
import decimal
decimal.getcontext().prec = 100

fib = lambda n: int(math.sqrt(5)**(-1)*(((1+math.sqrt(5))/2)**int(n) - ((1-math.sqrt(5))/2)**int(n)))
fib2 = lambda n: int(n) if(n==1 or n==2) else fib(int(n)-1)+fib(int(n)-2)
def fibo():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b

for index, number in enumerate(fibo()):
    if len(str(number)) == 1000:
        print(index)
        break
print(number)
print(index)