import pandas as pd
import matplotlib.pyplot as plt

products = ['Laptop', 'Mobile', 'Tablet', 'Headphones']
revenue = [50000, 80000, 30000, 20000]

df = pd.DataFrame({
    'Product': products,
    'Revenue': revenue
})

# Bar Graph
plt.figure()
plt.bar(df['Product'], df['Revenue'])
plt.title("Bar Graph - Product vs Revenue")
plt.xlabel("Products")
plt.ylabel("Revenue")
plt.show()

# Pie Chart
plt.figure()
plt.pie(df['Revenue'], labels=df['Product'], autopct='%1.1f%%')
plt.title("Revenue Distribution")
plt.show()
