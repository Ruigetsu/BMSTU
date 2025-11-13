import random
def check(string):
    symb = "0123456879"
    is_exp = False
    num = ""
    num_after_exp = ""
    for i in range(len(string)):
        if is_exp:
            """if string[i] == "-" and string[i-1] == "e":
                num_after_exp += string[i]"""
            if string[i] in symb:
                num_after_exp += string[i]
            else:
                return False
        elif string[i] == "e":
            if len(num) == 0:
                return False
            is_exp = True
        elif string[i] == "-":
            if i == 0:
                num += string[i]
            else:
                return False
        elif string[i] in symb:
            num += string[i]
        else:
            return False
    if is_exp:
        if len(num_after_exp) > 0:
            if check(num_after_exp):
                    return int(num)*10**check(num_after_exp)
            else:
                return False
        else:
            return False

    return int(num)

def input_list(invite):
    arr = list(map(str,input(invite).split()))
    if len(arr) == 0:
        return False, f"Вы ввели пустой массив"
    new_arr = []
    for i in arr: 
        if check(i) is False: 
            return False, f"{i} не целого типа, введите массив заного"
        else:
            new_arr.append(check(i))
    return True, new_arr


def generate_test_data(sizes):
    data = [[],[],[]]
    for size in sizes:
        data[0].append(list(range(1, size + 1)))
        data[1].append([random.randint(1, 100000) for _ in range(size)])
        data[2].append(list(range(size, 0, -1)))
    return data

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