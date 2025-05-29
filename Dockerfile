# Use official Python 3.9 image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Flask app code
COPY . .

# Expose the port Flask will run on
EXPOSE 5000

# Run your app
CMD ["python", "app.py"]
