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
    # Exercise 1
    # data = request.get_json()
    # input_features = np.array(data["features"]).reshape(1, -1)
    # prediction = model.predict(input_features)
    # confidence_score = model.predict_proba(input_features)[0][prediction[0]]  # Extract confidence for predicted class
    # return jsonify({"prediction": int(prediction[0]), "confidence": confidence_score})
    
    # Exercise 2
    # data = request.get_json()
    # input_features = np.array(data["features"].reshape(data.ndim, -1))
    # prediction = model.predict(input_features)
    # return jsonify({"prediction": predict.tolist()})
    
    # Exercise 3 
    def validate_inputs(features):
        if not isinstance(features, list):
            return False, "Input must be a list of feature arrays."
        for feature in features:
            if not isinstance(feature, list) or len(feature) != 4 or not all(isinstance(x, (float)) for x in feature):
                return False, "Each feature array must contain exactly 4 numeric values."
        return True, None
    data = request.get_json()
    is_valid, error_message = validate_inputs(data["features"])
    if is_valid:
        predictions = model.predict(np.array(data["features"]))
        print({"predictions": predictions.tolist()})
    else:
        print({"error": error_message})
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000) #check your port number ( if it is in use, change the port number)
