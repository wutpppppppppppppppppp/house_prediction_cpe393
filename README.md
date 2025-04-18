# 🏠 Housing Price Prediction API

This project is part of the **CPE393 Machine Learning Operations** course. The goal is to deploy a regression model for predicting housing prices using Flask and Docker. The trained model is exposed via a REST API, allowing users to send requests for predictions and health checks.

---

## 📖 Project Description

The project involves:

- Training a regression model on a housing dataset.
- Deploying the model as a Flask API.
- Dockerizing the application for easy deployment.
- Handling multiple inputs, input validation, and confidence scores.

---

## ⚙️ Setup Instructions

### Prerequisites

- **Python**: Version `>= 3.9`
- **GNU Make**: Ensure it is installed by running `make --version`.
- **Docker**: Installed and running.

### Steps

1. **Train the Model**:
   - Run `train.py` to train the regression model and save it as `reg_model.pkl` in the `app` folder.
   ```bash
   python train.py
   ```
````

- This step ensures the model is ready for deployment.

2. **Build the Docker Image**:

   - Use the Makefile to build the Docker image.

   ```bash
   make build
   ```

3. **Run the Docker Container**:

   - Start the Flask API inside a Docker container.

   ```bash
   make run
   ```

4. **Check the API**:

   - Visit `http://localhost:9000/health` to verify the API is running.

5. **Stop and Clean Up**:
   - Stop and remove the container when done.
   ```bash
   make stop
   ```

---

## 🌐 API Endpoints

###1. **Root Endpoint**

- **URL**: `/`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "message": "ML Model is Running"
  }
  ```

### 2. **Health Check**

- **URL**: `/health`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "status": "ok"
  }
  ```

### 3. **Prediction**

- **URL**: `/predict`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "features": [
      [7420, 4, 2, 3, "yes", "no", "no", "no", "yes", 2, "yes", "furnished"],
      [8960, 4, 4, 4, "yes", "no", "no", "no", "yes", 3, "no", "furnished"]
    ]
  }
  ```
- **Response**:

  ```json
  {
    "predictions": [13300000, 12250000]
  }
  ```

- **Error Example**:
  ```json
  {
    "error": "Invalid value for 'mainroad' at index 0: 1"
  }
  ```

---

## 🐳 Docker Commands

- **Build the Docker Image**:

  ```bash
  make build
  ```

- **Run the Docker Container**:

  ```bash
  make run
  ```

- **Stop and Remove the Container**:

  ```bash
  make stop
  ```

- **Clean Up Docker Image and Container**:
  ```bash
  make clean
  ```

---

## 📂 Folder Structure

```
.
├── app/
│   ├── app.py          # Flask API code
│   ├── reg_model.pkl   # Trained regression model
├── train.py            # Model training script
├── Dockerfile          # Docker configuration
├── Makefile            # Makefile for Docker commands
├── README.md           # Project documentation
```

---

## ✨ Sample Usage

1. **Train the Model**:

   ```bash
   python train.py
   ```

2. **Build and Run the API**:

   ```bash
   make build
   make run
   ```

3. **Send a Prediction Request**:

   ```bash
   curl -X POST http://localhost:9000/predict \
   -H "Content-Type: application/json" \
   -d '{
         "features": [
           [7420, 4, 2, 3, "yes", "no", "no", "no", "yes", 2, "yes", "furnished"]
         ]
       }'
   ```

4. **Expected Response**:
   ```json
   {
     "predictions": [13300000]
   }
   ```

---

## 📋 Notes

- Ensure the Housing.csv dataset is in the project directory before running train.py.
- Use the Makefile for easier Docker management.
- The API validates inputs and returns clear error messages for invalid data.

---

## 🛠️ Authors

- **Your Name**  
  CPE393 Machine Learning Operations
