import random

def arrays(n):
    S = []
    items = list(range(100))
    random.shuffle(items)
    for i in range(0,n):
        new_arr = []
        for j in range(0,items[i]):
            x = random.randint(0,1000)
            new_arr.append(x)
        if i % 2 == 1:
            new_arr = sorted(new_arr)
        else:
            new_arr = sorted(new_arr)
            new_arr = new_arr[::-1]
        S.append(new_arr)
    return S

n = int(input("Введите натуральное число n:"))
if n >= 1:
    print(arrays(n))
else:
    print("Введенное число не является натуральным")
            
