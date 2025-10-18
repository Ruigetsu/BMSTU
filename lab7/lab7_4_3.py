
list_of_str = []
while True:
    string = input("Введите строку: ")
    if string == "":
        break
    else:
        list_of_str.append(string)


for string_indx in range(len(list_of_str)): 
    new_string = "" 
    for char in list_of_str[string_indx]:
        if "A" <= char <= "Z":
            new_string += char.lower()
        else:
            new_string += char
    list_of_str[string_indx] = new_string
print(f"Измененный список: {list_of_str}")

