# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code into the container
COPY prototype/ ./prototype/
COPY prototype/client_secrets.json prototype/finalapp.py .

# Set environment variables if needed
# ENV VARIABLE_NAME=value

# Expose the port if necessary
# EXPOSE <port>

# Run the application
CMD ["python", "finalapp.py"]
