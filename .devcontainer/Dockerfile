# Stage 1: Build dependencies
FROM python:3.14-slim-bookworm as builder
ENV CONTAINER_NAME="forecasting-assistant"
ENV WORKDIR_PATH="/workspaces/forecasting-assistant"

WORKDIR $WORKDIR_PATH
# Install system dependencies needed for Python packages (e.g., psycopg2-binary)
# Adjust as per your specific database/other needs
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY .devcontainer/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy your Django application code
COPY . .
# Stage 2: Final production image

FROM python:3.14-slim-bookworm

#-------------------------------------------------------------
#       Repo Installation
#-------------------------------------------------------------
ENV PYTHONPATH $PYTHONPATH:$WORKDIR_PATH

WORKDIR $WORKDIR_PATH
# Install only runtime system dependencies if needed (e.g., libpq-dev for psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copy installed Python packages from the builder stage
COPY --from=builder /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
# Copy your Django application code from the builder stage
COPY --from=builder $WORKDIR_PATH .
# Expose the port your Django app runs on (e.g., Gunicorn)
EXPOSE 8000

# Command to run your Django application (e.g., with Gunicorn)
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project_name.wsgi:application"]
CMD ["sleep 600"]