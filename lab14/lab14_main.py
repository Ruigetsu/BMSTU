import os
from lab14_1 import choose_file
from lab14_2 import create_or_rewrite_file
from lab14_3 import print_db
from lab14_4 import insert_line
from lab14_5 import delete_line
from lab14_6 import find_one_field
from lab14_7 import find_two_fields
from lab14_functions import input_pos_int, input_data, safe_join, check_field, check_pos_int

menu_text = "\n1) Выбрать новый файл для работы\n\
2) Инициализировать базу данных\n\
3) Вывести содержимое базы данных\n\
4) Добавить запись в произвольное место базы данных\n\
5) Удалить произвольную запись из базы данных\n\
6) Поиск по одному полю\n\
7) Поиск по двум полям\n\
0) Выйти из программы"

def main():
    """Главная функция программы"""
    path_to_file = None
        
    while True:
        print(menu_text)
        
        if path_to_file:
            print(f"Текущий файл: {os.path.basename(path_to_file)}")
        else:
            print("Файл не выбран")
        
        inp = input("\nВведите номер команды: ").strip()
        
        match inp:
            case "1":
                result = choose_file()
                match result:
                    case None:
                        print("Файл не выбран")
                    case _:
                        path_to_file = result
            
            case "2":
                print("\n1 - Перезаписать текущий файл")
                print("2 - Создать новый файл в текущей директории")
                print("3 - Создать новый файл по указанному пути\n")
                
                create_choice = input("\nВыберите вариант: ").strip()
                
                number_of_rows = input_pos_int("Введите количество записей: ")
                data, format = input_data(number_of_rows)
                
                if len(data) == 0:
                    print("Данные не введены, операция отменена")
                    continue

                match create_choice:
                    case "1":
                        if path_to_file is not None:
                            create_or_rewrite_file(path_to_file, data, format)
                        else: 
                            print("Ошибка: необходимо сначала выбрать файл (пункт 1)")
                    
                    case "2":
                        name_for_file = input("Введите имя файла (без расширения): ").strip()
                        match name_for_file:
                            case "":
                                print("Ошибка: имя файла не может быть пустым")
                            case _:
                                path_to_file = safe_join(os.getcwd(), f"{name_for_file}.bin")
                                create_or_rewrite_file(path_to_file, data, format)
                    
                    case "3":
                        dir_path = input("Введите путь к директории: ").strip().strip('"').strip("'")
                        if os.path.isdir(dir_path):
                            name_for_file = input("Введите имя файла (без расширения): ").strip()
                            match name_for_file:
                                case "":
                                    print("Ошибка: имя файла не может быть пустым")
                                case _:
                                    path_to_file = safe_join(dir_path, f"{name_for_file}.bin")
                                    create_or_rewrite_file(path_to_file, data, format)
                        else:
                            print("Ошибка: указанная директория не существует")
                    
                    case _:                        
                        print("Ошибка: некорректный выбор")
            
            case "3":
                if path_to_file is not None:
                    print_db(path_to_file)
                else: 
                    print("Ошибка: необходимо сначала выбрать файл (пункт 1)")
            case "4":
                if path_to_file is None:
                    print("Ошибка: сначала выберите файл (пункт 1)")
                    continue
                while True:
                    pos = input("Введите позицию для вставки: ")
                    try:
                        pos = int(pos)
                        break
                    except ValueError: 
                        print("Вы ввели неверную позицию")

                data, _ = input_data(1)
                if len(data) > 0:
                    insert_line(path_to_file, pos, data)
                else:
                    print("Данные не введены")

            case "5": 
                if path_to_file is None:
                    print("Ошибка: сначала выберите файл (пункт 1)")
                    continue
                while True:
                    pos = input("Введите позицию для удаления: ")
                    try:
                        pos = int(pos)
                        break
                    except ValueError: 
                        print("Вы ввели неверную позицию")
                delete_line(path_to_file, pos)
            
            case "6":
                field = input("Введите номер столбца таблицы, по которому будет поиск: ")
                value = input("Введите значение по которому будет происходить поиск: ")
                checked_values = check_field(field,value)
                if checked_values is not None: 
                    field, value = checked_values
                    find_one_field(path_to_file, field, value)
                else: 
                    print("Вы ввели некоректный номер поля или некоректное значение для этого поля")

            case "7":
                field_1 = input("Введите номер первого столбца таблицы, по которому будет поиск: ")
                value_1 = input("Введите значение по которому будет происходить поиск в первом выбранном столбце: ")
                field_2 = input("Введите номер второго столбца таблицы, по которому будет поиск: ")
                value_2 = input("Введите значение по которому будет происходить поиск во втором выбранном столбце: ")
                checked_values_1 = check_field(field_1,value_1)
                checked_values_2 = check_field(field_2,value_2)
                if checked_values_1 is not None and checked_values_2 is not None: 
                    fields = [checked_values_1[0], checked_values_2[0]]
                    values = [checked_values_1[1], checked_values_2[1]]
                    find_two_fields(path_to_file, *fields, *values)
                else: 
                    print("Вы ввели некоректный номер поля или некоректное значение для этого поля")

            case "0":
                print("\nПрограмма завершена")
                break
            
            case _:
                print("Ошибка: некорректная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()