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

def analyze_duplicates(df):
    print("==========analyzing duplicates=============")
    duplicate_mask = df.duplicated(keep=False)
    duplicate_count = duplicate_mask.sum()
    print(f"total duplicate records : {duplicate_count}")
    if duplicate_count > 0:
        print("duplicate records:")
        print(df[duplicate_mask])
    else:
        print("no duplicate records")
    return df

def remove_duplicates(df):
     initial_count = len(df)

     df = df.drop_duplicates(keep="first")

     final_count = len(df)

     removed = initial_count - final_count

     print(f"total removed duplicates : {removed}")
     return df


def validate_data(df):
    print("\n ============Validating values===============")

    print("\n selecting numeric column values")
    numeric_columns = df.select_dtypes(include = "number").columns

    for col in numeric_columns:
        negative_count = (df[col]<0).sum()
        if negative_count > 0:
            print(f"{col}: {negative_count} negative values")

    for col in numeric_columns:
        zero_count = (df[col] == 0).sum()
        if zero_count > 0:
            print(f"{col} : {zero_count} zero values")

    for col in df.columns:
        if "discount" in col.lower():
            invalid_count = ((df[col]<0) | (df[col]>100)).sum()
            print(f"{col}: {invalid_count} invalid discount values" ) 

    for col in df.columns:
        if "date" in col.lower():
            converted_dates = pd.to_datetime(df[col],errors = "coerce")
            invalid_dates = converted_dates.isna().sum()
            print(f"{col}: {invalid_dates} invalid date count")

    print("remaining duplicate values :",df.duplicated().sum())
    return df