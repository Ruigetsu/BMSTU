def check(string):
    symb = "0123456879-"
    is_float = False
    is_exp = False
    num = ""
    num_after_exp = ""
    for i in string:
        if is_exp:
            num_after_exp += i
        if i == ".":
            is_float = True
            num += i
        elif i == "e":
            is_exp = True
        elif i not in symb:
            return False
        else:
            num += i
    if is_exp:
        if check(num_after_exp):
            if is_exp and is_float:
                return float(num)*10**check(num_after_exp)
            elif is_exp and not is_float:
                return int(num)*10**check(num_after_exp)
        else:
            return False
    if is_float:
        return float(num)
    else:
        return int(num)

def check_int(string):
    symb = "0123456879-"
    is_float = False
    is_exp = False
    num = ""
    num_after_exp = ""
    for i in string:
        if i not in symb:
            return False
        else:
            num += i
    return int(num)

def matrix_input():
    matrix = []
    row_number = 1
    print("Введите строки матрицы, её ширина будет определена по первой введённой строке\n\
Нажмите Enter, чтобы закончить ввод")
    
    matrix_width = None 
    while True: 
        row = []
        row_input = input(f"Введите числа строки №{row_number} через пробел:").split()
        
        if len(row_input) == 0:
            break
        
        for string in row_input:
            num = check(string)
            if num is False:
                print(f"Вы допустили ошибку в {string}, последняя строка не будет добавлена")
                continue
            else:
                row.append(num)
        
        if matrix_width is None:
            matrix_width = len(row)
        else: 
            if len(row) != matrix_width:
                print("Вы нарушили ширину матрицы, последняя строка не будет добавлена")
                continue
        matrix.append(row)
        row_number += 1

    return matrix if len(matrix) > 0 else False

def sqr_matrix_input():
    matrix = []
    row_number = 0
    print("Введите строки квадратной матрицы, её ширина будет определена по первой введённой строке\n\
Нажмите Enter, чтобы закончить ввод")

    matrix_width = None
    while True: 
        row = []
        row_number += 1
        row_input = input(f"Введите числа строки №{row_number} через пробел:").split()
        
        if len(row_input) == 0:
            break
        
        for string in row_input:
            num = check(string)
            if num is False:
                print(f"Вы допустили ошибку в {string}, последняя строка не будет добавлена")
                continue
            else:
                row.append(num)
        
        if matrix_width is None:
            matrix_width = len(row)
        else: 
            if len(row) != matrix_width:
                print("Вы нарушили ширину матрицы, последняя строка не будет добавлена")
                continue
            elif row_number == matrix_width:
                matrix.append(row)
                break
        matrix.append(row)
    
    return matrix if len(matrix) > 0 else False

def sqr_int_matrix_input():
    matrix = []
    row_number = 0
    print("Введите строки квадратной матрицы, её ширина будет определена по первой введённой строке\n\
Нажмите Enter, чтобы закончить ввод")

    matrix_width = None
    while True: 
        row = []
        row_number += 1
        row_input = input(f"Введите числа строки №{row_number} через пробел:").split()
        
        if len(row_input) == 0:
            break
        
        for string in row_input:
            num = check_int(string)
            if num is False:
                print(f"Вы допустили ошибку в {string}, последняя строка не будет добавлена")
                continue
            else:
                row.append(num)
        
        if matrix_width is None:
            matrix_width = len(row)
        else: 
            if len(row) != matrix_width:
                print("Вы нарушили ширину матрицы, последняя строка не будет добавлена")
                continue
            elif row_number == matrix_width:
                matrix.append(row)
                break
        matrix.append(row)
    
    return matrix if len(matrix) > 0 else False