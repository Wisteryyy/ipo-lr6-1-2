import random #библиотека random

chislo = random.randint(4, 8) # случайное число от 4 до 8
print(f"Размер матрицы: {chislo}") # это число будет размерностью матрицы

chisla_matrici = [-3, -5, -2, -12, 0, 15, 4, 7, 2] #список элементов матрицы
matrica = [] # сам список для матрицы

for _ in range(chislo): # цикл, который будет длиться s раз ( _ это переменная, которая не будет использоваться в цикле)
    stroka_matrici = [random.choice(chisla_matrici) for _ in range(chislo)] # список st состоящий из s случайных значений l
    matrica.append(stroka_matrici) # каждая строка st добавляется в матрицу m

print("Матрица:") #выводим матрицу
for stroka_matrici in matrica: # перебераем строку в матрице
    for element in stroka_matrici: # перебераем элемент в матрице
        print(f"{element}", end="\t") # выводит текущее значение ch в таблице, используя форматирование
    print() # перехлдит на новую строку после завершения первой

sumCH = 0 # инициализируем
for stroka_matrici in matrica: # перебераем строку в матрице
    for element in stroka_matrici: # перебераем элемент в матрице
        if element % 2 == 0: # ставим условие четности
            sumCH += element # считаем сумму

print(f"Сумма всех четных элементов: {sumCH}") # выводим сумму
