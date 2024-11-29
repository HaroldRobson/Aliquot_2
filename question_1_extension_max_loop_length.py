def max_loop_length(n):
    loop_lengths = []
    for i in json_file:
        if i[0] == "Loop Detected":
            c = len(i[1])
            loop_lengths.append(c)
    max_length = max(loop_lengths)
    return max_length