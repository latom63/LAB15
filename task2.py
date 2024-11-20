import pandas as pd

# Завантаження даних
file_path = 'comptagevelo2014.csv'  # Задайте ваш шлях до файлу
data = pd.read_csv(file_path, encoding='utf-8')

# Перетворення стовпця "Date" у формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# Додавання стовпця "Month" для визначення місяця
data['Month'] = data['Date'].dt.month

# Обчислення сумарної кількості велосипедистів по місяцях (по всіх доріжках)
monthly_usage = data.iloc[:, 1:-1].groupby(data['Month']).sum().sum(axis=1)

# Визначення місяця з найбільшим використанням
most_popular_month = monthly_usage.idxmax()
most_popular_value = monthly_usage[most_popular_month]

print("Найпопулярніший місяць:", most_popular_month)
print("Кількість велосипедистів у цей місяць:", most_popular_value)
