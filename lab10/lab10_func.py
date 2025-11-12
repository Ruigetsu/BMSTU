import random
def check(string):
    symb = "0123456879"
    is_exp = False
    num = ""
    num_after_exp = ""
    for i in range(len(string)):
        if is_exp:
            """if string[i] == "-" and string[i-1] == "e":
                num_after_exp += string[i]"""
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
            if check(num_after_exp):
                    return int(num)*10**check(num_after_exp)
            else:
                return False
        else:
            return False

    return int(num)

def input_list(invite):
    arr = list(map(str,input(invite).split()))
    if len(arr) == 0:
        return False, f"Вы ввели пустой массив"
    new_arr = []
    for i in arr: 
        if check(i) is False: 
            return False, f"{i} не целого типа, введите массив заного"
        else:
            new_arr.append(check(i))
    return True, new_arr


def generate_test_data(sizes):
    data = [[],[],[]]
    for size in sizes:
        data[0].append(list(range(1, size + 1)))
        data[1].append([random.randint(1, 100000) for _ in range(size)])
        data[2].append(list(range(size, 0, -1)))
    return data
