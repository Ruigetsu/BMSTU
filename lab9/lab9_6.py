from lab9_func import matrix_str_input

matrix = matrix_str_input()
sogl = "qwrtpsdfghjklzxcvbnm"
glas = "EYUIOA"

for row_indx in range(len(matrix)):
    for indx_in_row in range(len(matrix[0])):
        char = matrix[row_indx][indx_in_row]
        if char in sogl:
            matrix[row_indx][indx_in_row] = chr(ord(char)-32)
        elif char in glas:
            matrix[row_indx][indx_in_row] = chr(ord(char)+32)
        else:
            continue

print("\nИзмененная матрица:")
for row_indx in range(len(matrix)):
    row_to_print = " "

    for indx_in_row in range(len(matrix[0])):
        char = matrix[row_indx][indx_in_row]
        row_to_print += f"{char:^10}|"
        
    if row_indx < len(matrix) - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)