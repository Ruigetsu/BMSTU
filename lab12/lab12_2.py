def lab12_2(array): 
    max_len = len(max(array, key = len).strip())
    """for i in range(len(array)):
        words = array[i].split()
        len_current = sum(len(x) for x in words) + len(words) - 1
        if len_current != max_len:
            new_string = words[-1]
            diff = max_len - len_current
            for j in range(len(words) - 2,-1,-1): 
                new_string = words[j] + " "+ new_string
            array[i] = " "* diff + new_string
        else: 
            continue
    return array"""

    for i in range(len(array)):
        array[i] = array[i].strip().rjust(max_len)
    return array
    