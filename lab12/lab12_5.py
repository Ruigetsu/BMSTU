import re

def lab12_5(array,word_to_replace,word): 
    new_array = []
    count = 0
    for i in range(len(array)): 
        if len(array[i]) == 0: 
            continue
        count += len(re.findall(rf"\b{word_to_replace}\b", array[i]))
        new_str = re.sub(rf"\b{word_to_replace}\b", word, array[i])
        new_array.append(new_str)

        """for match in re.finditer(rf"{word}",array[i]):
            start = match.start()
            end = start + len(word) 
            print(start,end)
            array[i] = array[i][:start] + array[i][end:]
            print(array[i])"""
        
    return new_array,count