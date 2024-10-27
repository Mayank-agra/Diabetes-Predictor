# Diabetes-Predictor
This Diabetes Predictor is a machine learning-based tool designed to assess diabetes risk based on user health data. By leveraging a classification model, this project provides an efficient and reliable way to evaluate an individual's likelihood of having diabetes using health metrics often correlated with the condition.

# Project Overview
Diabetes Predictor is designed to help individuals and healthcare professionals gauge diabetes risk based on input health data. Using a trained classification model, this tool offers a user-friendly way to predict diabetes risk by analyzing health factors such as glucose levels, BMI, age, and blood pressure.

# Features
Health Metric Analysis: Uses key features (glucose, BMI, age, blood pressure) as inputs for risk prediction.
Model Performance: Employs accuracy, precision, recall, and F1-score to validate model predictions.
Simple Interface: Accepts health metrics and delivers immediate risk assessment.
Insights on Important Features: Highlights factors most relevant to prediction, useful for users and researchers.

# Getting Started
1. Clone the repository:
git clone https://github.com/Mayank-agra/diabetes-predictor.git

2. Install Dependencies:
   pip install streamlit

3. Run diabetes_prediction_ui.py file:
   streamlit run diabetes_prediction_ui.py file

# Model and Evaluation
Training Algorithm: The Diabetes Predictor uses a Support Vector Machine (SVM) algorithm, which is particularly effective for classification tasks by finding an optimal hyperplane to separate classes in the feature space. SVM was chosen for its robustness in handling high-dimensional data and effectiveness in classification accuracy.

# Results
The Diabetes Predictor outputs a straightforward classification, indicating whether an individual is "Diabetic" or "Not Diabetic" based on the input health data. 

