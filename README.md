# Breast Cancer Prediction System

Web-based machine learning system that predicts if a patient’s tumor is benign (healthy) or malignant (sick) using clinical features.

## Overview

- Uses a Gradient Boosting Classifier trained on the Breast Cancer dataset.
- Features include Age, BMI, Glucose, Insulin, HOMA, Leptin, Adiponectin, Resistin, and MCP_1.
- Provides a web interface for real-time predictions.
- Includes preprocessing, model training, evaluation, and deployment.

## Project Structure
```
📁 BreastCancerPrediction
├─ 📁 backend
│  ├─ 📝 main.py                     # Train model, cross-validation, save model
│  ├─ 📝 app.py                      # Flask app for frontend
│  ├─ 💾 gradient_boosting_model.pkl # Saved trained model
│  ├─ 📄 dataR2.csv                  # Dataset used for training
│  ├─ 📝 requirements.txt            # Python dependencies
│  ├─ 📊 ML.ipynb                    # ML notebook with Python code
│  └─ 📂 venv                        # Python virtual environment
│
├─ 📁 frontend
│  ├─ 📂 templates
│  │  └─ 🖥️ index.html               # Frontend form and result display
│  └─ 📂 static
│     ├─ 🖼️ logo.ico                 # Project logo
│     └─ 🎨 style.css                # CSS styling
│
└─ 📝 README.md                      # Project documentation


```

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
```bash
  venv\Scripts\activate .venv\Scripts\Activate1
```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Usage:
   - Run locally:
   cd backend
   python app.py
   - Online Deployement: https://breastcancerpredictionsystem-k643.onrender.com/

7. Workflow:
- Load and inspect the dataset dataR2.csv.
- Preprocess data and map target labels.
- Split dataset into training and test sets.
- Train a Gradient Boosting Classifier.
- Evaluate using accuracy, confusion matrix, and classification report.
- Save the trained model for predictions.
- Deploy the model using Flask with a web interface.


---

## 👩‍💻 Author

**Ons Elfekih**  
IT Engineering Student — Business Intelligence  
🔗 [LinkedIn](https://www.linkedin.com/in/ons-elfekih) · [Portfolio](https://portfolio-elfekih-ons.vercel.app/)

---

## 📄 License

This project is for academic and portfolio purposes.



