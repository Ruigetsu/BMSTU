from lab9_func import matrix_input

print("Введите матрицу А")
A = matrix_input()

print("Введите матрицу B")
B = matrix_input()
if len(A[0]) != len(B):
    print("Матрицы должны быть размеров l*m и m*n соотвветсвенно")
    exit()
C = [[] for i in range(len(A))]

for row_indx in range(len(A)):
    for indx_colomn_B in range(len(B[0])):
        num = 0
        for indx_in_row in range(len(A[0])):
            num += A[row_indx][indx_in_row] * B[indx_in_row][indx_colomn_B]
        C[row_indx].append(num)

print("\nМатрица C:")
for row_indx in range(len(C)):
    row_to_print = " "

    for indx_in_row in range(len(C[0])):
        num = C[row_indx][indx_in_row]
        if indx_in_row < len(C) - 1:
            row_to_print += f"{num:^10g}|"
        else: 
            row_to_print += f"{num:^10g}"
        
    if row_indx < len(C) - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)

