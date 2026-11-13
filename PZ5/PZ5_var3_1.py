#1. Составить функцию, которая выполнит суммирования числового ряда.
def summatotal(start, shag, stop):#Вводим функцию
    summa = 0
    while start < stop:
        summa += start
        start += shag
    summa += stop
    return summa
a = input("Введите начало числового ряда: ")
while type(a) != int : #обработка исключений 1
    try:
        a = int(a)
    except ValueError:
        print("Ошибка, попробуйте снова")
        a = input("Введите начало числового ряда: ")
b = input("Введите шаг числового ряда: ")
while type(b) != int : #обработка исключений 2
    try:
        b = int(b)
    except ValueError:
        print("Ошибка, попробуйте снова")
        b = input("Введите шаг числового ряда: ")
c = input("Введите конец числового ряда: ")
while type(c) != int : #обработка исключений 3
    try:
        c = int(c)
    except ValueError:
        print("Ошибка, попробуйте снова")
        N = input("Введите целое число больше 0: ")
Sum = summatotal(a, b, c)
print("Сумма числового ряда равна" , Sum)
