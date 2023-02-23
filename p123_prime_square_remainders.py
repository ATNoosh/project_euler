all_primes = ""
def read_primes():
    global all_primes
    f = open("all_primes.txt")
    all_primes = f.readlines()
    f.close()
    all_primes = list(map(int,all_primes[0].split(",")))

def get_reminder(n):
    return (((all_primes[n-1]-1) ** n ) + ((all_primes[n-1]+1) ** n )) % (all_primes[n-1]**2)

read_primes()
i = 7037
while 1==1:
    if(get_reminder(i)>(10000000000)):
        print('final:')
        print(i)
        break
    print(i)
    i += 1

print(get_reminder(3))
