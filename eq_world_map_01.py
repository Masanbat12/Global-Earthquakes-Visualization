import json
from plotly.graph_objs import Scattergeo, layout, Layout
import plotly.graph_objs as go
from plotly import offline
from eq_explore_data import mags, lons, lats

# Exploring the structure of the data.
filename = 'data/eq_data_2024.json'
with open(filename, 'r', encoding='utf-8') as f:
    all_eq_data = json.load(f)

readable_file = 'data/eq_data_2024.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

# Mapping the earthquakes.
# data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5 * mag for mag in mags],
        'color': mags,  # Using earthquake magnitudes for color
        'colorscale': 'Viridis',
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = go.Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

