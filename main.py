import random
s = random.randint(4, 8)
print("Размер матрицы:", s)
v = [-3, -5, -2, -12, 0, 15, 4, 7, 2]
m = []
for i in range(s):
    row = []
    for j in range(s):
        value = random.choice(v)
        row.append(value)
    m.append(row)
print("Сгенерированная матрица:")
for row in m:
    for elem in row:
        print(f"{elem:>3}", end=" ")
    print()
sum = 0
for row in m:
    for elem in row:
        if elem % 2 == 0:
            sum += elem
print("Сумма четных элементов:", sum)