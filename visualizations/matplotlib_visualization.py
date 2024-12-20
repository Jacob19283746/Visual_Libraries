import matplotlib.pyplot as plt

"""Функция построения графика"""
def plot_graph_matplotlib(data):
    plt.close()
    plt.figure(figsize=(10, 5))

    """Линии для цен открытия и закрытия"""
    plt.plot(data['Open time'], data['Open'], label='Цена открытия', color='blue')
    plt.plot(data['Open time'], data['Close'], label='Цена закрытия', color='orange')

    """Добавление скользящего среднего для цен закрытия
       20-периодное скользящее среднее"""
    data['Close_MA'] = data['Close'].rolling(window=20).mean()  
    plt.plot(data['Open time'], data['Close_MA'], label='Скользящее среднее (20)', color='green')

    """Настройки графика"""
    plt.title('Matplotlib | Цена открытия и закрытия криптовалюты с трендом')
    plt.xlabel('Время')
    plt.ylabel('Цена')
    plt.legend()

    """Вывод в окно рисунка"""
    plt.show()
