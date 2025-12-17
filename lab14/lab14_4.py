import os, struct

def load_format(file_path):
    with open(file_path, "rb") as file:
        format_line = file.readline().decode('utf-8').strip()
        line_size = struct.calcsize(format_line)
        return format_line, line_size

def get_total_records(file_path, line_size):
    file_size = os.path.getsize(file_path)
    
    with open(file_path, "rb") as file:
        format_size = len(file.readline())
        header_size = len(file.readline())
    
    data_size = file_size - header_size - format_size
    total_records = data_size // line_size
    return total_records

def insert_line(file_path, position, data):
    name, age, height, city = data[0]
    format_line, line_size = load_format(file_path)
    total_records = get_total_records(file_path, line_size)
    if position < 0 or position > total_records + 1:
        print(f"Ошибка: позиция должна быть от 1 до {total_records + 1}")
        return False
    
    new_line = struct.pack(format_line, name.encode('utf-8'), age, height, city.encode('utf-8'))
    if position == total_records + 1:
        with open(file_path, "ab") as file:
            file.write(new_line)
        return True
    
    with open(file_path, "r+b") as file:
        format_size = len(file.readline())
        header_size = len(file.readline())
        offset = format_size + header_size
        file.seek(0, 2)  # в конец файла
        file.write(b'\x00' * line_size)  
        file.flush()
        for i in range(total_records, position - 1, -1):
            read_offset = offset + (i - 1) * line_size
            file.seek(read_offset)
            record_data = file.read(line_size)
            write_offset = offset + i * line_size

            file.seek(write_offset)
            file.write(record_data)
            file.flush()

        insert_offset = offset + (position - 1) * line_size
        file.seek(insert_offset)
        file.write(new_line)
        file.flush()
    return True