

def is_palindrome(n):
    return str(n)[::-1] == str(n)
s = 0
for i in range(1,1000000 - 1):
    if is_palindrome(i) and is_palindrome(bin(i).replace("0b", "")):
        s += i

print(s)