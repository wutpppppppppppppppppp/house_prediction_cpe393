# 🏡 Housing Price Prediction API

A containerized Machine Learning API for predicting housing prices built with **Flask** and **Docker**, developed as part of the **CPE393 - Machine Learning Operations** course.

This project demonstrates how to train a regression model, serve it as a RESTful API, validate inputs, and manage deployments using Docker.

---

## 📚 Table of Contents

- [📖 Project Description](#-project-description)
- [⚙️ Setup Instructions](#-setup-instructions)
- [🧰 Makefile Commands](#-makefile-commands)
- [🌐 API Endpoints](#-api-endpoints)
- [📂 Folder Structure](#-folder-structure)
- [🚀 Sample Usage](#-sample-usage)
- [❗ Troubleshooting](#-troubleshooting)
- [📋 Notes](#-notes)
- [🛠️ Authors](#-authors)

---

## 📖 Project Description

This project covers the following:

- 📊 Training a regression model using a housing dataset.
- 🌐 Serving predictions through a Flask API.
- 🐳 Containerizing the app with Docker.
- 🧪 Validating user inputs with helpful error messages.
- 📈 Returning predictions and confidence scores for multiple inputs.

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

Ensure the following are installed:

- **Python**: `>= 3.9`
- **Docker**
- **GNU Make** (Optional but recommended)

### 🛠 Steps

1. **Train the Model**

   Generate the regression model file before deploying:

   ```bash
   python train.py
   ```

2. **Build the Docker Image**

   ```bash
   make build
   ```

3. **Run the Docker Container**

   ```bash
   make run
   ```

4. **Test the API**

   Visit: [http://localhost:9000/health](http://localhost:9000/health)

5. **Stop the Container**

   ```bash
   make stop
   ```

6. **Optional Cleanup**

   Remove both the container and image:

   ```bash
   make clean
   ```

---

## 🧰 Makefile Commands

The project includes a `Makefile` to simplify common Docker operations. Use the following commands to manage the application efficiently.

> 📝 **Note**: All commands below are run from the root directory of the project.

---

### 🔨 `make build`

Builds the Docker image using the name defined in the Makefile (`ml-model`).

```bash
make build
```

**Equivalent to:**

```bash
docker build -t ml-model .
```

---

### 🚀 `make run`

Runs the Docker container and maps port `9000` from container to host.

```bash
make run
```

**Equivalent to:**

```bash
docker run -p 9000:9000 --name ml-model-container ml-model
```

---

### 🛑 `make stop`

Stops and removes the running container (`ml-model-container`), if it exists.

```bash
make stop
```

**Equivalent to:**

```bash
docker stop ml-model-container
docker rm ml-model-container
```

---

### ♻️ `make restart`

A shortcut to **stop**, **rebuild**, and **run** the Docker container in one step.

```bash
make restart
```

**Does:**

```bash
make stop
make build
make run
```

---

### 🧹 `make clean`

Removes both the Docker container and the Docker image completely.

```bash
make clean
```

**Equivalent to:**

```bash
docker rm ml-model-container
docker rmi ml-model
```

---

### ✅ Summary Table

| Command        | Description                                      |
|----------------|--------------------------------------------------|
| `make build`   | Build the Docker image                           |
| `make run`     | Run the Flask app inside a Docker container      |
| `make stop`    | Stop and remove the running Docker container     |
| `make restart` | Stop, rebuild, and run the container             |
| `make clean`   | Remove both the Docker container and the image   |

---

## 🌐 API Endpoints

### 1. `/` — Root

- **Method**: `GET`
- **Response**:

  ```json
  {
    "message": "ML Model is Running"
  }
  ```

---

### 2. `/health` — Health Check

- **Method**: `GET`
- **Response**:

  ```json
  {
    "status": "ok"
  }
  ```

---

### 3. `/predict` — Predict Prices

- **Method**: `POST`
- **Request Body**:

  ```json
  {
    "features": [
      [7420, 4, 2, 3, "yes", "no", "no", "no", "yes", 2, "yes", "furnished"]
    ]
  }
  ```

- **Response**:

  ```json
  {
    "predictions": [13300000]
  }
  ```

- **Error Response Example**:

  ```json
  {
    "error": "Invalid value for 'mainroad' at index 0: 1"
  }
  ```

---

## 📂 Folder Structure

```
.
├── app/
│   ├── app.py            # Flask app with API endpoints
│   └── reg_model.pkl     # Trained regression model
├── train.py              # Script to train and save the model
├── Dockerfile            # Docker configuration
├── Makefile              # Automation with Docker commands
├── README.md             # Documentation (this file)
└── Housing.csv           # Dataset used for training
```

---

## 🚀 Sample Usage

1. **Train the Model**

   ```bash
   python train.py
   ```

2. **Build and Run the API**

   ```bash
   make build
   make run
   ```

3. **Send a Prediction Request**

   ```bash
   curl -X POST http://localhost:9000/predict \
     -H "Content-Type: application/json" \
     -d '{
           "features": [
             [7420, 4, 2, 3, "yes", "no", "no", "no", "yes", 2, "yes", "furnished"]
           ]
         }'
   ```

4. **Expected Response**

   ```json
   {
     "predictions": [13300000]
   }
   ```

---

## ❗ Troubleshooting

- **Error: `make: command not found`**
  - You're likely on Windows without GNU Make. You can:
    - Use Git Bash or WSL.
    - Manually run the Docker commands from the Makefile.

- **Port Already in Use**
  - Stop other apps using port `9000`, or change the port in the Makefile and Flask app.

- **Model Not Found**
  - Ensure `train.py` is run before starting the container.

---

## 📋 Notes

- ✅ Input validation ensures safer predictions.
- ✅ Clear error messages help with debugging requests.
- ✅ Docker makes it easy to deploy on any environment.
- 🧪 Consider writing tests (unit/integration) for endpoints.
- 🗃️ Add logging for better traceability in production environments.

---

## 🛠️ Authors

- **Panyawut Piyasirinanan**  
  *CPE393 - Machine Learning Operations*
