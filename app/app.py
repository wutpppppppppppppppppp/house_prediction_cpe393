from flask import Flask, request, jsonify
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("reg_model.pkl", "rb") as f:
    reg_model = pickle.load(f)

@app.route("/")
def home():
    return "ML Model is Running"

# Exercise 4
@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}

@app.route("/predict", methods=["POST"])
def predict():
    
    def preprocess_features(features):
        # Map categorical values to numerical values
        mappings = {
            "mainroad": {"yes": 1, "no": 0},
            "guestroom": {"yes": 1, "no": 0},
            "basement": {"yes": 1, "no": 0},
            "hotwaterheating": {"yes": 1, "no": 0},
            "airconditioning": {"yes": 1, "no": 0},
            "prefarea": {"yes": 1, "no": 0},
            "furnishingstatus": {"furnished": 0, "semi-furnished": 1, "unfurnished": 2},
        }

        processed_features = []
        for i, feature in enumerate(features):
            try:
                # Validate and normalize input
                if not isinstance(feature[4], str) or feature[4] not in mappings["mainroad"]:
                    raise ValueError(f"Invalid value for 'mainroad' at index {i}: {feature[4]}")
                if not isinstance(feature[5], str) or feature[5] not in mappings["guestroom"]:
                    raise ValueError(f"Invalid value for 'guestroom' at index {i}: {feature[5]}")
                if not isinstance(feature[6], str) or feature[6] not in mappings["basement"]:
                    raise ValueError(f"Invalid value for 'basement' at index {i}: {feature[6]}")
                if not isinstance(feature[7], str) or feature[7] not in mappings["hotwaterheating"]:
                    raise ValueError(f"Invalid value for 'hotwaterheating' at index {i}: {feature[7]}")
                if not isinstance(feature[8], str) or feature[8] not in mappings["airconditioning"]:
                    raise ValueError(f"Invalid value for 'airconditioning' at index {i}: {feature[8]}")
                if not isinstance(feature[10], str) or feature[10] not in mappings["prefarea"]:
                    raise ValueError(f"Invalid value for 'prefarea' at index {i}: {feature[10]}")
                if not isinstance(feature[11], str) or feature[11] not in mappings["furnishingstatus"]:
                    raise ValueError(f"Invalid value for 'furnishingstatus' at index {i}: {feature[11]}")

                processed_feature = [
                    int(feature[0]),  # area (ensure it's an integer)
                    int(feature[1]),  # bedrooms
                    int(feature[2]),  # bathrooms
                    int(feature[3]),  # stories
                    mappings["mainroad"][feature[4]],  # map yes/no
                    mappings["guestroom"][feature[5]],
                    mappings["basement"][feature[6]],
                    mappings["hotwaterheating"][feature[7]],
                    mappings["airconditioning"][feature[8]],
                    int(feature[9]),  # parking (ensure it's an integer)
                    mappings["prefarea"][feature[10]],
                    mappings["furnishingstatus"][feature[11]],  # furnishingstatus is already a string
                ]
                processed_features.append(processed_feature)
            except (ValueError, TypeError) as e:
                # Handle invalid data types or missing mappings
                raise ValueError(f"Invalid data format in feature at index {i}: {feature}. Error: {e}")
        return processed_features

    # Get JSON data from the request
    data = request.get_json()

    # Handle single feature array
    if "features" in data and isinstance(data["features"], list) and all(isinstance(x, (int, float, str)) for x in data["features"]):
        data["features"] = [data["features"]]

    # Validate input
    if "features" not in data:
        return jsonify({"error": "Missing 'features' key in request data"}), 400

    try:
        # Preprocess features
        processed_features = preprocess_features(data["features"])

        # Convert to DataFrame with correct column names
        feature_columns = ["area", "bedrooms", "bathrooms", "stories", "mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "parking", "prefarea", "furnishingstatus"]
        input_features = pd.DataFrame(processed_features, columns=feature_columns)

        # Perform predictions
        predictions = reg_model.predict(input_features)

        # Return predictions
        return jsonify({"predictions": predictions.tolist()})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000) #check your port number ( if it is in use, change the port number)
