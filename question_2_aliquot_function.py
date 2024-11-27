def A(k):
    if k < 1:
        print("Error: no aliquot sequence exists for this input")
        return None
    n = 30
    i = 10**9
    sequence = [k]
    for j in range(n-1):
        if k == S(k):
            break
        else:
            k = S(k)
            sequence.append(k)
            if k == 0:
                sequence.append(k)
                break
            else:
                if k > i:
                    break
    return sequence