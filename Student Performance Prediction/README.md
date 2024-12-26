# Student Performance Prediction Using Machine Learning

This repository presents a machine learning project that analyzes student performance data and predicts grades based on average marks. The project is designed to introduce students to essential data science practices, including data preprocessing, visualization, feature engineering, and model training with Naive Bayes and Decision Tree classifiers.

## Project Overview
The objective of this project is to:
- Explore the **Student Performance** dataset by visualizing score distributions and examining factors such as gender and parental education.
- Perform **feature engineering** by calculating average marks and assigning grades based on scores.
- Train and evaluate **Naive Bayes** and **Decision Tree** models to classify students into grade categories.
- Save the trained model in a joblib file, allowing for reuse and deployment.

## Key Features
- **Data Visualization**: Includes histograms and bar charts to visualize scores and understand relationships.
- **Feature Engineering**: Adds new columns for average marks and grades to enhance predictive modeling.
- **Machine Learning Models**: Uses Naive Bayes and Decision Tree classifiers for grade prediction.
- **Model Persistence**: Saves the Decision Tree model for later use with joblib.

## Dataset
The dataset includes student performance data across multiple subjects (Math, Reading, Writing), as well as demographic information such as gender and parental education. It’s a useful dataset for educational analysis and modeling.

## Notable Observations
An **inverse correlation** exists between average marks and grade values due to the numeric grade mapping where higher grades (e.g., "A") are assigned lower values, while lower grades (e.g., "F") have higher values.

## Requirements
- Python 3.x
- Required Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Joblib

## Usage
After training, use the `predict` function to predict grades for new input scores, or load the saved Decision Tree model for deployment.


---
