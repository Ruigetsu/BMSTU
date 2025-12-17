def append_data(path, data):     
    if path is None:
        print("Файл не выбран! Сначала выберите файл (пункт 1)")
        return False
    try:
        with open(path, 'a', encoding="utf-8-sig") as file: 
            for row in data: 
                file.write(";".join(row) + "\n")
    except Exception as e:
        print(f"Ошибка при добавлении данных: {e}")
        return False