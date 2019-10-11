"""
Пара натуральных чисел называется совместимой, если одно из чисел пары равно сумме всех цифр обоих чисел, 
а другое равно произведению всех цифр обоих чисел. 
Найдите все совместимые пары, в которых оба числа не превосходят 100.
"""
for a in range(1,100):
    for b in range(a,100):
        n = str(a) + str(b)
        mult = 1
        summa = 0
        for i in n:
            summa += int(i)
            if int(i) != 0: mult *= int(i)
        if (a==summa) and (b==mult): print (a, b)
        if (b==summa) and (a==mult): print (a, b)
