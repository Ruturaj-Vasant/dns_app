# Ruturaj Vasant Tambe DCN Lab 3 N10333254
# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server code into the container
COPY fibonacci_server.py ./

# Expose the port for the server
EXPOSE 9090

# Command to run the application
CMD ["python", "fibonacci_server.py"]