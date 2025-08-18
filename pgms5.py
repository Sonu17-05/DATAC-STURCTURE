import matplotlib.pyplot as plt

# Define data directly in the script
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Figs', 'Grapes']
sales = [120, 95, 75, 60, 30, 45, 110]

# Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(fruits, sales, color='skyblue')
plt.title('Fruit Sales (Bar Chart)')
plt.xlabel('Fruits')
plt.ylabel('Sales (in kg)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Scatter Plot
#plt.figure(figsize=(10, 5))
#plt.scatter(fruits, sales, color='green', s=100)
#plt.title('Fruit Sales (Scatter Plot)')
#plt.xlabel('Fruits')
#plt.ylabel('Sales (in kg)')
#plt.grid(True)
#plt.tight_layout()
#plt.show()
