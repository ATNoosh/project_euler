
def is_palindrome(n):
    return str(n)[::-1] == str(n)

mx = 0
isel = 0
jsel = 0
for i in range(100,999):
    for j in range(100,999):
        if str(i*j)[::-1] == str(i*j) and i*j>mx :
            mx = i*j
            isel = i
            jsel = j

print(isel)
print(jsel)
print(mx)