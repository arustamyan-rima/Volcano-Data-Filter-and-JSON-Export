# Volcano Data Filter and JSON Export

This project involves reading a CSV file named 'active_volcanos.csv' and filtering the entries based on a specific country (e.g., Italy). The filtered entries are then saved into a corresponding JSON file (e.g., data/volcanos_italy.json). Only volcanoes are considered for which the condition 'risk != NULL' holds.

The JSON entries contain specific attributes, including the Name of the volcano, Risk, Latitude, Longitude, Country, and Region.

The JSON keys have the following names:
- `name`
- `risk`
- `lat`
- `long`
- `country`
- `region`

For example, the JSON entries are represented as an array of objects:

```json
[
    {
        "name": "Farallon de Pajaros",
        "latitude": "20.538000000000000",
        "longitude": "144.895999999999000",
        "risk": "1",
        "country": "United States",
        "region": "Japan, Taiwan, Marianas"
    },
    {...},
]
```

## Project Structure

The main script is named volcanos.py.  
The CSV file to be processed is named active_volcanos.csv.  
The script includes functions for reading the file, filtering the data, and exporting to JSON.  

## Usage

Ensure you have the necessary libraries installed to run the code. You can run the script using Python.  
The filtered and processed data will be saved in a JSON file named 'volcanos_italy.json'.
  
## Functions  
read_file: Reads a CSV file and filters the entries based on a specific country.  
main: Main function that orchestrates the data filtering and JSON export
