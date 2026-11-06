#1. Составить функцию, которая выполнит суммирования числового ряда.
def summatotal(numb): #Вводим функцию
    summa = 0
    index = 0
    while index < len(numb):
        summa += numb[index]
        index += 1
    print(summa)
    return summa
numb = []
print("Вводите числа числового ряда по одному, чтобы закончить введите 0")
number = input()
while type(number) !=int: #обработка исключений
    try:
        number = int(number)
    except ValueError:
        print("Ошибка, попробуйте снова")
        number = input()
while number != 0:
    numb.append(number)
    number = input()
    while type(number) != int:  # обработка исключений
        try:
            number = int(number)
        except ValueError:
            print("Ошибка, попробуйте снова")
            number = input()
print(summatotal(numb))

