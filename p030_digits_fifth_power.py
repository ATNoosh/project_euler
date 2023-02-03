def sum_fifth_power(n):
    s = 0
    for st in str(n):
        s += int(st) ** 5
    return s

i=0
while 1==1:
    i += 1
    if i==sum_fifth_power(i):
        print(i)
    if i==999999:
        break 

print(i)