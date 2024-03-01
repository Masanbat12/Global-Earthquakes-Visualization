import json

# Exploring the structure of the data.
filename = 'data/eq_data_2024.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/eq_data_2024.json'
with open(readable_file, 'w') as f:
    """ pull each value from eq_dict and
        append it to the appropriate list in one line. 
        Doing so should shorten the body
        of this loop to just four lines."""
    json.dump(all_eq_data, f, indent=4)
    all_eq_dicts = [
        {'properties': {'mag': 5.2, 'title': 'M 5.2 - Near the coast of Yemen'},
         'geometry': {'coordinates': [45.753, 13.931, 10.0]}},
        {'properties': {'mag': 4.8, 'title': 'M 4.8 - Offshore El Salvador'},
         'geometry': {'coordinates': [-88.542, 13.385, 70.0]}},
    ]

# Refactored code
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

mags, lons, lats, hover_texts

print(mags[:10])
print(lons[:5])
print(lats[:5])
