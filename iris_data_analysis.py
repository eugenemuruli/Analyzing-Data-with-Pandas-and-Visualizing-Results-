# iris_data_analysis_fixed.py
"""
Robust Iris analysis script that:
- ensures required packages are available (tries to install if missing),
- loads the iris dataset,
- prints basic exploration and stats,
- creates 4 plots: line, bar, histogram, scatter.
"""

import sys
import subprocess
import importlib
import traceback

# mapping pip package name -> import name
REQUIREMENTS = [
    ("pandas", "pandas"),
    ("matplotlib", "matplotlib"),
    ("seaborn", "seaborn"),
    ("scikit-learn", "sklearn"),
    ("numpy", "numpy")
]

def try_install(pip_name):
    """Try to install a pip package into the current Python interpreter."""
    print(f"Attempting to install '{pip_name}' into {sys.executable} ...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
        print(f"Installed {pip_name} successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {pip_name}. Error: {e}")
        return False

# Check imports, attempt install if missing
missing = []
for pip_name, import_name in REQUIREMENTS:
    try:
        importlib.import_module(import_name)
    except ImportError:
        missing.append((pip_name, import_name))

if missing:
    print("Missing packages detected:", missing)
    for pip_name, import_name in missing:
        ok = try_install(pip_name)
        if not ok:
            print(f"Automatic install failed for {pip_name}.")
            print(f"Please run manually: {sys.executable} -m pip install {pip_name}")
            sys.exit(1)
else:
    print("All required packages present.")

# Now safe to import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

def main():
    sns.set(style="whitegrid")
    iris = load_iris(as_frame=True)
    df = iris.frame.copy()
    df["species"] = df["target"].map(dict(zip(range(3), iris.target_names)))

    # Exploration
    print("\nFirst 5 rows:")
    print(df.head())

    print("\nInfo:")
    df.info()  # prints to stdout

    print("\nMissing values per column:")
    print(df.isnull().sum())

    print("\nDescriptive statistics:")
    print(df.describe())

    print("\nMean of features grouped by species:")
    grouped_means = df.groupby("species").mean()
    print(grouped_means)

    # Visualizations
    # 1) Line chart (simulated time: index)
    plt.figure(figsize=(8, 4))
    plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
    plt.title("Sepal Length Trend Over Index (simulated time)")
    plt.xlabel("Index")
    plt.ylabel("Sepal Length (cm)")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # 2) Bar chart (average petal length per species) - use numpy.mean as estimator
    plt.figure(figsize=(8, 4))
    sns.barplot(x="species", y="petal length (cm)", data=df, estimator=np.mean)
    plt.title("Average Petal Length per Species")
    plt.xlabel("Species")
    plt.ylabel("Average Petal Length (cm)")
    plt.tight_layout()
    plt.show()

    # 3) Histogram (distribution of sepal length)
    plt.figure(figsize=(8, 4))
    plt.hist(df["sepal length (cm)"], bins=15, edgecolor="black")
    plt.title("Distribution of Sepal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # 4) Scatter plot (sepal length vs petal length)
    plt.figure(figsize=(8, 4))
    sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
    plt.title("Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title="Species")
    plt.tight_layout()
    plt.show()

    print("\nDone. Plots displayed and analysis printed above.")

if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("An unexpected error occurred:")
        traceback.print_exc()
        sys.exit(1)
