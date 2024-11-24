import random  # библиотека random

matrix_size = random.randint(4, 8)  # случайное число от 4 до 8, определяющее размер матрицы
print(f"Размер матрицы: {matrix_size}")  # выводим размер матрицы

matrix_elements = [-3, -5, -2, -12, 0, 15, 4, 7, 2]  # список возможных элементов для матрицы
matrix = []  # список для самой матрицы

for _ in range(matrix_size):  # цикл для каждой строки матрицы ( _ это переменная, которая не будет использоваться в цикле)
    row = [random.choice(matrix_elements) for _ in range(matrix_size)]  # строка случайных элементов
    matrix.append(row)  # добавляем сгенерированную строку в матрицу

print("Матрица:")  # выводим
for row in matrix:  # перебираем каждую строку в матрице
    for element in row:  # перебираем каждый элемент в текущей строке
        print(f"{element}", end="\t")  # выводим текущий элемент в форматированном виде
    print()  # переход на новую строку после завершения одной строки

even_sum = 0  # переменная для суммы
for row in matrix:  # перебираем каждую строку в матрице
    for element in row:  # перебираем каждый элемент в текущей строке
        if element % 2 == 0:  # проверка на четность элемента
            even_sum += element  # если элемент четный, добавляем его к сумме

print(f"Сумма всех четных элементов: {even_sum}")  # выводим сумму четных элементов
