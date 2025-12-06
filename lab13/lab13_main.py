import os
from lab13_1 import choose_file
from lab13_2 import input_data, create_or_rewrite_file
from lab13_3 import print_db
from lab13_4 import append_data
from lab13_functions import input_pos_int

menu_text = "1) Выбрать новый файл для работы\n\
2) Инициализировать базу данных\n\
3) Вывести содержимое базы данных\n\
4) Добавить запись в конец базы данных\n\
5) Поиск по одному полю\n\
6) Поиск по двум полям"

path_to_file = None
while True:
    print(menu_text)
    inp = input("Введите номер задания: ")
    match inp: 
        case "1": 
            while True: 
                path_to_file = choose_file()
                if path_to_file is not None: 
                    break
                else: 
                    print("Вы ввели некоректные значения")
        case "2":
            create_or_rewrite = input("Введите 1 если хотите перезаписать уже выбранный файл или 2 чтобы создать новый в текущей папке: ")
            number_of_rows = input_pos_int("Введите количество строк таблицы: ")
            data = input_data(number_of_rows)
            match create_or_rewrite:
                case "1":
                    if path_to_file is not None:
                        name_for_file_creation = os.path.basename(path_to_file)
                        create_or_rewrite_file(data, name_for_file_creation)
                    else: 
                        print("Необходимо сначала выбрать файл")
                case "2": 
                    name_for_file_creation = input("Введите имя файла без расширения: ")
                    path_to_file = os.getcwd() + f"\\{name_for_file_creation}.csv"
                    print(path_to_file)
                    create_or_rewrite_file(data, path_to_file)
                case _:
                    print("Вы ввели несуществующую значение команды")
            
        case "3": 
            print_db(path_to_file)
        
        case "4": 
            number_of_rows = input_pos_int("Введите количество строк таблицы: ")
            data = input_data(number_of_rows)
            append_data(path_to_file, data)

        case _:
            break

