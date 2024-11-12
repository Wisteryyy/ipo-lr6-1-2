import random
s = random.randint(4, 8)
print("Размер матрицы:", s)
vse = [-3, -5, -2, -12, 0, 15, 4, 7, 2]
m = []
for i in range(s):
    row = []
    for j in range(s):
        v = random.choice(vse)
        row.append(v)
    m.append(row)
print("Сгенерированная матрица:")
for row in m:
    for el in row:
        print(f"{el:>3}", end=" ")
    print()
sum = 0
for row in m:
    for el in row:
        if el % 2 == 0:
            sum += el
print("Сумма четных элементов:", sum)
