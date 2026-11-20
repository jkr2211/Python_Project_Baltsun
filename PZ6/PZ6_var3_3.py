import random
#3. Дан список размера N (N — четное число). Поменять местами его первый элемент
#со вторым, третий — с четвертым и т. д.
while True: #обработка исключений
    try:
        N = int(input("Введите размер списка (Должен быть четным): "))
        if N%2==0:
            break
        else:
            print("Ошибка, число должно быть четным")
    except ValueError:
        print("Ошибка, попробуйте снова")
A = []
for i in range(N):
    A.append(random.randint(1, 100))
print("Сгенерированный список: ", A)
for i in range(0, N, 2):
    A[i], A[i+1] = A[i+1], A[i]
print("Поменяный список: ", A)