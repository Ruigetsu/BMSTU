import os
from lab13_functions import safe_join 

def sort_one_field(file_path, field, is_reversed = False): 
    types = [str, int, int, str]

    with open(file_path, 'r', encoding="utf-8-sig") as file1: 
        header = file1.readline()
        file_name = os.path.basename(file_path)
        dir_name = os.path.dirname(file_path)
        
        list_of_values = []
        while True:
            position = file1.tell()
            line = file1.readline()
            if not line:
                break
            if not line.strip():
                continue
            value = types[field-1](line.split(";")[field-1].strip())
            list_of_values.append([value, position]) 
        
        list_of_values.sort(reverse=is_reversed, key=lambda x: x[0])
        file2_path = safe_join(dir_name, f"__{file_name}")
        with open(file2_path, 'w', encoding="utf-8-sig") as file2:
            file2.write(header)
            for _, pos in list_of_values: 
                file1.seek(pos)
                row = file1.readline()
                file2.write(row)

    os.remove(file_path)
    os.rename(file2_path, file_path)