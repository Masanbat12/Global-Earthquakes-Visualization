import json

# Exploring the structure of the data.
filename = 'data/eq_data_2024.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/eq_data_2024.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

# all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))
# mags = []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     mags.append(mag)
#
# print(mags[:10])
all_eq_dicts = all_eq_data['features']
# magnitudes, longitudes and latitudes
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

print(mags[:10])
print(lons[:5])
print(lats[:5])