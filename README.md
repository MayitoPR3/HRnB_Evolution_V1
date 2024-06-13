# HBnB Evolution Project

## Overview

This project involves creating a web application, HBnB Evolution, modeled after Airbnb using Python and Flask. The tasks include developing UML diagrams, implementing classes and business logic, creating RESTful APIs, and containerizing the application using Docker.

## Directory Structure

The project directory is structured as follows:


## Task 4: Implement the Country and City Management Endpoints

### Files
- `api/api_country.py`
- `api/api_city.py`
- `model/country.py`
- `model/city.py`
- `datamanagment.py`

### Summary
These files define the endpoints for managing country and city entities, including creation, retrieval, updating, and deletion. The data is validated to ensure the integrity and relationships between countries and cities.

## Task 5: Implement the Amenity Management Endpoints

### Files
- `api/api_amenities.py`
- `model/amenities.py`
- `datamanagment.py`

### Summary
These files define the endpoints for managing amenity entities. It includes CRUD operations for amenities, ensuring data integrity and validation to prevent duplicates.

## Task 6: Implement the Places Management Endpoints

### Files
- `api/api_places.py`
- `model/places.py`
- `datamanagment.py`

### Summary
These files define the endpoints for managing places. The implementation ensures that places are correctly linked to existing cities and amenities, with appropriate validation and detailed API responses.

## Task 7: Implement the Review Management Endpoints

### Files
- `api/api_review.py`
- `model/reviews.py`
- `datamanagment.py`

### Summary
These files define the endpoints for managing reviews. The implementation ensures reviews are linked to both users and places, with validation for ratings and preventing users from reviewing their own places.

## Task 8: Containerize the Application

### Files
- `Dockerfile`
- `app.py`
- `requirements.txt`

### Summary
The Dockerfile is set up to build the application into a Docker container using Alpine Linux and Gunicorn. It includes environment variable configuration for the application port and defines a volume for persistent data storage.

## Building and Running the Docker Container

### Building the Docker Image

To build the Docker image, navigate to the directory containing the `Dockerfile` and run:

```sh
docker build -t hbnb-api .

## Running the Docker Image
To run the Docker container with a persistent volume for data storage and a specified port:

docker run -d -p 5000:5000 -v $(pwd)/data:/app/data -e PORT=5000 hbnb-api

-d: Run the container in detached mode.
-p 5000:5000: Map port 5000 on the host to port 5000 in the container.
-v $(pwd)/data:/app/data: Mount the data directory on the host to /app/data in the container for persistent storage.
-e PORT=5000: Set the PORT environment variable to 5000.
You can change the port and volume paths as needed.

### Accessing the API
Once the container is running, you can access the API at http://localhost:5000.

### Stopping the Container
To stop the running container, use:
docker stop <container_id>

Replace <container_id> with the actual container ID obtained from docker ps.

### Removing the Container
To remove the stopped container, use:
docker rm <container_id>

Replace <container_id> with the actual container ID.

### Example of running tests with pytest:
pytest tests


### API Documentation
The API is documented using Flask-RESTx, which provides a Swagger UI for easy interaction and testing. Access the API documentation at http://localhost:5000 after starting the Docker container.

### Conclusion
This project involves creating a robust and scalable web application using Flask and Docker. The tasks include implementing various endpoints for managing entities and containerizing the application to ensure consistency across different environments. The provided documentation and files ensure a smooth setup and deployment process.


To download this `README.md` file, copy the above content into a text editor and save it as `README.md` in your project's root directory. This file will serve as a comprehensive guide for anyone working with or deploying your application.
