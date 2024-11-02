"""import plotly.graph_objects as go
from plotly.offline import plot
# Пример простого графика
df = px.data.gapminder().query("continent == 'Oceania'")
fig = px.line(df, x='year', y='gdpPercap', color='country')
plot(fig)"""

import plotly.graph_objects as go
# from plotly.offline import plot


"""Функция построения графика"""
def plot_graph_plotly(data):
    fig = go.Figure()

    """Линии для цен открытия и закрытия"""
    fig.add_trace(
        go.Scatter(
            x=data['Open time'], y=data['Open'], mode='lines', name='Цена открытия', line=dict(color='blue')))
    fig.add_trace(
        go.Scatter(
            x=data['Open time'], y=data['Close'], mode='lines', name='Цена закрытия', line=dict(color='orange')))

    """Добавление скользящего среднего для цены закрытия"""
    data['Close_MA'] = data['Close'].rolling(window=20).mean()  # 20-периодное скользящее среднее
    fig.add_trace(
        go.Scatter(
            x=data['Open time'], y=data['Close_MA'], mode='lines', name='Скользящее среднее (20)',
            line=dict(color='green')))

    """Настройки графика"""
    fig.update_layout(title='Plotly | Цены откытия и закрытия криптовалюты с трендом', xaxis_title='Время', yaxis_title='Цена')

    """Вывод графика в браузер"""
    fig.show()
