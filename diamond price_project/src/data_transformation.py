from sklearn.preprocessing import LabelEncoder

def encode_categorical(df):

    le = LabelEncoder()

    for col in ['cut', 'color', 'clarity']:
        df[col] = le.fit_transform(df[col])

    return df