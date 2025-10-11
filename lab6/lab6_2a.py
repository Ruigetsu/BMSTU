list_of_num = list(map(int,input("Введите элементы списка через пробел: ").split()))
indx = int(input("Введите индекс удаления элемента: "))
if indx > len(list_of_num) or indx < -len(list_of_num) - 1:
    print("Вы ввели неверный индекс")
list_of_num.pop(indx)
print(f"Новый список = {list_of_num}")
