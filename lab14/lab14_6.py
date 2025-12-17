import struct

def find_one_field(path,field,value):
    with open(path, 'rb') as file:
        format = file.readline().decode("utf-8").strip()
        print(format)
        line_size = struct.calcsize(format)
        header = file.readline().decode("utf-8").strip().split("|")
        print(f"{header[0]:^12}|{header[1]:^7}|{header[2]:^4}|{header[3]:<15}")
        print("="*35)
        count = 0
        while True:
            line = file.read(line_size)

            if len(line) < line_size:
                break
            
            unpacked_line = struct.unpack(format, line)
            if field == 1 or field == 4: 
                unpacked_value = unpacked_line[field-1].rstrip(b"\x00").decode("utf-8")
            else: 
                unpacked_value = unpacked_line[field-1]
            if value == unpacked_value:  
                count += 1
                print(f"{count:>2}) {unpacked_line[0].rstrip(b"\x00").decode("utf-8"):<8}|{unpacked_line[1]:^7}\
|{unpacked_line[2]:^4}|{unpacked_line[3].rstrip(b"\x00").decode("utf-8"):<15}")
        if count == 0: 
            print("Подходящих строк не найдено")