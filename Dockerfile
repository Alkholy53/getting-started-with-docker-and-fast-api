# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /fastapi-app

# Copy the current directory contents into the container at /app
COPY . /fastapi-app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose port 8000 to the outside world
EXPOSE 80

# Command to run FastAPI using uvicorn when the container starts
CMD ["uvicorn", "fastapi-app.main:app", "--host", "0.0.0.0", "--port", "80"]

