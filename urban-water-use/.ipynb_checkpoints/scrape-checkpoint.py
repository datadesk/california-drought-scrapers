"""
Download the State Water Resources Control Board's water use data for urban water suppliers

Source: https://data.ca.gov/dataset/urws-conservation-supply-demand
"""
import pathlib
import pandas as pd
import requests as re

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"


def main():
    """
    Download the Tableau export as a CSV.
    """
    # Download the data
    url = "https://data.ca.gov/datastore/dump/f4d50112-5fb5-4066-b45c-44696b10a49e?format=json"
    headers={'User-Agent': 'Mozilla/5.0'}
    response = re.get(url, headers=headers)
    data = response.json()
    
    # Make dataframe
    cols = [item['id'] for item in data['fields']]
    df = pd.DataFrame(data['records'], columns = cols)
    
    # Save it to the data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)

if __name__ == '__main__':
    main()
