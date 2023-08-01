# Use the official Python 3.9 image as the base image
FROM python:3.9

# Set environment variables
ENV DB_NAME=shopify
ENV DB_USER=kuma
ENV DB_USER_PASSWORD=geeksstudents
ENV DB_HOST=db
ENV DB_PORT=5432

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Expose the port that the Django application will listen on
EXPOSE 8000

# Command to run the Django development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]