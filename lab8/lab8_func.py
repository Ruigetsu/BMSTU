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

    row_width = None 
    while True: 
        row = []
        row_input = input(f"Введите числа строки №{row_number} через пробел:").split()
        is_error = False
        
        if len(row_input) == 0:
            break
        
        for string in row_input:
            num = check(string)
            if num is False:
                print(f"Вы допустили ошибку в {string}, последняя строка не будет добавлена")
                is_error = True
            else:
                row.append(num)
        
        if row_width is None and not is_error:
            row_width = len(row)
        else: 
            if len(row) != row_width:
                print("Вы нарушили ширину матрицы, последняя строка не будет добавлена")
                continue
        if not is_error:
            matrix.append(row)
            row_number += 1
    
    return matrix if len(matrix) > 0 else False
