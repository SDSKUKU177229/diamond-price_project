import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def remove_duplicates(df):
    print("Duplicate rows:", df.duplicated().sum())
    return df.drop_duplicates()

def handle_null_values(df):
    print("Null values:\n", df.isnull().sum())
    df.fillna(0, inplace=True)
    return df

def remove_unwanted_columns(df):
    df.drop(columns=['Unnamed: 0'], errors='ignore', inplace=True)
    return df

def save_cleaned_data(df, path):
    df.to_csv(path, index=False)
    print("Cleaned data saved successfully")