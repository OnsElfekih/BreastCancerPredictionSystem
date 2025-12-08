# Breast Cancer Prediction System

Web-based machine learning system that predicts if a patient’s tumor is benign (healthy) or malignant (sick) using clinical features.

## Overview

- Uses a Gradient Boosting Classifier trained on the Breast Cancer dataset.
- Features include Age, BMI, Glucose, Insulin, HOMA, Leptin, Adiponectin, Resistin, and MCP_1.
- Provides a web interface for real-time predictions.
- Includes preprocessing, model training, evaluation, and deployment.

## Project Structure

/backend/ ← Flask application and model script
├─ app.py ← Main Flask app for web interface
├─ gradient_boosting_model.pkl ← Saved trained model
└─ templates/
└─ index.html ← Frontend form and result display
/data/
└─ dataR2.csv ← Dataset used for training
requirements.txt ← Python dependencies
README.md ← Project documentation


## Prerequisites

- Python 3.7 or later
- Libraries:
  - Flask==3.1.0
  - numpy==2.1.3
  - pandas==2.3.3
  - scikit-learn==1.6.1
  - joblib==1.4.2
  - gunicorn==23.0.0

## Installation

1. Clone the repository:

```bash
git clone https://github.com/OnsElfekih/BreastCancerPredictionSystem.git
cd BreastCancerPredictionSystem
```

2. Create a virtual environment
  venv\Scripts\activate .venv\Scripts\Activate1

4. Install dependencies:
   pip install -r requirements.txt
   
5. Usage:
   - Run locally:
   cd backend
   python app.py
   - Online Deployement: https://breastcancerpredictionsystem-k643.onrender.com/

6. Workflow:
- Load and inspect the dataset dataR2.csv.
- Preprocess data and map target labels.
- Split dataset into training and test sets.
- Train a Gradient Boosting Classifier.
- Evaluate using accuracy, confusion matrix, and classification report.
- Save the trained model for predictions.
- Deploy the model using Flask with a web interface.


