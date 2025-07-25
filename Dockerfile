# Use the official lightweight Python image as a base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file first to take advantage of Docker's build cache
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's source code to the container
COPY . .

# Specify the default command to run when the container starts
# This should be your main application script
CMD ["python", "model/cognate.py"]