import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR/"data"/"raw_sales.csv"
CLEANED_DATA_PATH = BASE_DIR/"data"/"cleaned_sales.csv"

def load_data():
    df = pd.read_csv(RAW_DATA_PATH)

    print("data loaded successfully")

    return df

def inspect_data(df):
    print("\n========= DATASET OVERVIEW==========")
    print(df.shape)
    print(df.head())
    print(df.info())
    print(df.isnull().sum())
    print(df.describe())

def anyalyze_missing_values(df):
    missing_values = df.isnull().sum()
    missing_percentage = (missing_values/len(df)) * 100


    missing_report = pd.DataFrame({
        "Missing_count" : missing_values,
        "Missing_percentage" : missing_percentage
    })

    missing_report = missing_report[
        missing_report["Missing_count"]>0
    ]
    print(missing_report)
    return missing_report

def handle_missing_values(df):
    print("\n===========handle missing values============")
    categorical_columns = [
        col for col in df.select_dtypes(include=["object","string"]).columns
        if not any(key in col.lower() for key in ["id","date"])
    ]

    for col in categorical_columns:
        missing_count = df[col].isnull().sum()
        if missing_count > 0:
            df[col].fillna("Unknown")
            print(f"{col}:Replaced {missing_count} missing values with unknown")

    print("\n remaining missing values: ")
    print(df.isnull().sum())

    return df