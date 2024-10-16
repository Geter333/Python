import numpy as np
import matplotlib.pyplot as plt

# Визначаємо функцію Y(x)
def Y(x):
    return -x ** np.cos(5 * x)

# Створюємо масив значень x у діапазоні [0, 10]
x = np.linspace(0, 10, 1000)

# Обчислюємо значення y для кожного значення x
y = Y(x)

# Створюємо графік
plt.plot(x, y, color='blue', linewidth=2, linestyle='-', label=r'$Y(x) = -x^{\cos(5x)}$')

# Додаємо назву графіка
plt.title("Графік функції Y(x) = -x^cos(5x)")

# Позначаємо осі
plt.xlabel("x")
plt.ylabel("Y(x)")

# Додаємо легенду
plt.legend()

# Виводимо графік на екран
plt.grid(True)  # Додаємо сітку
plt.show()
