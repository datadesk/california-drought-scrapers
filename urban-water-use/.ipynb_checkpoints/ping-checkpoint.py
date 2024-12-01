"""
Ping the State Water Resources Control Board data portal to check for updates

Source: https://data.ca.gov/dataset/urws-conservation-supply-demand
"""

import json
import pathlib
import requests as re
from bs4 import BeautifulSoup

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"


def main():
    # Get HTML
    url = 'https://data.ca.gov/dataset/urws-conservation-supply-demand'
    r = re.get(url)
    soup = BeautifulSoup(r.content)

    # Parse table to find "Last Updated" row
    table = soup.find(
        'table',
        attrs={'summary':'metadata about the dataset'}
    )
    
    last_updated = table.find('th', string='Last Updated')\
        .find_next_sibling('td')\
        .find(
            'span',
            attrs={'data-datetime': True}
        )['data-datetime']
    
    # Write date to JSON file
    
    json_object = json.dumps({'last_updated': last_updated}, indent=4)
    
    with open(DATA_DIR / "ping.json", "w") as outfile:
        outfile.write(json_object)


if __name__ == '__main__':
    main()
