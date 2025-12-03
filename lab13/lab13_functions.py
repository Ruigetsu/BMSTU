import os

def choose_file():
    while True:
        file_path = input("Введите полный путь к файлу: ").strip().strip('"')
        if os.path.exists(file_path): #проверка существования файла
            if os.path.isfile(file_path): #проверка что файл а не директория
                if file_path[-4:] == ".csv":
                    abs_path = os.path.abspath(file_path)
                    print(f"Файл .csv найден: {abs_path}")
                    return abs_path
                else: 
                    print(f"Файл найден, но у фала расширение .{file_path.split(".")[-1]}")
            else:
                print("Это не файл, а директория. Попробуйте снова.")
        else:
            print("Файла не существует. Попробуйте снова.")

def create_new_file(data,file_name): 
    curr_dir = os.getcwd()
    file_path = curr_dir + "\\lab13" + f"\\{file_name}.csv"
    print(file_path)
    with open(file_path, "w", encoding="utf-8-sig") as file: # "w" - write или перезаписать
        for row in data:
            file.write(";".join(row) + "\n")

def check_word(word): 
    for i in word: 
        if i.isalpha(): 
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

def input_data(number_of_rows): 
    print("Введите данные для таблицы: \n\
ИМЯ | Возраст | Рост | Город проживания")
    data = [["Имя", "Возраст", "Рост", "Город проживания"]]
    count_rows = 0
    while True:
        if count_rows == number_of_rows: 
            break
        row = input("Введите строчку таблицы через пробел: ").split()

        if len(row) == 4:
            name, age, height, city = row
            if check_word(name) is None or check_word(city) is None or check_pos_int(age) is None or check_pos_int(height) is None: 
                print(check_word(name),check_word(city),check_pos_int(age),check_pos_int(height))
                print("Ошибка ввода!")
                continue
            else: 
                count_rows += 1 
                data.append(row)
        else: 
            print("В строке доложно быть 4 поля!")
    return data


data = input_data(1)
file_name = input("Введите названия файла: ")
#choose_file()

create_new_file(data, file_name)