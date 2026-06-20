import joblib
import os

# =========================
# SAVE MODEL
# =========================
def save_model(model, filename):

    model_dir = os.path.join("artifacts", "models")
    os.makedirs(model_dir, exist_ok=True)

    path = os.path.join(model_dir, filename)

    joblib.dump(model, path)

    print("Model saved at:", path)


# =========================
# LOAD MODEL
# =========================
def load_model(filename):

    path = os.path.join("artifacts", "models", filename)

    model = joblib.load(path)

    print("Model loaded from:", path)

    return model