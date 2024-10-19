# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]