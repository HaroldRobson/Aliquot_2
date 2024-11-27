#This is the function of sum_proper_divisors function, you can change it to your own function
import gmpy2
from gmpy2 import ceil
import json
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
    if not isinstance(n, gmpy2.mpz):
        n = gmpy2.mpz(n)
    if n <= 1:
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
        SOE(gmpy2.mpz(1)+n)
        return S(n)
SOE(10000000)
def sum_proper_divisors(n):

    """Return the sum of proper divisors of n."""
    if n < 2:
        return 0  # Proper divisors for 1 and 0 lead to termination
    total = 1  # Start with 1 because it's a divisor for all n > 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def detect_aliquot_sequence_behavior(start):
    """Return True if the aliquot sequence of start enters a loop, False if it terminates.
    Also, returns the sequence and any detected loop or terminating sequence.
    """
    visited = set()  # Keep track of numbers seen in the sequence
    sequence = []  # To store the sequence of values

    # while loop to check if the start_value enter the loop
    current = start
    i = 0
    while current != 0:
        if i > 30:
            return "non terminating" # if a sequence has more than 100 terms it is probably not going to terminate
        if current in visited:
            # Loop detected
            loop_start_index = sequence.index(current)
            loop = sequence[loop_start_index:]
            return "Loop Detected", loop #If we detect a loop, we return string "Loop Detected" and the sequence
        visited.add(current)
        sequence.append(current)
        current = sum_proper_divisors(current)
        i += 1
    # If we reach 0, it means the sequence terminates without a loop
    return "Terminates", sequence

# Example usage of number that enter the loop
start_value = 220  # You can test with different starting values
behavior, result = detect_aliquot_sequence_behavior(start_value)
if behavior == "Loop Detected":
    print(f"A loop is detected in the aliquot sequence: {result}")
else:
    print(f"The sequence terminates without a loop: {result}")

# Example of number that not enter the loop
'''
start_value = 100  # You can test with different starting values
behavior, result = detect_aliquot_sequence_behavior(start_value)
if behavior == "Loop Detected":
    print(f"A loop is detected in the aliquot sequence: {result}")
else:
    print(f"The sequence terminates without a loop: {result}")

#Example of a number enter the "Sociable Chain" Loop
start_value = 12496  # You can test with different starting values
behavior, result = detect_aliquot_sequence_behavior(start_value)
if behavior == "Loop Detected":
    print(f"A loop is detected in the aliquot sequence: {result}")
else:
    print(f"The sequence terminates without a loop: {result}")

#Example of the Perfect number
start_value = 6  # You can test with different starting values
behavior, result = detect_aliquot_sequence_behavior(start_value)
if behavior == "Loop Detected":
    print(f"A loop is detected in the aliquot sequence: {result}")
else:
    print(f"The sequence terminates without a loop: {result}")
'''
behaviour_dict = {}
for i in range(1, 20000):
    print(i)
    behaviour_dict[i] = detect_aliquot_sequence_behavior(i)

print(behaviour_dict)

with open("behaviour.json", "w") as outfile: 
    json.dump(behaviour_dict, outfile)
