"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

<21>  22  23  24 <25>
 20  <7>  8  <9> 10
 19   6  <1>  2  11
 18  <5>  4  <3> 12
<17> 16  15  14 <13>
I calculated according to 1 9 25 49 81 ... as reference number. In the base of n: 1 2 3 4 ..
So these numbers ar 1 9 25 49 ... (2n-1)^2
In each stage that square grows, 4 number will be added. On of them is from 1 9 25 49 ...
Others are these numbers:
(2n-1)^2 - 2(n-1)
(2n-1)^2 - 4(n-1)
(2n-1)^2 - 6(n-1)
After simplification:
The formula discovered as below
f(n) = f(n-1) + 16n^2 -28n + 16
f(1) = 1

After solving recurisve function:
f(n) = (16/3)n^3 - 6n^2 + (14/3)n - 3
"""

import sys
sys.setrecursionlimit(2000)

def reqursive_fun(n): return 1 if (n == 1) else reqursive_fun(n - 1) + 16 * (n**2) - 28 * n + 16
def simple_fun(n): return ((16 * (n ** 3)) + (14 * n))/3 - 6 * (n ** 2) - 3

print(simple_fun(10))
print(reqursive_fun(10))
