from question_1 import SOE, S
import gmpy2
from gmpy2 import ceil
from gmpy2 import sqrt

from gmpy2 import is_zero
onlyprimes = []
prime_dict = {}

SOE(100000)

def preimage(n, L):
    preImageArray = []
    if isinstance(n, gmpy2.mpz):
        for i in range(1, L):  # L is limit for checking for preimage - may not in fact include the entire preimage of S(n)
            if is_zero(S(i) - n):
                preImageArray.append(i)
        return preImageArray
    else:
        n = gmpy2.mpz(n)
        return preimage(n, L)

def preImageSizes(m, L):# computes the preimages for integers up to m, with the Limit for checking being L
    preImageSizeArray= []
    for j in range(m):
        print(j)# this function is very slow so i left this print(j) in for peace of mind that it is in fact working
        preImageSizeArray.append(len(preimage(j, L)))
    return preImageSizeArray
#print(preImageSizes(50, 1000))
