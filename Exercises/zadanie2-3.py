n = int(input("Введите число n: "))
i = 1
factorial = 1
s = 0
while i <= n: 
    factorial *= i
    s += factorial
    i += 1
print(s)
    
print("".join(["1"]*5))