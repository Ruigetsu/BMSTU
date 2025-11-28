def print_array(array): 
    str_to_print = ""
    for i in array: 
        str_to_print += f"{i}\n"
    print(str_to_print)

def input_with_check(text_for_import): 
    while True: 
        str = input(text_for_import)
        if not str or not str.strip():
            print("Ввод не может быть пустым или состоять только из пробелов\n")
        else: 
            return str
        
def check_int(string):
    symb = "0123456879"
    is_exp = False
    num = ""
    num_after_exp = ""
    if len(string) == 0:
        return False 
    for i in range(len(string)):
        if is_exp:
            if string[i] in symb:
                num_after_exp += string[i]
            else:
                return False
        elif string[i] == "e":
            if len(num) == 0:
                return False
            is_exp = True
        elif string[i] == "-":
            if i == 0:
                num += string[i]
            else:
                return False
        elif string[i] in symb:
            num += string[i]
        else:
            return False
    if is_exp:
        if len(num_after_exp) > 0:
            if check_int(num_after_exp):
                    return int(num)*10**check_int(num_after_exp)
            else:
                return False
        else:
            return False

    return int(num)