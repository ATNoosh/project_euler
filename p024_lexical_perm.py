import math
from itertools import permutations
main_str = ["0","1","2","3","4","5","6","7","8","9"]
tmp_main_str = main_str.copy()
str = []
def get_nth_permutation(n):

    global main_str,que
    counter = len(main_str) - 1
    digit = 0
    reminded = n - 1 # because we need nth

    while 1==1:
        digit = math.floor(reminded/math.factorial(counter))
        str.append(tmp_main_str[digit])
        tmp_main_str.pop(digit)
        reminded =  (reminded - digit * math.factorial(counter))
        
        if counter == 0:
            break
        counter -= 1
    
nth = math.factorial(10)
get_nth_permutation(nth)
print(str)
#below is using lib
counter = 0
prm = permutations(main_str)
for i in list(prm):
    counter += 1
    if(counter == nth):
        print(counter)
        print(i)