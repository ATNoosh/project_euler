import sys
import math

fib = lambda n: int(n) if(n==1 or n==2) else fib(int(n)-1)+fib(int(n)-2)


i = 1
e = 0
o = 0
s = 0
while 1 == 1:
    f = fib(i)
    if f>4000000:
        break
    e += f if(f%2==0) else 0
    o += f if(f%2==1) else 0
    s += f
    i += 1

print(e)
print(o)
print(s)