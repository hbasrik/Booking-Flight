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
  git clone https://github.com/your-username/booking-flight.git
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

### 7. You can check the endpoints based on these urls;


## **Airplanes**

**GET** /api/airplanes/: List all airplanes.

**GET** /api/airplanes/tail_number/: Get spesific airplane.

**GET** /api/airplanes/tail_number/flights: Get the flights of a specific airplane.

**POST** /api/airplanes/: Create a new airplane.

**PATCH** /api/airplanes/tail_number/: Update a specific airplane.

**DELETE** /api/airplanes/tail_number/: Delete a specific airplane.


## **Flights**

**GET** /api/flights/: List all flights.

**GET** /api/flights/{id}/: Get spesific flight.

**GET** /api/flights/{id}/reservations: Get reservations made for a specific flight.

**POST** /api/flights/: Create a new flight.

**PATCH** /api/flights/{id}/: Update a specific flight.

**DELETE** /api/flights/{id}/: Delete a specific flight.



## **Reservations**

**GET** /api/reservations/: List all reservations.

**GET** /api/reservations/{id}/: Get details of a specific reservation.

**POST** /api/reservations/: Create a new reservation.

**PATCH** /api/reservations/{id}/: Update a specific reservation.






















