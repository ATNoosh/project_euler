import itertools

def is_sub_div(item):
    if int(''.join(map(str, item))[1:4])%2!=0:
        return 0
    if int(''.join(map(str, item))[2:5])%3!=0:
        return 0
    if int(''.join(map(str, item))[3:6])%5!=0:
        return 0
    if int(''.join(map(str, item))[4:7])%7!=0:
        return 0
    if int(''.join(map(str, item))[5:8])%11!=0:
        return 0
    if int(''.join(map(str, item))[6:9])%13!=0:
        return 0
    if int(''.join(map(str, item))[7:10])%17!=0:
        return 0
    return 1
fff = 0
for item in list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])):

    if int(''.join(map(str, item))) < 1023456789:
        continue
    if is_sub_div(item) > 0:
        fff += int(''.join(map(str, item)))

print(fff)