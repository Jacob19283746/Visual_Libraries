import pandas as pd
from visualizations import matplotlib_visualization, seaborn_visualization, plotly_visualization
from custom_statistics import calculate_statistics, print_statistics

# Загрузка данных из CSV Файла
data = pd.read_csv('data/BTCUSD_1m_KuCoin.csv', nrows=1000)

# Преобразование времени в формат datatime
data['Open time'] = pd.to_datetime(data['Open time'])

# Рассчитываем статистику
stats = calculate_statistics(data)

# Выводим статистику
print_statistics(stats)

# Вывод первых строк из файла
# print(data.head())



# Визуализация с помощью Matplotlib
# matplotlib_visualization.plot_graph(data)

# Визуализация с помощью Seaborn
# seaborn_visualization.plot_graph(data)

# Визуализация с помощью Plotly
plotly_visualization.plot_graph(data)
