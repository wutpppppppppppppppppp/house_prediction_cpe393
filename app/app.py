from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "ML Model is Running"

# Exercise 4
@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}

@app.route("/predict", methods=["POST"])
def predict():
    def validate_inputs(features):
        if not isinstance(features, list):
            return False, "Input must be a list of feature arrays."
        for feature in features:
            if not isinstance(feature, list) or len(feature) != 4 or not all(isinstance(x, (float, int)) for x in feature):
                return False, "Each feature array must contain exactly 4 numeric values."
        return True, None

    # Get JSON data from the request
    data = request.get_json()

    # Validate input
    if "features" not in data:
        return jsonify({"error": "Missing 'features' key in request data"}), 400

    is_valid, error_message = validate_inputs(data["features"])
    if not is_valid:
        return jsonify({"error": error_message}), 400

    # Perform predictions
    input_features = np.array(data["features"])
    predictions = model.predict(input_features)

    # Handle confidence scores for single input
    if len(input_features) == 1:
        confidence_score = model.predict_proba(input_features)[0][predictions[0]]
        return jsonify({"prediction": int(predictions[0]), "confidence": float(confidence_score)})

    # Handle multiple inputs
    return jsonify({"predictions": predictions.tolist()})
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000) #check your port number ( if it is in use, change the port number)
