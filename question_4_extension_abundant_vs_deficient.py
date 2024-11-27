def abundant_vs_deficient(n):
    abundant, deficient = 0, 0
    for i in range(1,n+1):
        if S(i) > i:
            abundant =+ 1
        elif S(i) < i:
            deficient =+ 1
        else:
            abundant,deficient = abundant,deficient 
    return abundant, deficient


def abundant(n):
    c = abundant_vs_deficient(n)[0]
    return c

def deficient(n):
    c = abundant_vs_deficient(n)[1]
    return c

import matplotlib.pyplot as plt
import numpy as np

n_values = np.arange(1, 20000, 1)
a_values = abundant(n_values)
d_values = deficient(n_values)

plt.figure(figsize=(10,7))
plt.plot(n_values, a_values, label="abundant(n)", color="blue")
plt.plot(n_values, d_values, label="deficient(n)", color="red")
plt.title("Cumulative numbers of abundant and deficient numbers up to n plotted against n")
plt.xlabel("n")
plt.ylabel("abundant(n) & deficient(n)")
plt.legend()

plt.show()