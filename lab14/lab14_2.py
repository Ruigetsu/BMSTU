import struct

def create_or_rewrite_file(file_path, data, format): 
    with open(file_path, "wb") as file:
        formats = f"{format}\n"
        file.write(formats.encode("utf-8"))
        header_line = "Имя|Возраст|Рост|Город\n"
        file.write(header_line.encode('utf-8'))
        
        for row in data:
            encoded_row = []
            for val in row:
                if isinstance(val, str):
                    encoded_row.append(val.encode('utf-8'))
                else:
                    encoded_row.append(val)
            
            row_to_write = struct.pack(format, *encoded_row)
            file.write(row_to_write)
    
    print(f"Файл успешно создан: {file_path}")
    print(f"Записей: {len(data)}")
    return True

