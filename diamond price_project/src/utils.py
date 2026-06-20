import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PLOT_DIR = os.path.join(BASE_DIR, "artifacts", "plots")
MODEL_DIR = os.path.join(BASE_DIR, "artifacts", "models")

os.makedirs(PLOT_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)


def save_plot(filename, plt):
    path = os.path.join(PLOT_DIR, filename)
    plt.savefig(path, dpi=300, bbox_inches="tight")
    print("Plot saved:", path)