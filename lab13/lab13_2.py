import os 
from lab13_functions import check_pos_int, check_word

def create_or_rewrite_file(data, file_path): 
    """Создаёт или перезаписывает файл БД"""
    try:
        with open(file_path, "w", encoding="utf-8-sig", newline='') as file:
            file.write(";".join(["Имя", "Возраст", "Рост", "Город_проживания"]) + "\n")
            
            for row in data:
                file.write(";".join(row) + "\n")
        
        print(f"Файл успешно создан: {file_path}")
        print(f"Записей: {len(data)}")
        return True
        
    except PermissionError:
        print(f"Ошибка: нет прав на запись в файл: {file_path}")
        return False
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")
        return False

def input_data(number_of_rows): 
    """Ввод данных для таблицы"""
    print("\n" + "="*50)
    print("Введите данные для таблицы:")
    print("Формат: Имя Возраст Рост Город")
    print("Пример: Иван 25 180 Москва")
    print("(пустая строка для завершения ввода)")
    print("="*50)
    
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
        print(f"Запись {count_file_rows} добавлена")
