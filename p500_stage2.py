
prime_arr = []


def load_big_prime_array():
    global prime_arr
    f = open("p500_p.txt", "r")
    lines = f.readlines()
    f.close()
    for i in range(0, len(lines)):
        prime_arr.append(get_integers(lines[i]))


def get_integers(line):
    return list(map(int, line.split(':')))


def rem(begin, end, div):
    if begin + 1 == end:
        return ((prime_arr[begin][0] ** prime_arr[begin][1]) * (prime_arr[end][0] ** prime_arr[end][1])) % div
    if begin == end:
        return (prime_arr[begin][0] ** prime_arr[begin][1]) % div
    middle = int((begin + end)/2)
    tmp = (rem(begin, middle, div)*rem(middle+1, end, div)) % div
    return tmp


load_big_prime_array()
print(rem(0, len(prime_arr)-1, 500500507))  # output is 35407281
