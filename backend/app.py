from flask import Flask, render_template, request
import joblib
import numpy as np
import os

# Chemins vers frontend
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
template_folder = os.path.join(frontend_path, "templates")
static_folder = os.path.join(frontend_path, "static")

# Création de l'application Flask
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

# Charger le modèle
model_path = os.path.join(os.path.dirname(__file__), "gradient_boosting_model.pkl")
model = joblib.load(model_path)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    show_result = False

    if request.method == "POST":
        try:
            age = float(request.form.get("age", ""))
            BMI = float(request.form.get("BMI", ""))
            glucose = float(request.form.get("glucose", ""))
            insulin = float(request.form.get("insulin", ""))
            HOMA = float(request.form.get("HOMA", ""))
            leptin = float(request.form.get("leptin", ""))
            adiponectin = float(request.form.get("adiponectin", ""))
            resistin = float(request.form.get("resistin", ""))
            MCP_1 = float(request.form.get("MCP_1", ""))

            X_new = np.array([[age, BMI, glucose, insulin, HOMA, leptin, adiponectin, resistin, MCP_1]])
            pred = model.predict(X_new)[0]

            prediction = "healthy" if pred == 0 else "sick"
            show_result = True

        except ValueError:
            prediction = None
            show_result = False

    return render_template("index.html", prediction=prediction, show_result=show_result)

if __name__ == "__main__":
    app.run(debug=True)
