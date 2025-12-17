import os

def parse_line(line):
    line = line.split(";")
    return line[0], int(line[1]), int(line[2]), line[3]

def input_data(number_of_rows): 
    
    data = []
    count_file_rows = 0
    
    while True:
        if count_file_rows == number_of_rows: 
            return data
        
        prompt = f"\nЗапись {count_file_rows + 1}/{number_of_rows}: "
        row_input = input(prompt).strip()
        
        if len(row_input) == 0: 
            return data
        
        row = row_input.replace(";", "").split()
        
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
        
        if check_pos_int(age) is None:
            errors.append("Возраст должен быть положительным целым числом")
            
        if check_pos_int(height) is None:
            errors.append("Рост должен быть положительным целым числом")
        
        if errors:
            print("Ошибки ввода:")
            for error in errors:
                print(f"  - {error}")
            print("Повторите ввод")
            continue
        
        count_file_rows += 1 
        data.append(row)


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
    return os.path.join(*paths) #Пример: /bmstu + test.csv -> /bmstu/test.csv



