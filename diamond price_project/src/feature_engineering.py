import numpy as np
import pandas as pd

def add_price_per_carat(df):
    df['price_per_carat'] = df['price'] / df['carat']
    return df

def add_carat_category(df):
    df['carat_category'] = pd.cut(
        df['carat'],
        bins=3,
        labels=['small', 'medium', 'large']
    )
    return df