# Pull base image
FROM python:3.15.0rc2-slim-bookworm

# Set environmental variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# set working dirctory
WORKDIR /app


# Install dependency
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy project
COPY . .

