from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 and a D10.

die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(5000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analize the results.
multiplies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    multiply = results.count(value)
    multiplies.append(multiply)

# Visualize the results.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=multiplies)]
x_axis_config = {'title': 'Result', 'dtick':1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Result of multiply two D6 sides, rolling 50000 times',
                   xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')


