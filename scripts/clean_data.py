import pandas as pd

def clean_columns(df):
    # Rename columns for readability
    df = df.rename(columns={
        "datetime": "Datetime",
        "city": "City",
        "state": "State",
        "country": "Country",
        "shape": "Shape",
        "duration (seconds)": "Duration (seconds)",
        "duration (hours/min)": "Duration (hours/min)",
        "comments": "Comments",
        "date posted": "Date_Posted",
        "longitude ": "Longitude",
        "latitude": "Latitude",
    })
    return df


def preprocess_datetime(df):
    # Split datetime into Date and Time, and convert to datetime format
    df["Date"] = df["Datetime"].str.split(" ").str[0]
    df["Time"] = df["Datetime"].str.split(" ").str[1]
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    df["Date_Posted"] = pd.to_datetime(df["Date_Posted"], errors='coerce')
    df.drop(columns=["Datetime"], inplace=True)

    df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
    df["Longitude "] = pd.to_numeric(df["Longitude"], errors="coerce")
    return df

def standardize_values(df):
    # Standardize capitalization and formatting
    df["State"] = df["State"].str.upper()
    df["Country"] = df["Country"].str.upper()
    df["Shape"] = df["Shape"].str.capitalize()
    df["City"] = df["City"].str.capitalize()
    df["City"] = df["City"].str.split("(").str[0]

    # Replace country abbreviations with full names
    df["Country"] = df["Country"].replace({
        "US": "United States",
        "GB": "Great Britain",
        "CA": "Canada",
        "AU": "Australia",
        "DE": "Germany"
    })

    return df
