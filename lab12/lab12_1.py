"""import re
def lab12_1(array):
    for i in range(len(array)):
        first_not_space = re.search(r"[^ ]",array[i])
        array[i] = array[i][first_not_space.start():]
    return array"""

def lab12_1(array): 
    for i in range(len(array)): 
        indx_first_not_space = 0
        for j in range(len(array[i])): 
            if array[i][j] != " ": 
                indx_first_not_space = j
                break
        array[i] = array[i][indx_first_not_space:]
    return array