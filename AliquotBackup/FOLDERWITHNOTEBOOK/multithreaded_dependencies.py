'''
 (core) For each k < 20000 try to classify it according to the end state of the aliquot
sequence starting at k. It should either terminate at zero, enter a loop or be unknown
(you might want to distinguish between the cases where the calculation was cut short
because you reached term n and those where the sequence exceeded i).
'''
# answer to question 4. saves the 20000 behaviours in a json file which should be used later to prevent recalculations:
import json
import os
from concurrent.futures import ProcessPoolExecutor, TimeoutError
import concurrent# I had a read into using multithreaded python for computationally heavy tasks(such as this). - H
def S_for_multithreading(n):
    if n == 0: 
        return 0
    if n < 0:
        return 0
    else:

        return sum(i for i in range(1, n // 2 + 1) if n % i == 0) # multithreading requires function to affect no global variables





def detect_aliquot_sequence_behaviour_for_multithreading(n):
    sequence = [n]
    visited = set()

    current = n 
    i = 0
    while current != 0:
        if i > 10:
            return "non terminating", sequence # if a sequence has more than 100 terms it is probably not going to terminate
        if current in visited:
            # Loop detected
            loop_start_index = sequence.index(current)
            loop = sequence[loop_start_index:]
            return "Loop Detected", loop #If we detect a loop, we return string "Loop Detected" and the sequence
        visited.add(current)
        sequence.append(current)
        current = S_for_multithreading(current)
        i += 1
    # If we reach 0, it means the sequence terminates without a loop
    return "Terminates", sequence


"""
THIS WAS VERY INTERESTING:
    after a lot of work i got the jsonbehaviourmaker function to work in a multithreaded way. This does not 
    exactly result in the dictionary being filled up in order: try running jsonbehaviourmaker for a smallish 
    number like 200 and you'll see that the behaviours for numbers like 168 which are non terminating are 
    actually filled up last - a direct result of the concurrent multithreading running quicker tasks concurrently to harder ones
    

    
"""


def jsonbehaviourmaker(n: int, FILENAME: str):
    behaviour_dict = {}
    # Create the executor with a limited number of cores.  
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor: # I have ten cores you may have less and need to adjust accordingly. run corecheker.py to find out!
        futures = {
            executor.submit(detect_aliquot_sequence_behaviour_for_multithreading, i): i for i in range(1, n + 1)}
        total_tasks = len(futures)
        completed_tasks = 0
        for future in concurrent.futures.as_completed(futures):
            completed_tasks += 1
            i = futures[future]
            try:
               behaviour_dict[i] = future.result(timeout=0.5)
            except TimeoutError:
                behaviour_dict[i] = "probably non-terminating" # probably unneccessary but just in case it gets stuck on a sequence it will assume the sequence is non terminating. 
            except Exception as e:
                behaviour_dict[i] = f"error: {e}"

            # Track progress
            print(f"Progress: {completed_tasks}/{total_tasks} ({(completed_tasks / total_tasks) * 100:.2f}%)")

    # Save results to a file
    file = FILENAME + ".json"
    with open(file, "w") as outfile:
        json.dump(behaviour_dict, outfile)
    print("successfully made " + file)

#jsonbehaviourmaker(20000)a
if __name__ == "__main__":

    jsonbehaviourmaker(20000, "behaviour20000")
