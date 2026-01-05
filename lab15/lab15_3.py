import struct, os
from lab15_functions import write_numbers, print_numbers

def lab15_3():
    while True: 
        answ = write_numbers()
        if answ == True:
            break
        else:
            print("Вы ввели некоректные числа")

    size = struct.calcsize("i")

    def read_element(file, index):
        file.seek(index * size)
        return struct.unpack("i", file.read(size))[0]

    def write_element(file, index, value):
        file.seek(index * size)
        file.write(struct.pack("i", value))

    def shell_sort():
        total_nums = os.path.getsize("lab15/numbers.bin") // size
        
        if total_nums <= 1:
            return
        
        gap = 1
        while gap < total_nums // 3: 
            gap = gap*3 + 1
        
        with open("lab15/numbers.bin", "r+b") as file:
            while gap > 0: 
                for i in range(gap, total_nums):
                    temp = read_element(file, i)
                    j = i
                    while j >= gap: 
                        num1 = read_element(file, j - gap)
                        if num1 > temp:
                            write_element(file, j, num1)
                            j -= gap
                        else: 
                            break
                    write_element(file, j, temp)
                gap //= 3

    shell_sort()

    print_numbers()    
