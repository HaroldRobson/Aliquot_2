# answer to Related to perfect numbers are ‘abundant’ numbers with s(n) > n and ‘deficient’ numbers,
#where s(n) < n. A looping aliquot sequence should contain some of each. Compare the
#number of each up to a fixed value n.

import numpy as np
from question1 import S, SOE
import matplotlib.pyplot as plt
SOE(20000)

def abundant_deficient(n: int):


    abundant = []
    deficient = []
    a = 0
    d = 0

    for i in range(1, n + 1):
        if S(i) > i:
            a += 1
        if S(i) < i:
            d += 1
        abundant.append(a)
        deficient.append(d)

    return abundant, deficient

def plot_abundant_deficient(n):
    
    abundant, deficient = abundant_deficient(n)

    n_values = np.arange(1, n)
    plt.figure(figsize=(10, 7))
    plt.plot(n_values, abundant[1:], label="Abundant", color="blue")
    plt.plot(n_values, deficient[1:], label="Deficient", color="red")

    plt.text(n, abundant[n - 1], f'{abundant[n - 1]}', color="blue", fontsize=12, ha='left', va='bottom')
    plt.text(n, deficient[n - 1], f'{deficient[n - 1]}', color="red", fontsize=12, ha='left', va='bottom')
    plt.xlim(0, n + 2000)

    plt.title("Total numbers of abundant and deficient numbers up to n")
    plt.xlabel("n")
    plt.ylabel("Total")
    plt.legend()
    plt.show()
plot_abundant_deficient(20000)
