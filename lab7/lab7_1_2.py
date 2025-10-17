list_of_num = list(map(int,input("Введите числа через пробел:").split()))
flag_to_move_left = 0

for i in range(len(list_of_num)):
    if list_of_num[i] % 2 == 0:
        flag_to_move_left += 1
    else: 
        list_of_num[i-flag_to_move_left] = list_of_num[i]
list_of_num = list_of_num[:-flag_to_move_left]
print(f"Новый список: {list_of_num}")