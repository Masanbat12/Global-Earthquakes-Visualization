import json
from plotly.graph_objs import Layout
from plotly import offline

""" The code will automatically use the title from the dataset's
    metadata as the title of your map, 
    ensuring that the visualization remains up-to-date
    with the dataset without manual adjustments to the title."""

# Load the earthquake data
filename = 'data/eq_data_1_hour_2024.json'
with open(filename, 'r', encoding='utf-8') as f:
    all_eq_data = json.load(f)

# Extract the title from the dataset metadata
dataset_title = all_eq_data['metadata']['title']

# Extract earthquake data for plotting
all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Define the data for the map
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'colorbar': {'title': 'Magnitude'},
    },
}]

# Use the extracted title for the map's layout
my_layout = Layout(title=dataset_title)

# Generate the map
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes_1_hour_2024.html')
