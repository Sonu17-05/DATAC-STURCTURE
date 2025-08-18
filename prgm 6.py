import random
import matplotlib.pyplot as plt

# Step 1: Generate 50 random ages between 10 and 80
ages = [random.randint(10, 80) for _ in range(50)]

# Step 2: Plot the histogram
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=range(10, 85, 5), color='skyblue', edgecolor='black')  # bins of size 5
plt.title('Histogram of Random Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
