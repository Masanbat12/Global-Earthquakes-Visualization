import json
from plotly.graph_objs import Scattergeo, layout, Layout
from plotly import offline
from eq_explore_data import mags, lons, lats

# Exploring the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

# Mapping the earthquakes.
# data = [Scattergeo(lon=lons, lat=lats)]
data = [{'type': 'scattergeo',
       'lon': lons,
       'lat': lats,
       'marker':{
           'size': [5*mag for mag in mags],
       },
}]
my_layout = Layout(title = 'Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

