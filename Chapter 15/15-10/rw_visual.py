import plotly
import plotly.offline as py
import plotly.graph_objs as go

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk(50)
rw.fill_walk()

point_numbers = range(rw.num_points)
x_values = rw.x_values
y_values = rw.y_values

trace0 = go.Scatter(x=x_values,y=y_values ,mode = 'markers',name = 'random walk')
fig= go.Figure(trace0)
fig.show()
fig.write_html("rw.html")

