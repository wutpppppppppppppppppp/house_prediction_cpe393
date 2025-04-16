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
            print("Debug: 'features' is not a list. Received:", type(features))
            return False, "Input must be a list of feature arrays."
        
        for i, feature in enumerate(features):
            if not isinstance(feature, list):
                print(f"Debug: Feature at index {i} is not a list. Received:", type(feature))
                return False, "Each feature array must be a list of numeric values."
            if len(feature) != 4:
                print(f"Debug: Feature at index {i} does not have exactly 4 elements. Received length:", len(feature))
                return False, "Each feature array must contain exactly 4 numeric values."
            if not all(isinstance(x, (float, int)) for x in feature):
                invalid_elements = [x for x in feature if not isinstance(x, (float, int))]
                print(f"Debug: Feature at index {i} contains non-numeric values. Invalid elements:", invalid_elements)
                return False, "Each feature array must contain exactly 4 numeric values."
        
        return True, None

    # Get JSON data from the request
    data = request.get_json()

    # Handle case where "features" is a single list of floats
    if "features" in data and isinstance(data["features"], list) and all(isinstance(x, (float, int)) for x in data["features"]):
        data["features"] = [data["features"]]  # Wrap single feature array in a list

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
