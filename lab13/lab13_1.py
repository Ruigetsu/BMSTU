import os
from lab13_functions import print_lists, normalize_path, safe_join

def choose_file(): 
    """Главная функция выбора файла"""
    while True: 
        print("\n" + "="*50)
        path = input("Введите путь до директории или файла (или enter для выхода): ").strip()
        
        if path.lower() == '':
            return None
            
        path = normalize_path(path)
        result = choose(path)
        
        match result:
            case None:
                print("Ошибка: файл не найден или директория пуста")
            case _:
                print(f"Выбран файл: {result}")
                return result
                    
def choose(path): #навигация по директориям
    if not os.path.exists(path):
        print(f"Ошибка: путь не существует: {path}")
        return None

    if os.path.isfile(path):
        if path.lower().endswith('.csv'):
            return os.path.abspath(path)
        else:
            print("Ошибка: файл должен иметь расширение .csv")
            return None
    
    if os.path.isdir(path):
        items = os.listdir(path)
            
        if len(items) == 0: 
            print("Ошибка: директория пуста")
            return None
            
        files_list = []
        dirs_list = []
        
        for item in items:
            item_path = safe_join(path, item)
            
            if os.path.isfile(item_path) and item.lower().endswith(".csv"):
                files_list.append(item)
            elif os.path.isdir(item_path): 
                dirs_list.append(item)

        if len(files_list) == 0 and len(dirs_list) == 0:
            print("Ошибка: в директории нет .csv файлов и поддиректорий")
            return None

        if len(files_list) > 0:
            print(print_lists(files_list, "\nCSV файлы:\n"))
        if len(dirs_list) > 0:
            print(print_lists(dirs_list, "\nДиректории:\n"))
        
        if len(files_list) > 0 and len(dirs_list) > 0:
            choice = input("\nВведите '1' для выбора файла или '2' для перехода в директорию: ").strip()
            
            match choice:
                case "1":
                    try:
                        file_choice = int(input("Введите номер файла: "))
                        if 1 <= file_choice <= len(files_list): 
                            return os.path.abspath(safe_join(path, files_list[file_choice - 1]))
                        else:
                            print("Ошибка: некорректный номер файла")
                            return None
                    except ValueError:
                        print("Ошибка: введите число")
                        return None
                        
                case "2":
                    try:
                        dir_choice = int(input("Введите номер директории: "))
                        if 1 <= dir_choice <= len(dirs_list):
                            return choose(safe_join(path, dirs_list[dir_choice - 1]))
                        else:
                            print("Ошибка: некорректный номер директории")
                            return None
                    except ValueError:
                        print("Ошибка: введите число")
                        return None
                        
                case _:
                    print("Ошибка: некорректный выбор")
                    return None

        elif len(files_list) > 0: 
            try:
                file_choice = int(input("Введите номер файла: "))
                if 1 <= file_choice <= len(files_list): 
                    return os.path.abspath(safe_join(path, files_list[file_choice - 1]))
                else:
                    print("Ошибка: некорректный номер файла")
                    return None
            except ValueError:
                print("Ошибка: введите число")
                return None
            
        else:
            try:
                dir_choice = int(input("Введите номер директории: "))
                if 1 <= dir_choice <= len(dirs_list):
                    return choose(safe_join(path, dirs_list[dir_choice - 1]))
                else:
                    print("Ошибка: некорректный номер директории")
                    return None
            except ValueError:
                print("Ошибка: введите число")
                return None
    
    return None