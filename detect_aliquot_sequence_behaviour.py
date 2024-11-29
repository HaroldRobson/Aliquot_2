
from Question_1again import SOE, S
onlyprimes = []
prime_dict = {}  
def detect_aliquot_sequence_behaviour(start):
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
        current = S(current)
        i += 1
    # If we reach 0, it means the sequence terminates without a loop
    return "Terminates", sequence
print(detect_aliquot_sequence_behaviour(2500))
