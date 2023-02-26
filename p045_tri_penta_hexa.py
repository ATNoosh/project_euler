def triangle(n):
    return n*(n+1)/2
def penta(n):
    return n*(3*n-1)/2
def hexa(n):
    return n*(2*n-1)

t = 286
p = 166
h = 144
while 1==1:
    if triangle(t) == penta(p) and penta(p) == hexa(h):
        print(t)
        print(p)
        print(h)
        print(triangle(t))
        break
    if triangle(t) == min([triangle(t),penta(p),hexa(h)]):
        t += 1
        continue
    if penta(p) == min([triangle(t),penta(p),hexa(h)]):
        p += 1
        continue
    if hexa(h) == min([triangle(t),penta(p),hexa(h)]):
        h += 1
        continue
    