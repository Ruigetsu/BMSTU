import time, random
from lab10_func import input_list,generate_test_data, insertion_sort_with_sentinel
    
while True: 
    arr = input_list("Введите элементы массива через пробел: ")
    if arr[0] == True:
        print(f"Отсортированный массив: {insertion_sort_with_sentinel(arr[1])[0]}")
        break
    else: 
        print(arr[1])

while True:
    sizes = input_list("Введите размерности через пробел: ")
    print("\n")
    if sizes[0] == True: 
        first_row = " "*32 + "|"
        second_row = " "*28 + "|"
        for i in sizes[1]:
            colomn = f"Размерность = {i}"
            first_row += f"{colomn:^30} |"
            second_row += f"{"Время":^15}" + f"{"Перестановки":^15} |"
        print(f"{first_row}\n\
    {"-"*len(first_row)}\n\
    {second_row}\n\
    {"-"*len(first_row)}")
        data = generate_test_data(sizes[1])
        for arr_type in range(len(data)):
            if arr_type == 0:
                str_to_print = f"{"Упорядоченный список":^32}|"
            elif arr_type == 1:
                str_to_print = f"{"Случайный список":^32}|"
            else: 
                str_to_print = "Упорядоченный в обратном порядке|"
            for arr in data[arr_type]:
                start = time.time()
                swaps = insertion_sort_with_sentinel(arr)[2]
                end = time.time()
                str_to_print += f"{end-start:^15g} {swaps:^15}|"
            print(f"{str_to_print}\n\
    {"-"*len(str_to_print)}")
        break
    else: 
        print(sizes[1])
 
#делать рандомную дату, сортировать а потом его reverse()


while True:
    sizes = input_list("Введите размерности через пробел: ")
    print("\n")
    list_of_sizes = sizes[1]
    if sizes[0] == True: 
        first_row = " "*32 + "|"
        second_row = " "*28 + "|"
        for i in list_of_sizes:
            colomn = f"Размерность = {i}"
            first_row += f"{colomn:^30} |"
            second_row += f"{"Время":^15}" + f"{"Перестановки":^15} |"
        print(f"{first_row}\n\
    {"-"*len(first_row)}\n\
    {second_row}\n\
    {"-"*len(first_row)}")
        for arr_type in range(3):
            if arr_type == 0:
                str_to_print = f"{"Упорядоченный список":^32}|"
            elif arr_type == 1:
                str_to_print = f"{"Случайный список":^32}|"
            else: 
                str_to_print = "Упорядоченный в обратном порядке|"
            for size in range(len(list_of_sizes)):
                arr = [random.randint(1, 100000) for _ in range(size)]
                if arr_type == 0:
                    arr = insertion_sort_with_sentinel(arr)[0]
                    start = time.time()
                    swaps = insertion_sort_with_sentinel(arr)[2]
                    end = time.time()      
                    str_to_print += f"{end-start:^15g} {swaps:^15}|"
                elif arr_type == 1:
                    start = time.time()
                    swaps = insertion_sort_with_sentinel(arr)[2]
                    end = time.time()      
                    str_to_print += f"{end-start:^15g} {swaps:^15}|"
                else:
                    arr = reversed(insertion_sort_with_sentinel(arr)[0])
                    start = time.time()
                    swaps = insertion_sort_with_sentinel(arr)[2]
                    end = time.time()      
                    str_to_print += f"{end-start:^15g} {swaps:^15}|"
            print(f"{str_to_print}\n\
    {"-"*len(str_to_print)}")
        break
    else: 
        print(sizes[1])