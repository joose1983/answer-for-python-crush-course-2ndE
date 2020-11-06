import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get indexes
    LAT_INDEX = header_row.index('latitude')
    LON_INDEX = header_row.index('longitude')
    BRI_INDEX = header_row.index('brightness')

    # Get data from this file.
    latitudes, longitudes, brights = [],[],[]
    for row in reader:
        latitude = row[LAT_INDEX]
        longitude = row[LON_INDEX]
        if (type(row[BRI_INDEX]) is int) or (type(row[BRI_INDEX]) is float):
            bright = row[BRI_INDEX]
        elif type(row[BRI_INDEX]) is str:
            bright = float(row[BRI_INDEX])
        else:
            continue

        latitudes.append(latitude)
        longitudes.append(longitude)
        brights.append(bright)


# Map the world fires.
sizes = []
for bright in brights:
    size = int(bright/50)
    sizes.append(size)

colors = []
for color in brights:
    color = int(bright)
    colors.append(color)
    
data = [{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat':latitudes,
    'marker':{
        'size': sizes,
        'color': colors,
        'colorscale': 'Viridis',
        'reversescale':True,
        'colorbar': {'title': 'Fire brightness'},
        },
    }]
my_layout = Layout(title='Global Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')

