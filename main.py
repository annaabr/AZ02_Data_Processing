import pandas as pd
import numpy as np
import random

# 1. Создаем DataFrame с данными
subjects = ['Математика', 'Физика', 'Химия', 'История', 'Литература']
num_students = 10
data = {subject: [random.randint(2, 5) for _ in range(num_students)] for subject in subjects}

df = pd.DataFrame(data)

# 2. Выводим первые несколько строк DataFrame
print("Первые несколько строк DataFrame:")
print(df.head())

# 3. Вычисляем среднюю оценку по каждому предмету
mean_scores = df.mean()
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

# 4. Вычисляем медианную оценку по каждому предмету
median_scores = df.median()
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# 5. Вычисляем Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print("\nQ1 для математики:", Q1_math)
print("Q3 для математики:", Q3_math)
print("IQR для математики:", IQR_math)

# 6. Вычисляем стандартное отклонение
std_dev = df.std()
print("\nСтандартное отклонение по каждому предмету:")
print(std_dev)