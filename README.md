# Airline Management System

## Overview
This is a Django-based API for managing airlines, flights, and reservations. It provides endpoints for creating, reading, updating, and deleting data related to airplanes, flights, and reservations.

## Features
- **Airplane Management**: Create, read, update, and delete airplanes.
- **Flight Management**: Manage flights and associate them with airplanes.
- **Reservation Management**: Create and manage reservations for flights.

## Installation

**You need to have python and django downloaded on your local. Then you can follow the steps;**

### 1. Clone the Repository
  ```bash
  git clone https://github.com/your-username/airline-management-system.git
  cd airlinesystem


```

### 2. Set Up a Virtual Environment (venv)
MacOS/Linux
  ```bash
  python3 -m venv venv
  source venv/bin/activate

```

Windows
  ```bash
  python -m venv venv
  venv\Scripts\activate

```

### 3. Install Dependencies
   ```bash
  pip install -r requirements.txt

```

### 4. Set up a Secret Key
Create a .env file in the root of your project and add SECRET_KEY to that
  ```bash
  touch .env
  SECRET_KEY=your-secret-key-here

```

You can generate it by running;
  ```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'


```

### 5. Run Migrations
  ```bash
  python manage.py makemigrations
  python manage.py migrate

```

### 6. You can run the application
   ```bash
  python manage.py runserver

```





















