# example of using numpy instead of gmpy2. this should be used in the jupyter notebook to demonstrate the time differences (ie using %timeit)
import numpy as np
import math
prime_dict = {}
onlyprimes = []
def S_badOE_bad(n):
    for i in range(n):
        prime_dict[i] = True
    prime_dict[0] = False
    prime_dict[1] = False
    for i in range(2, int(np.ceil(np.sqrt(n)) + 1)):
        if prime_dict[i]:
            onlyprimes.append(i)
            for j in range(i*i, n, i):
                prime_dict[j] = False
    for k in range(int(np.ceil(np.sqrt(n))+1), n):
        if prime_dict[k]:
            onlyprimes.append(k)
def S_bad(n):
    if len(onlyprimes) >= 1:
        if onlyprimes[-1] >= np.sqrt(n):
            productoffactors = 1
            sumoffactors = 1
            while productoffactors != n:
                for p in onlyprimes:
                    if n % p == 0:
                        power = p
                        while power <= n and n % (power * p) == 0:
                                power *= p
                        sumoffactors *= (power*p - 1)/ (p - 1)
                        productoffactors *= power
            if sumoffactors == 1:
                sumoffactors = 0
            return sumoffactors- n
        else:
            print("onlyprimes hastnt got large enough: recreating the sieve of Eratosthenes")
            S_badOE_bad(n*5)
            return S_bad(n)

    else:
        print("onlyprimes hastnt got large enough: recreating the sieve of Eratosthenes")
        S_badOE_bad(n*5)
        return S_bad(n)
print(S_bad(2000))    
