# Forecasting Assistant

This is a Python-based web application built with Django, designed to run within a Docker container.

## Project Structure

*   `.devcontainer/`: Contains Docker configuration for development environment.
*   `forecastingsite/`: The main Django project directory.
*   `polls/`: A Django application within the project.
*   `db.sqlite3`: SQLite database file.
*   `manage.py`: Django's command-line utility for administrative tasks.

## Setup and Installation

This project is designed to be developed and run using Docker.

### Prerequisites

*   Docker installed on your system.

### Steps

1.  **Build the Docker image:**
    Navigate to the project root directory (where `Dockerfile` is located) and run:
    ```bash
    docker build . -t previsionnel-assistant
    ```

2.  **Install Python Dependencies:**
    The `requirements.txt` file is used to manage Python dependencies. Make sure to add your project's dependencies to this file.
    ```bash
    # Example: Add dependencies to requirements.txt
    # Django==X.Y.Z
    # ...
    ```
    The Docker build process will install these dependencies.

## Running the Application

After building the Docker image, you can run the application:

```bash
docker run -p 8000:8000 previsionnel-assistant
```

**Note:** The `CMD` in the `Dockerfile` uses `gunicorn`. You will need to ensure the `gunicorn` command correctly points to your Django project's WSGI application. Based on the current structure, it should be `forecastingsite.wsgi:application`.

The default `CMD` in the `Dockerfile` is `gunicorn --bind 0.0.0.0:8000 your_project_name.wsgi:application`.
You will need to update `your_project_name` to `forecastingsite` for the application to run correctly.

## Development

To work on this project, you can use the provided `.devcontainer` setup if you are using an IDE like VS Code that supports Development Containers.

### Running Migrations

Once the container is running, you can execute Django management commands inside the container. For example, to apply migrations:

```bash
docker exec <container_id_or_name> python manage.py migrate
```

You can find the `<container_id_or_name>` by running `docker ps`.
