import time
from lab10_func import input_list,generate_test_data

def insertion_sort_with_sentinel(arr):
    n = len(arr)
    
    iterations = 0
    swaps = 0
    
    sentinel = min(arr) - 1  # Барьер, значение гарантированно меньше всех элементов
    arr.insert(0, sentinel)
    
    # Сортируем массив с барьером
    for i in range(2, n + 1):
        iterations += 1
        key = arr[i]
        j = i - 1
        
        while True:
            iterations += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        if j+1 != i: 
            arr[j + 1] = key
            swaps += 1
    arr.pop(0) #Удаляем барьер
    return arr, iterations, swaps
    
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
        data = generate_test_data(sizes[1])
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

        for arr_types in range(len(data)):
            if arr_types == 0:
                str_to_print = f"{"Упорядоченный список":^32}|"
            elif arr_types == 1:
                str_to_print = f"{"Случайный список":^32}|"
            else: 
                str_to_print = "Упорядоченный в обратном порядке|"
            for arr in data[arr_types]:
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