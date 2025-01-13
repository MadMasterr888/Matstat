import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Установка генератора случайных чисел для воспроизводимости
np.random.seed(42)

# Генерация 100 случайных вещественных значений в интервале [-9, 10]
data = np.random.uniform(-9, 10, 100)

# Создание DataFrame для удобства работы с данными
df = pd.DataFrame(data, columns=['Values'])

# Вычисление описательной статистики
mean_value = df['Values'].mean()
median_value = df['Values'].median()
mode_value = df['Values'].mode()[0]  # Берем первый элемент, так как мода может быть несколько

# Вывод результатов
print(f"Среднее: {mean_value:.2f}")
print(f"Медиана: {median_value:.2f}")
print(f"Мода: {mode_value:.2f}")

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(df['Values'], bins=20, color='skyblue', edgecolor='black')
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=1, label=f'Среднее: {mean_value:.2f}')
plt.axvline(median_value, color='green', linestyle='dashed', linewidth=1, label=f'Медиана: {median_value:.2f}')
plt.axvline(mode_value, color='orange', linestyle='dashed', linewidth=1, label=f'Мода: {mode_value:.2f}')
plt.title('Гистограмма случайных значений')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.legend()
plt.grid()
plt.show()
