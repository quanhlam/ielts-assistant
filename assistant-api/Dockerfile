# Development stage
FROM python:3.9 AS dev

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
        curl \
        netcat \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements files
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the app code
COPY . /app/

# Expose the port
EXPOSE 8000

# Set the command to run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Production stage
FROM python:3.9-slim AS prod

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
        curl \
        netcat \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements files
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install gunicorn

# Copy the app code
COPY . /app/

# Expose the port
EXPOSE 8000

# Set the command to run the app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "bag_api.wsgi:application"]
