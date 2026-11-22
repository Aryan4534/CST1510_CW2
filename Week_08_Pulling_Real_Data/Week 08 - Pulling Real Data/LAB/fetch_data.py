"""
Week 8 Lab solution: fetch COVID-19 country data and save DATA/raw.csv.

Copy this file into the root of your CST1510_CW2 project folder.
Run from that folder with: python fetch_data.py
Install dependencies first: python -m pip install requests pandas
"""

from pathlib import Path

import pandas as pd
import requests

URL = "https://disease.sh/v3/covid-19/countries"
PARAMS = {}
RECORDS_KEY = None

RENAME = {}
KEEP = [
    "country",
    "continent",
    "cases",
    "deaths",
    "recovered",
    "tests",
    "population",
    "active",
]
MUST_HAVE = ["cases", "continent"]

RAW_FILE = Path(__file__).parent / "DATA" / "raw.csv"


def get_data(url, params):
    """Fetch JSON data. Return None and explain the error if the request fails."""
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        print("Could not get the data:", error)
        return None


def make_table(data, records_key):
    """Convert a list of JSON records (or a keyed list) into a DataFrame."""
    records = data[records_key] if records_key else data
    return pd.json_normalize(records, sep="_")


def tidy_data(df):
    """Keep useful columns and remove rows missing required values."""
    df = df.rename(columns=RENAME)
    missing = [column for column in KEEP if column not in df.columns]
    if missing:
        raise KeyError(f"These KEEP columns were not returned by the API: {missing}")
    df = df[KEEP]
    return df.dropna(subset=MUST_HAVE)


def save_data(df, path):
    """Create DATA if needed and save a clean CSV without the index."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Saved {len(df)} rows to {path}")


def main():
    data = get_data(URL, PARAMS)
    if data is None:
        return

    table = make_table(data, RECORDS_KEY)
    tidy = tidy_data(table)
    print(tidy.head())
    print("Shape:", tidy.shape)
    save_data(tidy, RAW_FILE)


if __name__ == "__main__":
    main()
