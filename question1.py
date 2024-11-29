import gmpy2
from gmpy2 import ceil
from gmpy2 import sqrt
prime_dict = {}
onlyprimes = []
#this is the answer to (core) Write a function to calculate s(n). (Note: In week 9 we’ll see a method that
#exploits the fact that the sum of all divisors is a multiplicative function.)
# it uses gmpy2 and also inlcudes extension 6 using the sieve of Eratosthenes (SOE(n)). the file S_bad.py is an example of the function using numpy instead of gmpy2 and can be used to sho
# the slowness of numpy as opposed to gmpy2 
# When using S from an import please include the followning line:
# from question1 import S
def SOE(n):
    for i in range(n):
        prime_dict[i] = True
    prime_dict[0] = False
    prime_dict[1] = False
    for i in range(2, int(ceil(sqrt(n)))+1):
        if prime_dict[i]:
            onlyprimes.append(i)
            for j in range(i*i, n, i):
                prime_dict[j] = False
    for k in range(int(ceil(sqrt(n)))+1, n):
        if prime_dict[k]:
            onlyprimes.append(gmpy2.mpz(k))
def S(n): # requires n to be of form gmpy2.mpz(x) where x is an integer
    if len(onlyprimes) >= 1:
        if n < 0:
            print("input to S is negative")
            return None
        if n < gmpy2.mpz(0):
            print("inout to S is negative")
            return None
        if n == gmpy2.mpz(1):
            return gmpy2.mpz(0)
        if n == gmpy2.mpz(0):
            return gmpy2.mpz(0)
        if int(onlyprimes[-1]) >= int(sqrt(n)):
            productoffactors = gmpy2.mpz(1)
            sumoffactors = gmpy2.mpz(1)
            while productoffactors != n:
                for p in onlyprimes:
                    if int(gmpy2.f_mod(gmpy2.mpz(n), p)) == 0:
                        power = p
                        while power <= n and int(gmpy2.f_mod(n, power*p)) == 0:
                                power *= p
                        sumoffactors *= (power*p - gmpy2.mpz(1))/ (p - gmpy2.mpz(1))
                        productoffactors *= power
            if sumoffactors == 1:
                sumoffactors = 0
            return gmpy2.mpz(sumoffactors- n)

        else:
            print("onlyprimes hasnt got large enough: recreating the sieve of Eratosthenes")
            SOE(n ** gmpy2.mpz(5))
            return S(n)

    else:
        print("onlyprimes hasnt got large enough: recreating the sieve of Eratosthenes")
        SOE(n * gmpy2.mpz(5))
        return S(n)
