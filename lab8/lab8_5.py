from lab8_func import sqr_matrix_input
matrix = sqr_matrix_input()
if matrix == False: 
    print("Вы ничего не ввели")
    exit()

max_num_over_first = float("-inf") #Максимальное значение над главной диагональю
min_num_under_second = float("inf") #Минимальное значение под побочной диагональю
print("\nИзначальная матрица:")
for row_indx in range(len(matrix)):
    count_negative = 0
    row_to_print = " " 
    indx_first_diag = row_indx #Индекс элемента на главной диагонали
    indx_second_diag = len(matrix) - 1 - row_indx #Индекс элемента на побочной диагонали
    for indx_in_row in range(len(matrix)):
        num = matrix[row_indx][indx_in_row]
        if indx_in_row < len(matrix) - 1:
            row_to_print += f"{num:^10g}|"
        else: 
            row_to_print += f"{num:^10g}"

        if indx_in_row > indx_first_diag:
            max_num_over_first = max(max_num_over_first,num)
        if indx_in_row > indx_second_diag:
            min_num_under_second = min(min_num_under_second,num)

    if row_indx < len(matrix) - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)

print(f"Максимальное значение над главной диагональю: {max_num_over_first}\n\
Минимальное значение под побочной диагональю: {min_num_under_second}")