import matplotlib.pyplot as plt

from die import Die

# Create two D6 and a D6.

die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analize the results.
frequencies = []
max_result = die_1.num_sides +die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
plt.style.use('seaborn')
x_values = list(range(2, max_result+1))

plt.bar(x_values, frequencies, label='roll times')
plt.legend()
plt.xlabel('Result')
plt.ylabel('Frequency of Result')

plt.title('Frequency of Result')
plt.show()

