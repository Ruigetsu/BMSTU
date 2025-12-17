import struct

def find_two_fields(path,field1,field2,value1,value2):
    with open(path, 'rb') as file:
        format = file.readline().decode("utf-8").strip()
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
            if field1 in [1,4]: 
                unpacked_value1 = unpacked_line[field1-1].rstrip(b"\x00").decode("utf-8")
            else:
                unpacked_value1 = unpacked_line[field1-1]
            if field2 in [1,4]: 
                unpacked_value2 = unpacked_line[field2-1].rstrip(b"\x00").decode("utf-8")
            else:
                unpacked_value2 = unpacked_line[field2-1] 
            if value1 == unpacked_value1 and value2 == unpacked_value2:  
                count += 1
                print(f"{count:>2}) {unpacked_line[0].rstrip(b"\x00").decode("utf-8"):<8}|{unpacked_line[1]:^7}\
|{unpacked_line[2]:^4}|{unpacked_line[3].rstrip(b"\x00").decode("utf-8"):<15}")
        
        if count == 0: 
            print("Подходящих строк не найдено")