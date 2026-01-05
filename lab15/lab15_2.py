import struct, os
from lab15_functions import write_numbers, print_numbers

def lab15_2():
    while True: 
        answ = write_numbers()
        if answ == True:
            break
        else:
            print("Вы ввели некоректные числа")

    size = struct.calcsize("i")
    with open("lab15/numbers.bin", "rb") as file:
        odd_count = 0
        while True:
            raw_num = file.read(size)
            if not raw_num:
                break
            number = struct.unpack("i", raw_num)[0]
            if number % 2 != 0:
                odd_count += 1

    original_size = os.path.getsize("lab15/numbers.bin")
    new_size = original_size + odd_count * size

    with open("lab15/numbers.bin", "r+b") as file:
        read_pos = original_size - size  
        write_pos = new_size - size

        while read_pos >= 0:
            file.seek(read_pos)
            number = struct.unpack("i", file.read(size))[0]

            if number % 2 != 0:
                file.seek(write_pos)
                file.write(struct.pack("i", number * 2))
                write_pos -= size
            
            file.seek(write_pos)
            file.write(struct.pack("i", number))
            write_pos -= size
            read_pos -= size
            
    print_numbers()    