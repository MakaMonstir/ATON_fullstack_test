# Django Fullstack Test Project

## Overview

This is a Fullstack test project built with Django and PostgreSQL. It includes a user authentication system and allows authorized users to manage clients. Dummy data can be generated for testing purposes.

## Features

- User Authentication (Login, Logout)
- Client Management (View clients, Update client status)
- Admin Interface for managing users and clients
- Dockerized setup for easy deployment
- Dummy data generation using Faker

## Installation

### Requirements

- Docker
- Docker-compose

### Setup

1. **Clone repo:**

```sh
   git clone https://github.com/MakaMonstir/ATON_fullstack_test.git
   cd ATON_fullstack_test
```

2. **Build and start the Docker containers:**

```sh
docker-compose build
docker-compose up # or docker-compose up --build
```

3. **Run database migrations:**
```sh
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

4. **Create a superuser:**

```sh
docker-compose exec web python manage.py createsuperuser
```

5. **Generate dummy data (Optional):**
```sh
docker-compose exec web python manage.py create_dummy_data
```

### Usage

Accessing the app:
- The application can be accessed at http://localhost:8000
- The admin interface can be accessed at http://localhost:8000/admin

Admin interface:
- Use the superuser credentials to log in to the admin interface.
- Manage users and clients through the admin panel.

Dummy data:
- All users created with faker script has default password "password".
- See username at Admin page or at stdout in creation
