IMAGE_NAME = ml-model
CONTAINER_NAME = ml-model-container
PORT = 9000

# Build Docker image
build:
	@echo "Building Docker image: $(IMAGE_NAME)..."
	docker build -t $(IMAGE_NAME) .
	@echo "Docker image $(IMAGE_NAME) built successfully."

# Run Docker container
run:
	@echo "Running Docker container: $(CONTAINER_NAME)..."
	docker run -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)
	@echo "Docker container $(CONTAINER_NAME) is running on port $(PORT)."

# Stop and remove Docker container
stop:
	@echo "Stopping and removing Docker container: $(CONTAINER_NAME)..."
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true
	@echo "Docker container $(CONTAINER_NAME) stopped and removed."

# Rebuild and restart the container
restart: stop build run

# Clean up Docker image and container
clean:
	@echo "Cleaning up Docker image and container..."
	docker rm $(CONTAINER_NAME) || true
	docker rmi $(IMAGE_NAME) || true
	@echo "Cleanup completed. Docker image and container removed."