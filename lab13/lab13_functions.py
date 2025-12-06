import os

def print_lists(array, string): 
    str_to_print = string
    for i, j in enumerate(array): 
        str_to_print += f"{i+1}) {j}\n"
    return str_to_print
    
def check_word(word): 
    if not word:  # Проверка на пустую строку
        return None
    for i in word: 
        if i.isalpha() or i == "-": 
            continue
        else: 
            return None
    return word

def check_pos_int(num):
    try:
        if str(int(num)) == num and int(num) > 0: 
            return num
        else:
            return None
    except: 
        return None 

def input_pos_int(prompt): 
    while True:
        num = check_pos_int(input(prompt))
        if num is None: 
            print("Вы ввели некорректное значение числа!")
        else: 
            return int(num)

def normalize_path(path):
    path = path.strip().strip('"').strip("'")
    path = os.path.normpath(path)  #для слешей на windows/mac os
    return path

def safe_join(*paths):
    return os.path.join(*paths)