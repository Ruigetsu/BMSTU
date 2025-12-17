import os
from math import ceil

def parse_line(line):
    line = line.split(";")
    return line[0], int(line[1]), int(line[2]), line[3]

def input_data(number_of_rows): 
    
    data = []
    count_file_rows = 0
    max_num_1 = 0
    max_num_2 = 0
    max_str_1 = 0
    max_str_2 = 0
    while True:
        if count_file_rows == number_of_rows:
            max_num_1, max_num_2 = change_in_struct_format(max_num_1), change_in_struct_format(max_num_2)
            if max_num_1 is not None and max_num_2 is not None:
                return data, f"10s2I15s"
            else: 
                f"Одно из чисел слишком большое"
        
        prompt = f"\nЗапись {count_file_rows + 1}/{number_of_rows}: "
        row_input = input(prompt).strip()
        
        if len(row_input) == 0: 
            return data, f"10s2I15s"
    
        row = row_input.split()
        
        if len(row) != 4:
            print(f"Ошибка: должно быть 4 поля, введено {len(row)}")
            print("Повторите ввод")
            continue
        
        name, age, height, city = row
        
        errors = []
        if check_word(name) is None:
            errors.append("Имя должно содержать только буквы и дефис")
        
        if check_word(city) is None:
            errors.append("Город должен содержать только буквы и дефис")

        age = check_pos_int(age)
        if age is None:
            errors.append("Возраст должен быть положительным целым числом")

        height = check_pos_int(height)
        if height is None:
            errors.append("Рост должен быть положительным целым числом")

        if errors:
            print("Ошибки ввода:")
            for error in errors:
                print(f"  - {error}")
            print("Повторите ввод")
            continue
        
        count_file_rows += 1 
        data.append([name,age,height,city])

def check_field(field,value):
    field = check_pos_int(field)
    if field is not None and 1 <= field <= 4:
        if field in [1,4]: 
            if check_word(value) is not None:
                return field, value
            else:
                return None
        else:
            print(field, check_pos_int(value))
            value = check_pos_int(value) 
            if value is not None: 
                return field, value
            else: 
                return None
    else: 
        return None

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
            return int(num)
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
    path = os.path.normpath(path)  #для слешей на windows/macos
    return path

def safe_join(*paths):
    return os.path.join(*paths) #/bmstu + test.bin -> /bmstu/test.bin

def change_in_struct_format(num_bytes): 
    if num_bytes == 1:
        return "B"
    elif num_bytes == 2:
        return "H"
    elif num_bytes <= 4:
        return "I"
    elif num_bytes <= 8:
        return "Q"
    else:
        return None