def check(string):
    symb = "0123456879-"
    is_float = False
    for i in string:
        if i == ".":
            is_float = True
        elif i not in symb:
            return False
    if is_float:
        return float(string)
    else:
        return int(string)

def matrix_input():
    matrix = []
    row_number = 1
    print("Введите строки матрицы, её ширина будет определена по первой введённой строке\n\
Нажмите Enter, чтобы закончить")

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
    print("Введите строки матрицы, её ширина будет определена по первой введённой строке\n\
Нажмите Enter, чтобы закончить")

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