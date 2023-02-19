import math
from itertools import permutations
main_str = ["0","1","2","3","4","5","6","7","8","9"]
que = []
def get_nth_permutation(n):
    global main_str,que
    counter = len(main_str) - 1
    current_num = 0
    reminded = n
    while 1==1:
        digit = math.floor(reminded/math.factorial(counter))
        que.append(digit)
        reminded =  (reminded - digit * math.factorial(counter))
        print(digit)
        print(reminded)
        counter -= 1
        if counter == 0:
            break

#get_nth_permutation(1000000)
#print(que)
counter = 0
prm = permutations(main_str)
for i in list(prm):
    counter += 1
    if(counter == 1000000):
        print(counter)
        print(i)