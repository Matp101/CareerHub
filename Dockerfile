# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory into the container
COPY . /app/

# Expose the port that your Flask app will be running on (e.g., 5000)
EXPOSE 5000

# Set the environment variable to run the Flask app
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Run the Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
