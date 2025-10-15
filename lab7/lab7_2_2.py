list_of_num = list(map(int,input("Введите числа через пробел:").split()))
flag_to_move_right = 0
is_prev_even = False
temporary = 0
for i in range(len(list_of_num)):
    if list_of_num[i] % 2 == 0: 
        list_of_num.append(None)
        flag_to_move_right += 1
        temporary = list_of_num[i] * 2
        is_prev_even = True
    elif is_prev_even: 
        list_of_num[i], list_of_num[i+1], temporary = temporary, list_of_num[i], list_of_num[i+1]
        is_prev_even = False
    else: 
        list_of_num[i], list_of_num[i+flag_to_move_right], temporary = temporary, list_of_num[i], list_of_num[i+flag_to_move_right]

print(list_of_num)
