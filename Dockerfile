FROM python:3.10


# Working directory
WORKDIR /app


# Copy requirements.txt from computer to image and calls it requirements.txt
COPY requirements.txt requirements.txt


# Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Copies all files
COPY . .


# Run application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]





