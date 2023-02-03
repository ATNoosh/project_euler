colatz = lambda n: n/2 if(n%2==0) else 3*n+1

def colatz_sequence(n):
    i = 0
    while 1==1:
        if n==1 :
            break
        i += 1
        n = colatz(n)
    return i

mx = 0
mxi = 0
for i in range(999999,1,-1):
    tmp = colatz_sequence(i)
    if mx<tmp:
        mx = tmp
        mxi = i

print(mx)
print(mxi)
