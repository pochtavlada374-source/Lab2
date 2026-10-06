n = int(input("Введите количество измерений: "))
summa = 0.0
for i in range(n):
    count = float(input(f"Введите значение измерения {i + 1}: "))
    summa = summa + count
if n > 0:
    sr = summa / n
else:
    sr = 0.0
print("Сумма всех значений:", summa)
print("Среднее арифметическое:", sr)