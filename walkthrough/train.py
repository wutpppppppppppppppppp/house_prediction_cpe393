# save_model.py
import pickle
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X, y = iris.data, iris.target

model = RandomForestClassifier()
model.fit(X, y)

with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)

# Single input example
input_features = np.array([5.1, 3.5, 1.4, 0.2]).reshape(1, -1)
prediction = model.predict(input_features)
confidence_score = model.predict_proba(input_features)[0][prediction[0]]

# Output
print({"prediction": int(prediction[0]), "confidence": float(confidence_score)})

# Multiple input example
input_features = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [6.2, 3.4, 5.4, 2.3]
])
predictions = model.predict(input_features)

# Output
print({"predictions": predictions.tolist()})

def validate_inputs(features):
    if not isinstance(features, list):
        return False, "Input must be a list of feature arrays."
    for feature in features:
        if not isinstance(feature, list) or len(feature) != 4 or not all(isinstance(x, (float)) for x in feature):
            return False, "Each feature array must contain exactly 4 float values."
    return True, None

# Example input
input_features = [
    [5, 3, 1, 0],
    [6, 3, 5, 2]
]

is_valid, error_message = validate_inputs(input_features)
if is_valid:
    predictions = model.predict(np.array(input_features))
    print({"predictions": predictions.tolist()})
else:
    print({"error": error_message})