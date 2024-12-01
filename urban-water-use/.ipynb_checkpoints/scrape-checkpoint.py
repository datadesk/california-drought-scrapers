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
    Download and export as CSV
    """
    
    # Request data from URL
    url = "https://data.chhs.ca.gov/dataset/e283ee5a-cf18-4f20-a92c-ee94a2866ccd/resource/130d7ba2-b6eb-438d-a412-741bde207e1c/download/covid19vaccinesbycounty.csv"
    headers={'User-Agent': 'Mozilla/5.0'}
    response = re.get(url, headers=headers)
    response_str = response.text
    
    # Parse the response string to dataframe
    df = pd.DataFrame([row.split(',') for row in response_str.split('\r\n')])
    # Dataframe will have column names as first row
    # move them to column headers
    df.columns = df.iloc[0]  # Set the first row as column names
    df = df[1:] 
    # lowercase headers
    df.columns = map(str.lower, df.columns)
    
    # Save it to the data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()
