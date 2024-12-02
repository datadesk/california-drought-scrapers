"""
Ping the State Water Resources Control Board data portal to check for updates

Source: https://data.ca.gov/dataset/urws-conservation-supply-demand
"""

import json
import pathlib
import requests as re
from bs4 import BeautifulSoup
from zoneinfo import ZoneInfo
from datetime import datetime

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"


def main():
    # Get HTML
    url = 'https://data.ca.gov/dataset/urws-conservation-supply-demand'
    r = re.get(url)
    soup = BeautifulSoup(r.content, features="lxml")

    # Parse table to find "Last Updated" row
    table = soup.find(
        'table',
        attrs={'summary':'metadata about the dataset'}
    )
    
    date_string = table.find('th', string='Last Updated')\
        .find_next_sibling('td')\
        .find(
            'span',
            attrs={'data-datetime': True}
        )['data-datetime']

    # Format date
    utc_datetime = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S%z")
    local_timezone = ZoneInfo("America/Los_Angeles")
    local_datetime = utc_datetime.astimezone(local_timezone)
    formatted_date = local_datetime.strftime("%Y-%m-%d")
    
    # Write date to JSON file
    
    json_object = json.dumps({'last_updated': formatted_date}, indent=None)
    
    with open(DATA_DIR / "ping.json", "w") as outfile:
        outfile.write(json_object)


if __name__ == '__main__':
    main()
