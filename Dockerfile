# Use an official Python runtime as a parent image
FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_NO_INTERACTION 1

# Set work directory
WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy only the dependency file to leverage Docker layer caching
COPY pyproject.toml poetry.lock* ./

# Install dependencies
# --no-root: Do not install the project itself, only the dependencies
RUN poetry install --no-root --no-dev

# Copy the rest of the application code
COPY . .

# Install the project itself in editable mode
RUN poetry install --no-dev

# Expose the port the app runs on
EXPOSE 8000
