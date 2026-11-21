# Student Score Prediction Model

Predicts a student's exam score from hours studied, comparing linear and polynomial regression, with a small Streamlit app for trying the model.

## Features
- Linear regression baseline with train/test split, MSE and R² evaluation
- Degree-2 polynomial regression compared against the linear fit
- Trained model saved with `joblib` and served in a Streamlit app

## Results
Hours studied alone explains about 20% of the variance in exam scores (R² ≈ 0.20 for both models); the polynomial curve adds almost nothing over a straight line. The dataset includes many other factors (attendance, previous scores, sleep, tutoring), which are the natural next step for a multi-feature model.

## Tech Stack
Python · pandas · scikit-learn · matplotlib · joblib · Streamlit

## How to Run
```bash
git clone https://github.com/Muqeet04/Student-Score-Prediction-Model.git
cd Student-Score-Prediction-Model
pip install -r requirements.txt
streamlit run app.py
```

The trained model (`poly_model.pkl`, `poly_transformer.pkl`) is included. To retrain, place the Student Performance Factors dataset as `spf.csv` in the project folder and run `score_prediction.ipynb`.
