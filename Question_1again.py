import gmpy2
from gmpy2 import ceil
from gmpy2 import sqrt
prime_dict = {}
onlyprimes = []
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
 
 print(S(2500))
