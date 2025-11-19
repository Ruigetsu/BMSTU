from lab9_func import matrix_input
A = matrix_input()
B = matrix_input()
width = len(A[0])
for indx_in_row in range(width):
    avg = 0
    s = 0
    for row_indx in range(len(B)):
        s += B[row_indx][indx_in_row]
    avg = s / len(B)

    count = 0
    for row_indx in range(len(A)):
        if A[row_indx][indx_in_row] > avg:
            count += 1
    print(f"\nКоличество чисел для столбца {indx_in_row+1} = {count}")

    for row_indx in range(len(B)):
        if count != 0:
            B[row_indx][indx_in_row] *= count

print("\nИзмененная матрица B:")
for row_indx in range(len(B)):
    row_to_print = " "

    for indx_in_row in range(len(B[0])):
        num = B[row_indx][indx_in_row]
        if indx_in_row < len(B) - 1:
            row_to_print += f"{num:^10g}|"
        else: 
            row_to_print += f"{num:^10g}"
        
    if row_indx < len(B) - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)