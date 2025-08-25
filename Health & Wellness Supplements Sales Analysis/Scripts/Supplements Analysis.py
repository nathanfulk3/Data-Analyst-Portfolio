import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('N:/Supplement_Sales_Weekly_Expanded.csv', parse_dates=['Date'])

df['Net_Units_Sold'] = df['Units Sold'] - df['Units Returned']
df['Net_Revenue'] = df['Net_Units_Sold'] * df['Price']
df['Return_Rate'] = df['Units Returned'] / df['Units Sold'] * 100


category_revenue = df.groupby('Category')['Net_Revenue'].sum().reset_index()
sns.barplot(data=category_revenue, x='Net_Revenue', y='Category', palette='viridis')
plt.title('Total Revenue by Supplement Category')
plt.show()

sns.scatterplot(data=df, x='Discount', y='Net_Units_Sold', hue='Category')
plt.title('Discount vs Units Sold')
plt.show()

df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Net_Revenue'].sum().reset_index()
monthly_sales['Month'] = monthly_sales['Month'].dt.to_timestamp()

plt.figure(figsize=(12,5))
sns.lineplot(data=monthly_sales, x='Month', y='Net_Revenue')
plt.title('Monthly Net Revenue Trend')
plt.show()


returns_summary = df.groupby('Category')['Return_Rate'].mean().sort_values()
sns.barplot(x=returns_summary.values, y=returns_summary.index, palette='magma')
plt.title('Average Return Rate by Category')
plt.show()
