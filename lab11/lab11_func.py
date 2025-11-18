def check_int(string):
    symb = "0123456879"
    num = ""
    if len(string) == 0:
        return False
    
    for i in range(len(string)):
        if string[i] == "-":
            if i == 0:
                num += string[i]
            else:
                return False
        elif string[i] in symb:
            num += string[i]
        else:
            return False
        
    return int(num)

def check_num(string):
    symb = "0123456879"
    is_exp = False
    is_float = False
    num = ""
    num_after_exp = ""
    if len(string) == 0:
        return False
    for i in range(len(string)):
        if is_exp:
            if string[i] == "-" and string[i-1] == "e":
                num_after_exp += string[i]
            elif string[i] in symb:
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
        elif string[i] == ".":
            if i != 0: 
                num += string[i]
                is_float = True
            else: 
                return False
        elif string[i] in symb:
            num += string[i]
        else:
            return False
        
    if is_exp:
        if check_int(num_after_exp) is not False:
            if is_float == True: 
                return float(num)*10**check_int(num_after_exp)
            else:
                return int(num)*10**check_int(num_after_exp)
        else:
            return False
    else:
        if is_float: 
            return float(num)
        else:
            return int(num)

def input_num_func(string):
    while True: 
        var = input(string)
        checked = check_num(var)
        if checked is False:
            print(f"Некоректное значение '{var}'") 
        else:
            return checked
        
def input_int_func(string):
    while True: 
        var = input(string)
        checked = check_int(var)
        if checked is False or checked <= 0:
            print(f"Некоректное значение '{var}'") 
        else:
            return checked
"""
def f(x): 
    return x**0.5

x = float(input("Введите X: "))
var = True
try:
    f(x)
except ArithmeticError: 
    var = False 
    
if var == True and type(f(x)) != complex: 
    print(var,f(x))
else: 
    print("Error")"""

