import struct

def print_db(path):
    with open(path,"rb") as file:
        format = file.readline().decode("utf-8").strip()
        line_size = struct.calcsize(format)
        header = file.readline().decode("utf-8").strip().split("|")
        print(f"{header[0]:^12}|{header[1]:^7}|{header[2]:^4}|{header[3]:<15}")
        print("="*35)
        count = 1
        while True: 
            line = file.read(line_size)
            if len(line) < line_size:
                break

            unpacked_line = struct.unpack(format, line)
            name = unpacked_line[0].rstrip(b"\x00").decode("utf-8")
            city = unpacked_line[-1].rstrip(b"\x00").decode("utf-8")
            print(f"{count:>2}) {name:<8}|{unpacked_line[1]:^7}|{unpacked_line[2]:^4}|{city:<15}")
            count += 1
