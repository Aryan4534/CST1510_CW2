"""
fetch_data.py - Week 8 starter project.
Fetches public Python organisation repositories and saves a tidy CSV.

Install once:
    python -m pip install requests pandas

Run:
    python fetch_data.py
"""

from pathlib import Path

import pandas as pd
import requests

URL = "https://api.github.com/orgs/python/repos"
PARAMS = {"per_page": 100, "sort": "updated"}
RECORDS_KEY = None

RENAME = {}
KEEP = [
    "name",
    "language",
    "stargazers_count",
    "forks_count",
    "open_issues_count",
    "size",
    "created_at",
]
MUST_HAVE = ["name"]

RAW_FILE = Path(__file__).parent / "DATA" / "raw.csv"


def get_data(url, params):
    """Request JSON data. Return None safely if the request fails."""
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as error:
        print("Could not get the data:", error)
        return None


def make_table(data, records_key=None):
    """Convert a list of JSON records into a pandas DataFrame."""
    records = data[records_key] if records_key else data
    if not isinstance(records, list):
        raise TypeError("The selected API data must be a list of records.")
    return pd.json_normalize(records, sep="_")


def tidy_data(df):
    """Keep useful columns, use simple names and remove incomplete rows."""
    missing = [column for column in KEEP if column not in df.columns]
    if missing:
        raise KeyError(f"These KEEP columns are missing from the API response: {missing}")

    tidy = df.rename(columns=RENAME)[KEEP].copy()
    tidy = tidy.dropna(subset=MUST_HAVE)
    tidy.columns = [
        str(column).strip().lower().replace(" ", "_").replace(".", "_")
        for column in tidy.columns
    ]
    return tidy


def save_data(df, path):
    """Create the DATA folder if needed and save the CSV."""
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
    save_data(tidy, RAW_FILE)


if __name__ == "__main__":
    main()
