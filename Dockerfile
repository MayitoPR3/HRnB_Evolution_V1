# Start with an appropriate Alpine Linux base image with Python
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY . .

# Set environment variables
ENV PORT 5000

# Expose the port
EXPOSE $PORT

# Define a volume for persistent data storage
VOLUME ["/app/data"]

# Command to run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]
