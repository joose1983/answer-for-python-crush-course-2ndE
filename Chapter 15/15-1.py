import matplotlib.pyplot as plt

#input_values = [1, 2, 3, 4, 5]
#cube = [1, 8, 27, 64, 125]
input_values = range(1, 5001)
cube = [x**3 for x in input_values]

plt.style.use('classic')
fig, ax = plt.subplots()

# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of Value", fontsize = 14)

ax.tick_params(axis='both', labelsize =14)

ax.plot(input_values, cube, linewidth=3)

plt.show()