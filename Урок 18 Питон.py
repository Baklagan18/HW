print("Задание 1, связанное с идеальным кубом")
print("Вариант 1")
V = int(input("Объем куба: "))
i = round(V ** (1./3.))
if V == i ** 3:
    print("Идеальный")
else:
    print("Не идеальный")

print("Вариант 2")
V = int(input("Объем куба: "))
import math
i = round(math.pow(V, 1/3))
if V == i ** 3:
    print("Идеальный")
else:
    print("Не идеальный")

print("Задание 2, связанное с суммой чисел")
print("Вариаент 1")     
x = 0
N = int(input("Количество сложений: "))
for i in range(N):
    i = input("Число для сложения: ")
    if i == "stop":
        break
    x += int(i)
print("Сумма: ", x)

print("Вариант 2")
x = 0
while True:
    b = input("Введите число: ")
    if b == "stop":
        break
    x += int(b)
print("Сумма: ", x)
