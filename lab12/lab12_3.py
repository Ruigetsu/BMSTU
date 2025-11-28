def lab12_3(array): 
    max_len = len(max(array, key = len))
    new_array = []

    for line in array:
        words = line.split()
        if len(words) == max_len:
            # Если одно слово или пустая строка - просто добавляем
            new_array.append(line)
        elif len(words) <= 1: 
            new_array.append(line.center(max_len))
        else:
            # Вычисляем пробелы для выравнивания
            total_spaces = max_len - sum(len(word) for word in words)
            spaces_between = total_spaces // (len(words) - 1)
            extra_spaces = total_spaces % (len(words) - 1)
            
            # Собираем строку с равномерными пробелами
            new_string = words[0]
            count_extra_spaces = 0
            for i in range(1, len(words)):
                if count_extra_spaces < extra_spaces: 
                    count_extra_spaces += 1
                    spaces = spaces_between + 1
                else: 
                    spaces = spaces_between
                new_string += ' ' * spaces + words[i]
            
            new_array.append(new_string)
    
    return new_array

