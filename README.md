# Medical Data Classification System

## Overview
This project aims to build a classification system for medical data using Decision Trees. The project compares the performance of the Decision Tree model using different splitting criteria such as Gini, Chi-Square, Entropy, Gain Ratio, and Split Info.

## Project Structure
- `DataLoader`: Class responsible for loading and preprocessing the data.
- `DecisionTreeModel`: Class responsible for training and evaluating the Decision Tree model.
- `MetricsCalculator`: Class containing static methods to calculate various metrics such as Gini, Entropy, Gain Ratio, Split Info, and Chi-Square.
- `Visualization`: Class for plotting and visualizing the results.
- `Main`: Class to run the entire project.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/medical-data-classification.git
   cd medical-data-classification
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Prepare your medical data file (e.g., `data.csv`).
2. Run the project:
   ```bash
   python main.py data.csv
   ```

## Classes Description

### DataLoader
- **`__init__(self, file_path)`**: Initialize with the path to the data file.
- **`load_data(self)`**: Load data from the file.
- **`preprocess_data(self, data)`**: Clean and preprocess the data.

### DecisionTreeModel
- **`__init__(self, criterion='gini')`**: Initialize with the splitting criterion.
- **`train(self, X_train, y_train)`**: Train the model.
- **`evaluate(self, X_test, y_test)`**: Evaluate the model.
- **`visualize_tree(self)`**: Visualize the decision tree.

### MetricsCalculator
- **`calculate_gini(data)`**: Calculate Gini.
- **`calculate_entropy(data)`**: Calculate Entropy.
- **`calculate_gain_ratio(data)`**: Calculate Gain Ratio.
- **`calculate_split_info(data)`**: Calculate Split Info.
- **`calculate_chi_square(data)`**: Calculate Chi-Square.

### Visualization
- **`plot_results(results)`**: Plot the results and comparisons.

### Main
- **`run(file_path)`**: Run the entire project with the given data file path.

## Results
The project will output the classification performance of the Decision Tree model using different splitting criteria, along with visualizations of the decision trees and comparison plots.

## License
This project is licensed under the MIT License.
```

### Explanation of the Data Table

Assuming you are using a dataset similar to medical data, your table might look like this:

| Patient ID | Age | Gender | Blood Pressure | Cholesterol | Heart Disease |
|------------|-----|--------|----------------|-------------|---------------|
| 1          | 45  | Male   | High           | Normal      | Yes           |
| 2          | 54  | Female | Normal         | High        | No            |
| 3          | 34  | Male   | Low            | Normal      | No            |
| 4          | 67  | Female | High           | High        | Yes           |
| ...        | ... | ...    | ...            | ...         | ...           |

- **Patient ID**: Unique identifier for each patient.
- **Age**: Age of the patient.
- **Gender**: Gender of the patient (Male/Female).
- **Blood Pressure**: Blood pressure level (High/Normal/Low).
- **Cholesterol**: Cholesterol level (High/Normal/Low).
- **Heart Disease**: Target variable indicating the presence of heart disease (Yes/No).

This structure will allow you to train and evaluate your Decision Tree model effectively using different criteria for splitting the nodes.
