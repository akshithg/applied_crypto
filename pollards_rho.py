'''
Pollard's Rho Algorithm
'''
import sys
from fractions import gcd

def g(x):
    return (x*x) + 1

def factorize(n):
    x = 2
    y = 2
    d = 1

    while d==1:
        x = g(x)
        y = g(g(x))
        d = gcd(abs(x-y), n)

    if d == n:
        print("fail")
    else:
        print(d)


if __name__ == "__main__":
    factorize(int(sys.argv[-1]))
