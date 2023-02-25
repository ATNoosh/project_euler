
prime_arr = [[2, 1]]
all_primes = []
next_prime_index = 1
def load_big_prime_array():
    global all_primes
    f = open("p500_primes.txt", "r")
    lines = f.readlines()
    f.close()
    for i in range(0, len(lines)):
        all_primes.append(int(lines[i]))



def read_primes():
    global all_primes
    f = open("all_primes.txt")
    all_primes = f.readlines()
    f.close()
    all_primes = list(map(int,all_primes[0].split(",")))

def get_factors(n):
    factors = []
    tmp = n
    all_primes_counter = 0
    factors_prime_counter = -1
    while(1==1):
        if tmp < 2:
            break
        if tmp % all_primes[all_primes_counter] == 0:
            tmp /= all_primes[all_primes_counter]
            if len(factors)>0 and factors[factors_prime_counter][0] == all_primes[all_primes_counter]:
                factors[factors_prime_counter][1] += 1
            else:
                factors.append([all_primes[all_primes_counter],1])
                factors_prime_counter += 1
        else:
            all_primes_counter += 1

    return factors

def get_radical(n):
    factors = get_factors(n)
    res = 1
    for fac in factors:
        res*=fac[0]
    return res
def sort_arr(arr):
    print("---")
    for i in range(0,len(arr)-1):
        print(i)
        for j in range(i+1,len(arr)):
            if arr[i][0]>arr[j][0]:
                tmp=arr[i]
                arr[i]=arr[j]
                arr[j]=tmp
    return arr
read_primes()

arr = []
print(61)
for i in range(1,100001):
    print(i)
    arr.append([get_radical(i),i])
sort_arr(arr)


print(arr[10000-1])
print(arr[10000])
print(arr[10000+1])

ff=open('p124output.txt','w')
ff.writelines('\n'.join(map(str,arr)))
ff.close()