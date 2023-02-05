def square_digits(n):
    r = 0
    for d in str(n):
        r += int(d) ** 2
    return r

arr = [0]
arr = arr * 10000000
listShouldChange = []
def chains(n):
    global arr,listShouldChange
    if arr[n] > 0:
        for ii in listShouldChange:
            arr[ii] = arr[n]
        return arr[n]

    if n == 1 or n == 89:
        for ii in listShouldChange:
            arr[ii] = n
        return n

    
    listShouldChange.append(n)
    chains(square_digits(n))


for i in range(1,10000000):
    chains(i)
    listShouldChange = []
    print(i)
s89 = 0
for jjj in arr:
    if jjj == 89:
        s89 += 1

f = open("p092.txt","w")
f.write( '\n'.join(map(str,arr)))
f.close()
print(s89)#answer is 8581145


