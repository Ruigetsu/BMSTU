import os, struct

def load_format(file_path):
    with open(file_path, "rb") as file:
        format_line = file.readline().decode('utf-8').strip()
        line_size = struct.calcsize(format_line)
        return line_size

def get_total_records(file_path, line_size, file_size):
    with open(file_path, "rb") as file:
        format_size = len(file.readline())
        header_size = len(file.readline())
    
    data_size = file_size - header_size - format_size
    total_records = data_size // line_size
    return total_records

def delete_line(file_path, position):
    file_size = os.path.getsize(file_path)
    line_size = load_format(file_path)
    total_records = get_total_records(file_path, line_size, file_size)
    if position < 0 or position > total_records:
        print(f"Ошибка: позиция должна быть от 1 до {total_records + 1}")
        return False
    if position == total_records:
        with open(file_path, "r+b") as file:
            file.truncate(file_size - line_size)
        return True
    
    with open(file_path, "r+b") as file:
        format_size = len(file.readline())
        header_size = len(file.readline())
        offset = format_size + header_size

        for i in range(position, total_records):
            read_offset = offset + i * line_size
            file.seek(read_offset)
            record_data = file.read(line_size)            

            write_offset = offset + (i-1) * line_size
            file.seek(write_offset)
            file.write(record_data)

        file.truncate(file_size - line_size)
    return True

