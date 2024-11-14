import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

fixed_df = pd.read_csv('comptagevelo2011.csv', sep=',', encoding='latin1')
fixed_df = fixed_df.loc[:, ~fixed_df.columns.str.contains('^Unnamed')]

fixed_df['Date'] = pd.to_datetime(fixed_df['Date'], dayfirst=True, errors='coerce')
fixed_df.set_index('Date', inplace=True)

fixed_df['Month'] = fixed_df.index.month

bike_path = 'Berri1'
monthly_counts = fixed_df.groupby('Month')[bike_path].sum()

most_popular_month = monthly_counts.idxmax()
most_popular_month_count = monthly_counts.max()

# Словник для назв місяців
month_names = {
    1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень',
    5: 'Травень', 6: 'Червень', 7: 'Липень', 8: 'Серпень',
    9: 'Вересень', 10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'
}

# Вивести найпопулярніший місяць, його номер, назву та кількість велосипедистів
print(f'Найпопулярніший місяць: {month_names[most_popular_month]} ({most_popular_month}), кількість велосипедистів: {most_popular_month_count}')

plt.figure(figsize=(10, 6))
monthly_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title(f'Щомісячна кількість велосипедистів на велодоріжці {bike_path}')
plt.xlabel('Місяць')
plt.ylabel('Загальна кількість велосипедистів')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Виділити найпопулярніший місяць кольором
plt.bar(most_popular_month - 1, most_popular_month_count, color='orange')

plt.show()
