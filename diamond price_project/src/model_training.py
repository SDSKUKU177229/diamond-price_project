from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR

def train_linear_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def train_svr_model(X_train, y_train):
    model = SVR()
    model.fit(X_train, y_train)
    return model