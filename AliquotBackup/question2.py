# Joseph's way of making an aliquot sequence

from question1 import S

def A(k):
    n = 30
    i = 10**9
    sequence = [k]
    for j in range(1,n+1):
        if k == S(k) or k > i:
            break
        elif k == 0:
            sequence.append(k)
            break
        else:
            k = int(S(k))
            sequence.append(k)
    return sequence
