import os

def append_data(path, data): 
    """Добавляет записи в конец файла БД"""
    if path is None:
        print("❌ Файл не выбран! Сначала выберите файл (пункт 1)")
        return False
    
    if not os.path.exists(path):
        print(f"❌ Файл не существует: {path}")
        return False
    
    try:
        with open(path, 'a', encoding="utf-8-sig", newline='') as file: 
            for row in data: 
                file.write(";".join(row) + "\n")
        
        print(f"✅ Добавлено записей: {len(data)}")
        return True
        
    except PermissionError:
        print(f"❌ Нет прав на запись в файл: {path}")
        return False
    except Exception as e:
        print(f"❌ Ошибка при добавлении данных: {e}")
        return False