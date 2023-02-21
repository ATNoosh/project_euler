def is_permuted_multples(n):
    tmp1 = list(map(int,str(n)))
    tmp1.sort()
    tmp2 = list(map(int,str(n*2)))
    tmp2.sort()
    tmp3 = list(map(int,str(n*3)))
    tmp3.sort()
    tmp4 = list(map(int,str(n*4)))
    tmp4.sort()
    tmp5 = list(map(int,str(n*5)))
    tmp5.sort()
    tmp6 = list(map(int,str(n*6)))
    tmp6.sort()
    if tmp1 != tmp2:
        return False
    if tmp1 != tmp3:
        return False
    if tmp1 != tmp4:
        return False
    if tmp1 != tmp5:
        return False
    if tmp1 != tmp6:
        return False
    return True

i = 1
while 1==1:
    if is_permuted_multples(i):
        print(i)
        break
    i += 1

is_permuted_multples(14746)
