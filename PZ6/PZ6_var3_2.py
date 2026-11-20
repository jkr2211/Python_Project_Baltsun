import random
#2. Дан список размера N. Найти номер его первого локального минимума (локальный
#минимум — это элемент, который меньше любого из своих соседей).
N = input("Введите размер списка: ")
while type(N) != int : #обработка исключений
    try:
        N = int(N)
    except ValueError:
        print("Ошибка, попробуйте снова")
        N = input("Введите размер списка: ")
spisok = []
for i in range(N):
    spisok.append(random.randint(1, 100))
print("Сгенерированный список:" , spisok)
for i in range(len(spisok)):
    if i == 0 and len(spisok) > 1:
        if spisok[i] < spisok[i+1]:
            print("Номер первого локального минимума:", i)
            break
    elif i == len(spisok)-1 and len(spisok) > 1:
        if spisok[i] < spisok[i-1]:
            print("Номер первого локального минимума:", i)
            break
    elif 0 < i < len(spisok)-1:
        if spisok[i] < spisok[i-1] and spisok[i] < spisok[i+1]:
            print("Номер первого локального минимума:", i)
            break
else:
    print("Локальный минимум не найден")