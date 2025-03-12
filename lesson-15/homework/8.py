import numpy as np
import matplotlib.pyplot as plt

# data
time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [3, 5, 2, 6]
category_B = [4, 2, 7, 5]
category_C = [2, 6, 4, 3]

x = np.arange(len(time_periods))

# stacked bar chart
plt.figure(figsize=(8, 6))
plt.bar(x, category_A, label='Category A', color='blue')
plt.bar(x, category_B, bottom=category_A, label='Category B', color='green')
plt.bar(x, category_C, bottom=np.array(category_A) + np.array(category_B), label='Category C', color='orange')

# title and labels
plt.xlabel('Time Periods')
plt.ylabel('Values')
plt.title('Stacked Bar Chart of Categories Over Time')
plt.xticks(x, time_periods)
plt.legend()

plt.show()
