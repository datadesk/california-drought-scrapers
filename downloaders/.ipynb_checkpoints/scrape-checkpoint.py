"""
Download the California State Water Resources Control Board's monthly reports of water production and conservation by the larger urban water suppliers in California.
Source: https://data.ca.gov/dataset/drinking-water-public-water-system-operations-monthly-water-production-and-conservation-information
"""
import pathlib
import pandas as pd

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"


def main():
    """
    Download as a CSV.
    """
    # Download the data
    url = "https://data.ca.gov/dataset/e4b31aa4-0a61-4e03-84bd-2ae46183db59/resource/0c231d4c-1ea7-43c5-a041-a3a6b02bac5e/download/uw_supplier_data051022.csv"
    df = pd.read_csv(url)
    # Save it to the data folder
    df.to_csv(DATA_DIR / "raw/water-use-by-district-timeseries.csv", index=False)


if __name__ == '__main__':
    main()