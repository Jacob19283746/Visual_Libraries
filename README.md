# Сравнение библиотек визуализации данных: Matplotlib, Seaborn и Plotly.

## Обзор

Данный проект демонстрирует сравнение трех популярных библиотек визуализации данных на Python: Matplotlib, Seaborn и Plotly. В проекте используются исторические данные о криптовалютной паре BTC-USD. Сравнение включает удобство использования, возможности визуализации и производительность.

## Основные возможности

- Matplotlib: Статичные графики с высокой степенью кастомизации.
- Seaborn: Упрощенное создание статистических визуализаций.
- Plotly: Интерактивные графики с поддержкой 3D и карт.

## Установка

1. Создайте виртуальное окружение (рекомендуется).
2. Установите зависимости из файла requirements.txt:

  
    pip install -r requirements.txt
   
## Запуск

1. Скачать и распаковать файл-zip с данными в папку /data.
2. Запустите основной файл main.py для выполнения программы.
3. Скрипты визуализации находятся в папке visualizations/, запускаются для генерации графиков.

## Скриншоты

### Пример графика Matplotlib:
![img.png](scrin_result/img.png)

### Пример графика Seaborn:
![img_1.png](scrin_result/img_1.png)

### Пример графика Plotly:
![img_2.png](scrin_result/img_2.png)

### Пример вывода статистики:
![img_3.png](scrin_result/img_3.png)


## Результаты сравнения:

| Критерий                         | **Matplotlib**                                 | **Seaborn**                                      | **Plotly**                                            |
|----------------------------------|------------------------------------------------|--------------------------------------------------|-------------------------------------------------------|
| **Качество графиков**            | Высокая детализация и настройка                | Простота и автоматическое управление стилями     | Интерактивные графики с масштабированием и настройкой |
| **Интерактивность**              | Только статические графики                     | Только статические графики                       | Полностью интерактивные графики                       |
| **Удобство восприятия**          | Высокий уровень детализации, может перегружать | Аккуратные, легко читаемые                       | Интуитивная интерактивность, удобство анализа         |
| **Поддержка 3D графиков**        | Ограниченная поддержка                         | Отсутствует                                      | Полная поддержка                                      |
| **Производительность**           | Хорошая для небольших данных                   | Умеренная, зависит от объема данных              | Мощная, но требует ресурсов при больших объемах       |
| **Удобство настройки**           | Высокая кастомизация, сложнее в настройке      | Легко настраивается, но с ограниченной гибкостью | Легко настраивается, меньше гибкости                  |
| **Интеграция с Pandas**          | Поддержка, но требует дополнительной настройки | Полная поддержка DataFrame                       | Полная поддержка DataFrame                            |
| **Простота использования**       | Требует больше кода для сложных графиков       | Простота создания сложных графиков               | Простая работа с интерактивными графиками             |
| **Поддержка различных форматов** | PNG, PDF, SVG, и другие                        | PNG, PDF, SVG                                    | HTML, PNG, JPEG, и другие для интерактивных графиков  |
| Поддержка цветовых палитр        | Требует настройки                              | Автоматическая и стильная                        | Поддержка, но требует настройки                       |


## Структура проекта

    ├── data/
    ├── scrin_result/
    ├── visualizations/
    ├── custom_statistics.ipynb
    ├── main.ipynb
    ├── README.md
    ├── requirements.txt
    └── temp-plot.html
