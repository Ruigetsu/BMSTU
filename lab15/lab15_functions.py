import struct, os

def input_num(): 
    while True:
        try: 
            numbers = list(map(int,input("Введите целые числа через пробел: ").split()))
            break
        except ValueError: 
            print("Введены неверные значения")
    return numbers

def write_numbers(): 
    data = input_num()
    with open("lab15/numbers.bin", "wb") as file_w: 
        for raw_num in data:
            try: 
                num = struct.pack("i", raw_num)
                file_w.write(num)
            except struct.error: 
                return False
    return True

def print_numbers(): 
    with open("lab15/numbers.bin", "rb") as file_r: 
        size = struct.calcsize("i")
        total_nums = os.path.getsize("lab15/numbers.bin") // size
        numbers = []
        for i in range(total_nums): 
            file_r.seek(i*size)
            raw_num = file_r.read(size)
            num = struct.unpack("i", raw_num)[0]
            numbers.append(num)
        print(numbers)
