from math import comb 

def C(n):
    return comb(2*n, n)//(n+1)


n = int(input())
3
print(C(n))