from lab8_func import sqr_matrix_input
matrix = sqr_matrix_input()
if matrix == False: 
    print("Вы ничего не ввели")
    exit()


print("\nИзначальная матрица:")
for row_indx in range(len(matrix)):
    count_negative = 0
    row_to_print = " " 
    indx_first_diag = row_indx #Индекс элемента на главной диагонали
    indx_second_diag = -row_indx #Индекс элемента на побочной диагонали
    for indx_in_row in range(len(matrix)):
        num = matrix[row_indx][indx_in_row]
        if indx_in_row < len(matrix) - 1:
            row_to_print += f"{num:^10g}|"
        else: 
            row_to_print += f"{num:^10g}"

        if num < 0: 
            count_negative += 1

    if count_negative > max_count:
        max_count = count_negative
        indx_count_max_negative = row_indx
    elif count_negative < min_count:
        min_count = count_negative
        indx_count_min_negative = row_indx

    if row_indx < len(matrix) - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)