""" 
Read the file active_volcanos.csv and filter the entries by country (e.g. Italy).
The filtered entries go into a corresponding
json file (e.g. data/volcanos_italy.json).
Only volcanoes are to be considered, for which applies:
risk != NULL

The json entries should contain:
Name of the volcano
Risk
Latitude
Longitude
Country
Region

the json keys should have the following names:
name, risk, lat, long, country, region

e.g. as an array of objects

[
    {
        "name": "Farallon de Pajaros",
        "latitude": "20.538000000000000",
        "longitude": "144.895999999999000",
        "risk": "1",
        "country": "United States",
        "region": "Japan, Taiwan, Marianas"
    },
    {..},


]
"""

import csv
from pathlib import Path
import json
from pathlib import Path

def read_file(filename, country):
    filtered = []
    with open(Path(__file__).parent / filename) as f:
        reader = csv.reader(f, delimiter=",")
        header = next(reader)
        for row in reader:
            if row[2].lower() == country.lower() and row[-1] != 'NULL':
                filtered.append(row)
                

    return header, filtered


T = read_file('active_volcanos.csv', country = 'Italy')

final_dic = []

for volcano in T[1]:
    dic = {k: v for k, v in zip([ T[0][i] for i in [1,2,3,5,6,12] ], [ volcano[i] for i in [1,2,3,5,6,12] ]) }
    final_dic.append(dic)


with open(Path(__file__).parent / "volcanos_italy.json", mode="w") as f:
    json.dump(final_dic, f)


