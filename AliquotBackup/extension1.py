import json
with open('behaviour20000.json', 'r') as file:
    data = json.load(file)

from itertools import islice


    
def max_loop_length(n):
    loop_lengths = []
    loop_dict = {}
    if not isinstance(n, int) or not (1 <= n <= 19999):
        print("Input error")
        return None
    else:
        loop_lengths = []
        for key, value in islice(data.items(), n):
            length = len(value[1])
            loop_lengths.append(length)
            loop_dict[length] = value[1] 
        if loop_lengths == []:
            print("No loops detected")
            return None
        else:
            return max(loop_lengths), loop_dict[max(loop_lengths)]
print(max_loop_length(19999))        
