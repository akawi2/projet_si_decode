# Use the official Python image from Docker Hub
FROM python:3.12.4

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install the dependencies
RUN pip install -r requirements.txt

# RUN python manage.py collectstatic --noinput

# Copy the entire project
COPY . .
    
# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "test5.py"]