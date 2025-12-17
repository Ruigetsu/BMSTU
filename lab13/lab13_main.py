import os
from lab13_1 import choose_file
from lab13_2 import create_or_rewrite_file
from lab13_3 import print_db
from lab13_4 import append_data
from lab13_5 import find_one_field
from lab13_6 import find_two_fields
from lab13_7 import sort_one_field
from lab13_8 import sort_two_fields
from lab13_functions import input_pos_int, input_data, safe_join, check_field, check_pos_int

menu_text = "\n1) Выбрать новый файл для работы\n\
2) Инициализировать базу данных\n\
3) Вывести содержимое базы данных\n\
4) Добавить запись в конец базы данных\n\
5) Поиск по одному полю\n\
6) Поиск по двум полям\n\
7) Сортировка по одному полю\n\
8) Сортировка по двум полям\n\
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
                data = input_data(number_of_rows)
                
                if len(data) == 0:
                    print("Данные не введены, операция отменена")
                    continue
                
                match create_choice:
                    case "1":
                        if path_to_file is not None:
                            create_or_rewrite_file(data, path_to_file)
                        else: 
                            print("Ошибка: необходимо сначала выбрать файл (пункт 1)")
                    
                    case "2":
                        name_for_file = input("Введите имя файла (без расширения): ").strip()
                        match name_for_file:
                            case "":
                                print("Ошибка: имя файла не может быть пустым")
                            case _:
                                path_to_file = safe_join(os.getcwd(), f"{name_for_file}.csv")
                                create_or_rewrite_file(data, path_to_file)
                    
                    case "3":
                        dir_path = input("Введите путь к директории: ").strip().strip('"').strip("'")
                        if os.path.isdir(dir_path):
                            name_for_file = input("Введите имя файла (без расширения): ").strip()
                            match name_for_file:
                                case "":
                                    print("Ошибка: имя файла не может быть пустым")
                                case _:
                                    path_to_file = safe_join(dir_path, f"{name_for_file}.csv")
                                    create_or_rewrite_file(data, path_to_file)
                        else:
                            print("Ошибка: указанная директория не существует")
                    
                    case _:                        
                        print("Ошибка: некорректный выбор")
            
            case "3":
                print_db(path_to_file)
            
            case "4":
                if path_to_file is None:
                    print("Ошибка: сначала выберите файл (пункт 1)")
                    continue
                
                number_of_rows = input_pos_int("Введите количество добавляемых записей: ")
                data = input_data(number_of_rows)
                
                if len(data) > 0:
                    append_data(path_to_file, data)
                else:
                    print("Данные не введены")
            
            case "5":
                field = input("Введите номер столбца таблицы, по которому будет поиск: ")
                value = input("Введите значение по которому будет происходить поиск: ")
                checked_values = check_field(field,value)
                if checked_values is not None: 
                    field, value = checked_values
                    find_one_field(path_to_file, field, value)
                else: 
                    print("Вы ввели некоректный номер поля или некоректное значение для этого поля")
            
            case "6":
                field_1 = input("Введите номер первого столбца таблицы, по которому будет поиск: ")
                value_1 = input("Введите значение по которому будет происходить поиск в первом выбранном столбце: ")
                field_2 = input("Введите номер второго столбца таблицы, по которому будет поиск: ")
                value_2 = input("Введите значение по которому будет происходить поиск во втором выбранном столбце: ")
                checked_values_1 = check_field(field_1,value_1)
                checked_values_2 = check_field(field_2,value_2)
                if checked_values_1 is not None and checked_values_2 is not None: 
                    fields = [checked_values_1[0], checked_values_2[0]]
                    values = [checked_values_1[1], checked_values_2[1]]
                    find_two_fields(path_to_file, fields, values)
                else: 
                    print("Вы ввели некоректный номер поля или некоректное значение для этого поля")
            case "7": 
                field = check_pos_int(input("Введите номер столбца таблицы, по которому будет сортировка: "))
                if field is None:
                    print("Вы ввели некоректный номер столбца таблицы")
                elif field < 1 or field >= 4:
                    print("Номер столбца должен быть в интервале от 1 до 4")
                else:
                    reversed_or_not = input("Введите 1 если сортировка по возрастанию или 0, если по убыванию: ")
                    match reversed_or_not: 
                        case "1":
                            sort_one_field(path_to_file, field, is_reversed=False)
                        case "0":
                            sort_one_field(path_to_file, field, is_reversed=True)
                        case _:
                            print("Вы ввели неверную команду")
            case "8":
                field_1 = check_pos_int(input("Введите номер первого столбца таблицы, по которому будет сортировка: "))
                field_2 = check_pos_int(input("Введите номер второго столбца таблицы, по которому будет сортировка: "))

                if field_1 is None or field_2 is None :
                    print("Вы ввели некоректный номер столбца таблицы")
                elif (field_1 < 1 or field_1 >= 4) or (field_2 < 1 or field_2 >= 4):
                    print("Номер столбца должен быть в интервале от 1 до 4")
                else:
                    reversed_or_not = input("Введите 1 если сортировка по возрастанию или 0, если по убыванию: ")
                    match reversed_or_not: 
                        case "1":
                            sort_two_fields(path_to_file, field_1, field_2, is_reversed=False)
                        case "0":
                            sort_two_fields(path_to_file, field_1, field_2, is_reversed=True)
                        case _:
                            print("Вы ввели неверную команду")
            case "0":
                print("\nПрограмма завершена")
                break
            
            case _:
                print("Ошибка: некорректная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()




"""    [
        ["3","1",15],
        ["1","2",10]
    ]"""