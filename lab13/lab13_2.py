def create_or_rewrite_file(data, file_path): 
    with open(file_path, "w", encoding="utf-8-sig", newline='') as file:
        file.write(";".join(["Имя", "Возраст", "Рост", "Город_проживания"]) + "\n")
        
        for row in data:
            file.write(";".join(row) + "\n")
    
    print(f"Файл успешно создан: {file_path}")
    print(f"Записей: {len(data)}")
    return True

