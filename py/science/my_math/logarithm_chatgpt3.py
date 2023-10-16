import math
from decimal import Decimal as Dec


def my_log(x, num_terms=10**3):
    """chat
    Обчислює натуральний логарифм числа x за допомогою ряду Тейлора.

    Параметри:
    x (float): Число, для якого потрібно обчислити натуральний логарифм.
    num_terms (int): Кількість термінів ряду Тейлора для використання.
    Чим більше, тим точніше результат, але потребує більше обчислень.

    Повертає:
    float: Натуральний логарифм числа x.
    """
    if x <= 0:
        raise ValueError("Аргумент x повинен бути більше 0")

    ln_x = [] #change1
    for n in range(1, num_terms + 1): 
        ln_x.append(Dec(((-1) ** (n - 1)) * ((x - 1) ** n) / n))

    return ln_x

# Приклад використання функції:
for i in range(1,16):
    try:
        val = 2**i
        r = my_log(val)
        #r = math.log(val,2)
        print(r)
    except Exception as e:
        print(e)
