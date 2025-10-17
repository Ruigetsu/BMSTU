
list_of_str = []
while True:
    string = input("Введите строку: ")
    if string == "":
        break
    else:
        list_of_str.append(string)

indx_to_change = int(input("Введите индекс элемента, который надо поменять: "))

if indx_to_change > len(list_of_str) or indx_to_change < -len(list_of_str) - 1:
    print("Вы ввели неверный индекс")
else:
    string_to_change = list_of_str[indx_to_change]
    new_string = "" 
    for char in string_to_change:
        if "A" <= char <= "Z":
            new_string += char.lower()
        else:
            new_string += char
    list_of_str[indx_to_change] = new_string
    print(f"Измененный список: {list_of_str}")

