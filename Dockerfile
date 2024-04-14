# Use an existing Python image as a base
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy the rest of the application code into the container at /app
COPY . .

# Run any commands needed to set up the application
RUN python3 -m venv myvirenv
RUN python3 -m pip install Django
RUN python3 manage.py makemigrations members
RUN python3 manage.py migrate

# Expose the port that Django runs on
EXPOSE 8000

# Command to run the application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
