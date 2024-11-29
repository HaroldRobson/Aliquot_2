import json

"""
Made this to find the largest loop length from our json file and then return the loop length along with the 
loop itself. works v quickly - H
"""

with open('behaviour20000.json', 'r') as file:
    data = json.load(file)

from itertools import islice
def max_loop_length(n: int):
    loop_lengths = []
    loop_lengths_dict = {}
    for key, value in islice(data.items(), n):
        if value[0] == "Loop Detected":
            loop_lengths.append(len(value[1]))
            loop_lengths_dict[len(value[1])] = value[1]
    return max(loop_lengths), loop_lengths_dict[max(loop_lengths)]
print(max_loop_length(20000))
                              
