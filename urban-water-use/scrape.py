"""
Download the State Water Resources Control Board's water use data for urban water suppliers

Source: https://data.ca.gov/dataset/urws-conservation-supply-demand
"""
import pathlib
import pandas as pd

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"


def main():
    """
    Download the Tableau export as a CSV.
    """
    # Download the data
    url = "https://data.ca.gov/dataset/c69ac02b-adfb-459a-bc58-bf69a8b572d2/resource/f4d50112-5fb5-4066-b45c-44696b10a49e/download/monthly_combined_dataset.csv"
    df = pd.read_csv(url)
    df.columns = map(str.lower, df.columns)
    # Save it to the data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()