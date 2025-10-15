list_of_num = list(map(int,input("Введите элементы списка через пробел: ").split()))
indx = int(input("Введите индекс удаления элемента: "))

if indx > len(list_of_num) or indx < -len(list_of_num) - 1:
    print("Вы ввели неверный индекс")
else:
    for i in range(indx+1,len(list_of_num)): 
            list_of_num[i - 1] = list_of_num[i]
list_of_num.pop()
print(f"Новый список = {list_of_num}")