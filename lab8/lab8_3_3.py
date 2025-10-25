from lab8_func import matrix_input
matrix = matrix_input()
if matrix == False: 
    print("Вы ничего не ввели")
    exit()

indx_of_min_delta = -1
min_delta = float("inf")

matrix_width = len(matrix[0])

print("\nИзначальная матрица:")
for row_indx in range(len(matrix)):
    row_to_print = " " 

    for indx_in_row in range(matrix_width):
        num = matrix[row_indx][indx_in_row]
        if row_indx < matrix_width - 1:
            row_to_print += f"{num:^10g}|"
        else: 
            row_to_print += f"{num:^10g}"
  
    if indx_in_row < len(matrix) - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)

for indx_in_row in range(matrix_width):
    s_pos = 0
    s_abs_neg = 0

    for row_indx in range(len(matrix)):
        num = matrix[row_indx][indx_in_row]

        if num > 0:
            s_pos += num
        else: 
            s_abs_neg += abs(num)

    delta = abs(s_pos - s_abs_neg)
    if delta < min_delta:
        min_delta = delta
        indx_of_min_delta = indx_in_row

print(f"\nМинимальная разница модулей сумм положительных и отрицательных элементов имеет столбец №{indx_of_min_delta+1} = {min_delta}")
for row in range(len(matrix)):
    print(matrix[row][indx_of_min_delta])