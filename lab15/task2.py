import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

fixed_df = pd.read_csv('comptagevelo2011.csv', sep=',', encoding='latin1')

fixed_df = fixed_df.loc[:, ~fixed_df.columns.str.contains('^Unnamed')]

print(fixed_df.columns)

fixed_df['Date'] = pd.to_datetime(fixed_df['Date'], dayfirst=True, errors='coerce')
fixed_df.set_index('Date', inplace=True)

pd.set_option('display.max_columns', None)  # Виводити всі стовпці

print(fixed_df.head(3))

fixed_df.plot(title="Використання велодоріжок у 2011 році")
plt.xlabel("Дата")
plt.ylabel("Кількість відвідувань")
plt.show()
