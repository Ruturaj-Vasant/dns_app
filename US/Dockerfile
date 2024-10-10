# Ruturaj Vasant Tambe DCN Lab 3 N10333254
# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8080 and run the application
EXPOSE 8080
CMD ["python", "app.py"]