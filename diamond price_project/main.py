# =========================
# IMPORT MODULES
# =========================
import os
import subprocess
import sys

try:
    import joblib
except ImportError:
    print("joblib not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "joblib"])
    import joblib


print("WORKING DIR:", os.getcwd())

from src.model_deployment import save_model, load_model



from src.data_cleaning import (
    load_data,
    remove_duplicates,
    handle_null_values,
    remove_unwanted_columns,
    save_cleaned_data
)

from src.data_visualization import (
    plot_cut_distribution,
    plot_price_hist,
    plot_scatter,
    plot_heatmap
)

from src.feature_engineering import (
    add_price_per_carat,
    add_carat_category
)

from src.data_transformation import encode_categorical

from src.feature_selection import select_features

from src.data_split import split_data

from src.model_training import (
    train_linear_model,
    train_svr_model
)

from src.model_evaluation import evaluate

from src.model_deployment import save_model


# =========================
# 1. LOAD DATA
# =========================
df = load_data("data/price.csv")
print("Data Loaded Successfully")
print(df.head())



# =========================
# 2. DATA CLEANING
# =========================
df = remove_duplicates(df)
df = handle_null_values(df)
df = remove_unwanted_columns(df)

save_cleaned_data(df, "data/cleaned_price.csv")


# =========================
# 3. DATA VISUALIZATION
# =========================
plot_cut_distribution(df)
plot_price_hist(df)
plot_scatter(df)
plot_heatmap(df)


# =========================
# 4. FEATURE ENGINEERING
# =========================
df = add_price_per_carat(df)
df = add_carat_category(df)


# =========================
# 5. DATA TRANSFORMATION
# =========================
df = encode_categorical(df)


# =========================
# 6. FEATURE SELECTION
# =========================
X, y = select_features(df)


# =========================
# 7. TRAIN-TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = split_data(X, y)


# =========================
# 8. MODEL TRAINING
# =========================
print("\nTraining Linear Regression Model...")
lr_model = train_linear_model(X_train, y_train)

print("\nTraining SVR Model...")
svr_model = train_svr_model(X_train, y_train)


# =========================
# 9. MODEL EVALUATION
# =========================
print("\nEvaluating SVR Model...")
predictions = evaluate(svr_model, X_test, y_test)


# =========================
# 10. MODEL SAVING
# =========================
save_model(lr_model, "linear_model.pkl")
save_model(svr_model, "svr_model.pkl")

print("\nPipeline Completed Successfully 🚀")
