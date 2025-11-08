
#1
list_1 = list(map(int,input("Введите числа массива 1: ").split()))
list_2 = list(map(int,input("Введите числа массива 2: ").split()))
list_3 = []
i,j = 0,0
while i < len(list_1) and j < len(list_2):
    if list_1[i] <= list_2[j]:
        list_3.append(list_1[i])
        i += 1
    else:
        list_3.append(list_2[j])
        j += 1
if i < len(list_1):
    list_3 += list_1[i:]
else:
    list_3 += list_2[j:]
print(list_3)
"""#1
list_of_nums = list(map(int,input("Введите числа массива: ").split()))

for i in range(len(list_of_nums)):
    offset = 0
    for j in range(i+1,len(list_of_nums)):
        if list_of_nums[i] == list_of_nums[j]:
            list_of_nums[j] = None
            offset += 1
        else:
            list_of_nums[j-offset] = list_of_nums[j]
for i in range(len(list_of_nums)):
    if list_of_nums[i] == None:
        list_of_nums = list_of_nums[:i]
        break
print(list_of_nums)"""
"""#2
N,M = map(int,input("Введите размеры матриц: ").split())

matrix_A = []
for n in range(N):
    list_of_nums = list(map(int,input(f"Введите числа {n+1}-ой строчки матрицы А: ").split()))
    if len(list_of_nums) == M:
        matrix_A.append(list_of_nums)

matrix_B = []
for m in range(M):
    list_of_nums = list(map(int,input(f"Введите числа {m+1}-ой строчки матрицы B: ").split()))
    if len(list_of_nums) == M:
        matrix_B.append(list_of_nums)

for row in range(M-1):
    for indx_in_row in range(M - row - 1):
        matrix_B[row][indx_in_row], matrix_B[M-indx_in_row-1][M-row-1] = matrix_B[M-indx_in_row-1][M-row-1], matrix_B[row][indx_in_row]
        #print(matrix_B[row][indx_in_row],matrix_B[M-row-1][M-indx_in_row-1])
matrix_A += matrix_B
for row_indx in range(len(matrix_A)):
    row_to_print = " "

    for indx_in_row in range(M):
        char = matrix_A[row_indx][indx_in_row]
        row_to_print += f"{char:^10}|"
        
    print(row_to_print)
    print("-"*(len(row_to_print)))"""
"""
# -------------------------------------------
# Задача №2
# -------------------------------------------
matrix = []

order = int(input("Введите порядок матрицы: "))
print()
for i in range(order):
    row = list(map(int, input(f"Введите {i + 1}-ю строку матрицы, разделяя элементы через пробел: ").split()))
    matrix.append(row)

# <Блок 2 - Поворот нечётных луковых колец>
for i in range(0,len(matrix)//2,2): #1
    for j in range(i, len(matrix) - 1 - i): #2
        temp = matrix[i][j]
        matrix[i][j] = matrix[len(matrix) - 1 - j][i]
        matrix[len(matrix) - 1 - j][i] = matrix[len(matrix) - 1 - i][len(matrix) - 1 - j]
        matrix[len(matrix) - 1 - i][len(matrix) - 1 - j] = matrix[j][len(matrix) - 1 - i]
        matrix[j][len(matrix) - 1 - i] = temp
print("Матрица после преобразования:\n")

for row_indx in range(len(matrix)):
    row_to_print = " "

    for indx_in_row in range(len(matrix[0])):
        char = matrix[row_indx][indx_in_row]
        row_to_print += f"{char:^10}|"
        
    print(row_to_print)
    print("-"*(len(row_to_print)))"""