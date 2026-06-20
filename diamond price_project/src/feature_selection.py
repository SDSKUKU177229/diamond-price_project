def select_features(df):

    X = df[['carat', 'depth', 'table', 'x', 'y', 'z']]
    y = df['price']

    return X, y