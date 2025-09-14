

 Iris Data Analysis and Visualization

 Project Overview

This project analyzes the **Iris dataset** using **Pandas** for data handling and **Matplotlib/Seaborn** for visualization.
It is designed to fulfill the assignment requirements of:

* Loading and exploring a dataset.
* Performing basic data analysis.
* Visualizing results with different types of plots.
* Drawing meaningful insights from the data.

---

 Requirements

Before running the program, ensure you have Python 3.x installed and the following libraries:

How to Run the Program

1. Clone or download this project folder to your computer.

2. Open a terminal/command prompt and navigate to the project directory:


3. Run the script:

  

4. The program will:

   * Load the **Iris dataset**.
   * Explore and clean the data (if needed).
   * Perform descriptive statistics and grouping.
   * Generate and display **four plots**:

     * **Line Chart** (simulated trend over index).
     * **Bar Chart** (mean petal length per species).
     * **Histogram** (distribution of sepal length).
     * **Scatter Plot** (relationship between sepal length and petal length).

 What the Program Does

Task 1: Load and Explore the Dataset

* Loads the **Iris dataset** using `sklearn.datasets.load_iris`.
* Converts it into a Pandas DataFrame.
* Displays the first rows, data types, and missing values.
* Cleans data (not much needed since Iris is already clean).

Task 2: Basic Data Analysis

* Uses `.describe()` to calculate **mean, median, standard deviation, etc.**
* Groups data by `species` and computes the **average petal length** per group.
* Highlights interesting patterns in the dataset.

 Task 3: Data Visualization

* **Line Chart**: Shows feature trend across samples.
* **Bar Chart**: Compares average petal length per species.
* **Histogram**: Distribution of sepal length.
* **Scatter Plot**: Sepal length vs. petal length relationship.

---

 Error Handling

* If a required library is missing, the program will show an error (`ModuleNotFoundError`).
* Install the missing library with `pip install <library-name>`.

