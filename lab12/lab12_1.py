def lab12_1(array): 
    for i in range(len(array)): 
        array[i] = array[i].strip()
    return array

    """for i in range(len(array)): 
        words = array[i].split()
        new_string = words[0]
        for j in range(1,len(words)): 
            new_string += " " + words[j]
        array[i] = new_string  
    return array"""