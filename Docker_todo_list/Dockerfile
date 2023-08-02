# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container's working directory
COPY . /app/

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask application will listen on (replace with the appropriate port)
EXPOSE 5050

# Set environment variables (replace with your MongoDB settings if needed)
ENV MONGO_HOST=localhost
ENV MONGO_PORT=27017
ENV FLASK_ENV=production
ENV PORT=5050

# Run the Flask application when the container starts
CMD ["python", "-u", "app.py"]