import seaborn as sns
import matplotlib.pyplot as plt

"""Функция построения графика"""
def plot_graph_seaborn(data):
    plt.close()
    """Установка стилей"""
    sns.set_style('darkgrid')

    plt.figure(figsize=(10, 5))

    """Линии для цен открытия и закрытия"""
    sns.lineplot(data=data, x='Open time', y='Open', label='Цена открытия', color='blue')
    sns.lineplot(data=data, x='Open time', y='Close', label='Цена закрытия', color='orange')

    """Добавление скользящего среднего для цены закрытия"""
    data['Close_MA'] = data['Close'].rolling(window=20).mean() # 20-периодное скользящее среднее
    sns.lineplot(data=data, x='Open time', y='Close_MA', label='Скользящее среднее (20)', color='green')

    """Настройки графика"""
    plt.title('Seaborn | Цена открытия закрытия криптовалюты с трендом')
    plt.xlabel('Время')
    plt.ylabel('Цена')
    plt.legend()

    """Вывод в окно рисунка"""
    plt.show()
