import matplotlib.pyplot as plt 

x_values = []
y_values = []

for x in range(1, 1001):
    x_values.append(x)
    y_values.append(x**2)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

#Set chart title and lable axes.
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value ", fontsize = 14)

#Set size of tick labels.
ax.tick_params(labelsize = 14)

#Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_00])

plt.show()