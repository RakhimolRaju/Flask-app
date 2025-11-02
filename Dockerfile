# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files into the image
COPY . .

# Install Flask and any other dependencies
RUN pip install --no-cache-dir flask

# Expose the Flask app port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
