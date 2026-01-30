import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:\\Users\\USER\\Downloads\\company_sales_data.csv")
print(df)

df.info()

# Ploting the total profit generated across months
x = df['month_number']
y = df['total_profit']
plt.figure(figsize= (10, 8))
plt.plot(x, y, marker = 'o', c = 'red')
for x, y in zip(x, y):
    plt.text(x, y,y)
plt.xlabel('month_number')
plt.ylabel('total_profit')
plt.title('Total profits generated across months')
plt.show()

# Subplots for Bathing Soap and facewash
a = df['month_number']
b = df['bathingsoap']
c = df['facewash']
print(a)

plt.figure(figsize=(8,6))
plt.subplot(2, 1, 1)
plt.plot(a, b, marker = '*', color = 'green')
plt.title("Bathing Soap Sales")
plt.ylabel("Sales")

plt.subplot(2, 1, 2)
plt.plot(a, c, marker = '*', color = 'orange')
plt.title("Facewash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()