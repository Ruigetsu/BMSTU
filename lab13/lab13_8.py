import os
from lab13_functions import safe_join 

def sort_two_fields(file_path, field1, field2, is_reversed=False): 
    types = [str, int, int, str]

    with open(file_path, 'r', encoding="utf-8-sig") as file1: 
        header = file1.readline()
        file_name = os.path.basename(file_path)
        dir_name = os.path.dirname(file_path)
        
        list_of_values = []
        for line in file1:
            if not line.strip():
                continue
            parts = line.split(";")
            value1 = types[field1-1](parts[field1-1].strip())
            value2 = types[field2-1](parts[field2-1].strip())
            list_of_values.append([value1, value2, line])

    list_of_values.sort(reverse=is_reversed, key=lambda x: (x[0], x[1]))
    
    file2_path = safe_join(dir_name, f"__{file_name}")
    
    with open(file2_path, 'w', encoding="utf-8-sig") as file2:
        file2.write(header)
        for _, _, row in list_of_values:
            file2.write(row)

    os.remove(file_path)
    os.rename(file2_path, file_path)