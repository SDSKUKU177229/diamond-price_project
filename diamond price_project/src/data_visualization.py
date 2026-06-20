import os
import subprocess
import sys

# =========================
# PROGRAMMATIC INSTALLATION
# =========================
# This replaces the Jupyter-specific '!pip install seaborn' 
try:
    import seaborn as sns
except ImportError:
    print("Seaborn not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "seaborn"])
    import seaborn as sns

import matplotlib.pyplot as plt

# =========================
# SAVE PLOT HELPER
# =========================
def save_plot(filename):
    plot_dir = "../artifacts/plots"
    os.makedirs(plot_dir, exist_ok=True)

    path = os.path.join(plot_dir, filename)

    plt.savefig(path)
    print("Plot saved at:", path)


# =========================
# PLOTS
# =========================

def plot_price_hist(df):
    plt.figure() # Create a clean figure context
    df['price'].plot(kind='hist', bins=20)
    plt.title("Price Distribution")

    save_plot("price_hist.png")
    plt.show()
    plt.close() # Close the figure to free up memory


def plot_scatter(df):
    plt.figure()
    plt.scatter(df['carat'], df['price'])
    plt.title("Carat vs Price")

    save_plot("scatter.png")
    plt.show()
    plt.close()


def plot_heatmap(df):
    plt.figure()
    sns.heatmap(df.corr(numeric_only=True), annot=True)
    plt.title("Correlation Heatmap")

    save_plot("heatmap.png")
    plt.show()
    plt.close()


def plot_box(df):
    plt.figure()
    plt.boxplot(df['price'])
    plt.title("Price Boxplot")

    save_plot("boxplot.png")
    plt.show()
    plt.close()


def plot_cut_distribution(df):
    plt.figure()

    df['cut'].value_counts().plot(kind='bar')
    plt.title("Cut Distribution")

    save_plot("cut_distribution.png")
    plt.show()
    plt.close()