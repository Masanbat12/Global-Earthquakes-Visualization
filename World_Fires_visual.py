import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot

# Load the data from the CSV file
filename = 'data/world_fires_1_day.csv'
fires_data = pd.read_csv(filename)

# Display the first few rows of the dataframe to understand its structure
print(fires_data.head())

# Extract the necessary data
lats = fires_data['latitude'].tolist()
lons = fires_data['longitude'].tolist()
brightness = fires_data['brightness'].tolist()

# Define the data for the map
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': ['Brightness: %s' % b for b in brightness],
    'marker': {
        'size': [b / 50 for b in brightness],  # Example size scaling, adjust as needed
        'color': brightness,
        'colorscale': 'YlOrRd',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]

# Define the layout of the map
layout = go.Layout(
    title='World Fires in the Last Day',
    geo=dict(showland=True, landcolor="rgb(217, 217, 217)")
    )

# Create and display the figure
fig = go.Figure(data=data, layout=layout)
plot(fig, filename='world_fires.html')
