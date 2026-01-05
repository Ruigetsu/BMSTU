import struct, os
from lab15_functions import write_numbers, print_numbers

def lab15_1():
    while True: 
        answ = write_numbers()
        if answ == True:
            break
        else:
            print("Вы ввели некоректные числа")

    with open("lab15/numbers.bin", "r+b") as file: 
        size = struct.calcsize("i")
        total_nums = os.path.getsize("lab15/numbers.bin") // size
        offset = 0
        for i in range(total_nums): 
            file.seek(i*size)
            raw_num = file.read(size)
            num = struct.unpack("i", raw_num)[0]
            if num < 0: 
                offset += 1
            else: 
                file.seek((i-offset)*size)
                file.write(raw_num)
        file.truncate(os.path.getsize("lab15/numbers.bin") - size*offset)

    print_numbers()    