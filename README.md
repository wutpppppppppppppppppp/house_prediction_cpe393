# Housing Price Prediction 🏠

This project is an assignment in CPE393 Machine Learning Operation. The key of this project is to deploy regression model it via docker. In this project, the model is trained with housing price along with features and then saved as a model. After run this project, you can send a request to port 9000 for prediction and status checking.

## Setup

### Prerequisite

'''
python > 3.9
'''
Make sure you have GNU Make. Check this by typing 'make clean' in root folder of the project

1. Run train.py to save the trained model (reg_model.pkl will be saved in app folder)
2. Run 'make build' to build docker image of this flask backend
3. Run 'make run' to run the docker container
4. Access 'localhost:9000/health' to check if the setup is done or not

## Example

- / (root)
- Expected Output
  "ML Model is Running"

- /health
- Expected Output
  {
  "status":"ok"
  }

- /predict
- Header
  Content-Type : application/json
- Body
  {
  "features": [
  [7420, 4, 2, 3, "yes", "no", "no", "no", "yes", 2, "yes", "furnished"],
  [8960, 4, 4, 4, "yes", "no", "no", "no", "yes", 3, "no", "furnished"]
  ]
  }

Run train.py. (model.pkl will be saved in app folder)

# Go to the directory in terminal

cd "project folder directory"

# Build Docker image

docker build -t ml-model .

# Run Docker container

docker run -p 9000:9000 ml-model

# Test the API in new terminal

curl -X POST http://localhost:9000/predict \
 -H "Content-Type: application/json" \
 -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

expected output

{"prediction": 0}
