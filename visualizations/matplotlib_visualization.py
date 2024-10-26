# import matplotlib.pyplot as plt

# Пример простого графика
#
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]
#
# plt.plot(x, y)
# plt.title('Простой график')
# plt.xlabel('X-оси')
# plt.ylabel('Y-оси')
# plt.show()

import matplotlib.pyplot as plt

# Функция построения графика
def plot_graph(data):
    plt.figure(figsize=(10, 5))

    # Линии для цен открытия и закрытия
    plt.plot(data['Open time'], data['Open'], label='Цена открытия', color='blue')
    plt.plot(data['Open time'], data['Close'], label='Цена закрытия', color='orange')

    # Добавление скользящего среднего для цен закрытия
    data['Close_MA'] = data['Close'].rolling(window=20).mean() # 20-периодное скользящее среднее
    plt.plot(data['Open time'], data['Close_MA'], label='Скользящее среднее (20)', color='green')

    # Настройки графика
    plt.title('Цена открытия и закрытия криптовалюты с трендом')
    plt.xlabel('Время')
    plt.ylabel('Цена')
    plt.legend()

    # Вывод в окно рисунка
    plt.show()
