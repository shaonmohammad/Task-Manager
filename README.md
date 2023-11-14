# Task Manager
    Task Manager is a Django project designed to help users manage their daily tasks.
    It consists of two apps: `tasks` and `api`. The `tasks` app uses Django templates for rendering views, 
    while the `api` app provides an API for task management.

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL
- Pipenv (optional but recommended for managing virtual environments)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/shaonmohammad/Task-Manager.git
    cd Task_Manager
    ```

2. Install dependencies:

    ```bash
    pipenv install
    ```      

    If you're not using Pipenv, you can use `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

## Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
SECRET_KEY=django-insecure-tc87*rs!10gua3#bau_a6u+dow&bod^(#^(z6_9tx6=b$hir_6
API_KEY=dsfkjsdflwkjoie4urledwkjfrelwkjfelka
DEBUG=True
DB_NAME=task_manager
USER=shaon
PASSWORD=484251
HOST=localhost



---------------Configuration---------------
#Endpoints
  POST /api/token/
  Obtain JWT token by providing username and password.
  
  POST /api/token/refresh/
  Refresh JWT token.
  
  GET /api/tasks/
  Retrieve a list of tasks.

  GET /api/tasks/{task_id}/
  Retrieve details of a specific task.

  POST /api/tasks/
  Create a new task.

  PUT /api/tasks/{task_id}/  
  Update details of a specific task.

  DELETE /api/tasks/{task_id}/
  Delete a specific task.

-----------Running the Development Server------------
python manage.py runserver
Visit http://localhost:8000 in your browser.

------------------Dependencies-----------------
asgiref==3.7.2
Django==3.2
djangorestframework==3.14.0
djangorestframework-simplejwt==5.3.0
Pillow==10.1.0
psycopg2==2.9.9
PyJWT==2.8.0
python-decouple==3.8
pytz==2023.3.post1
sqlparse==0.4.4
