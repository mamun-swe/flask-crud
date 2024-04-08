# Use the official Python image as base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port that the Flask app runs on
EXPOSE 8000

# Command to run the Flask application
CMD ["python3", "main.py"]