from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.
results = []
times = 5000000
for roll_num in range(times):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analize the results.
frequencies = []
max_result = die_1.num_sides +die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick':1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Result of rolling two D8 {times} times',
                   xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')


