list_of_num = list(map(int,input("Введите элементы списка через пробел: ").split()))
num = int(input("Введите элемент для вставки: "))
indx = int(input("Введите индекс вставки элемента: "))
if indx == -1 or indx == len(list_of_num)-1:
    list_of_num.append("")
    list_of_num[indx] = num
    print(f"Новый список = {list_of_num}")
elif indx > len(list_of_num) or indx < -len(list_of_num) - 1:
    print("Вы ввели неверный индекс")
else:
    for i in range(len(list_of_num)-1,indx-1,-1): 
        list_of_num[i] = list_of_num[i-1]
        if i == indx: 
            list_of_num[i] = num
    print(f"Новый список = {list_of_num}")