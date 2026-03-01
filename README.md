# Tourism Booking API

A Django REST Framework-based API for tourism booking management.

## Features

- **Destinations** - Manage tourism destinations
- **Tour Packages** - Create and manage tour packages linked to destinations
- **Bookings** - Handle customer bookings with price calculation
- **Payments** - Process and track payments
- **Reviews** - Allow users to review destinations

## Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite (default database)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/marymaya10/Tourism-Booking.git
cd Tourism-Booking
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install django djangorestframework django-filter
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/` | API root with available endpoints |
| `GET /api/destinations/` | List all destinations |
| `POST /api/destinations/` | Create a destination |
| `GET /api/tourpackages/` | List all tour packages |
| `POST /api/tourpackages/` | Create a tour package |
| `GET /api/bookings/` | List all bookings |
| `POST /api/bookings/` | Create a booking |
| `GET /api/payments/` | List all payments |
| `POST /api/payments/` | Create a payment |
| `GET /api/reviews/` | List all reviews |
| `POST /api/reviews/` | Create a review |

### Booking Actions

- `POST /api/bookings/{id}/confirm/` - Confirm a booking
- `POST /api/bookings/{id}/cancel/` - Cancel a booking

## Models

### Destination
- `name`, `description`, `location`, `country`, `image_url`, `price_per_person`, `duration_days`, `rating`, `is_active`

### TourPackage
- `destination`, `name`, `description`, `price`, `duration_days`, `available_slots`, `is_active`

### Booking
- `package`, `customer_name`, `customer_email`, `number_of_guests`, `booking_date`, `status`, `total_price`

### Payment
- `booking`, `amount`, `payment_method`, `payment_status`, `transaction_reference`, `created_at`

### Review
- `user`, `destination`, `rating`, `comment`, `created_at`

## License

MIT License


## API Testing Guide

This guide provides step-by-step instructions to test each API endpoint.

### Prerequisites

Run the server:
python manage.py runserver

API Base URL: http://127.0.0.1:8000

---

### Step 1: Authentication

- POST /api/auth/users/ - Register
- POST /api/auth/token/login/ - Login
- POST /api/auth/token/logout/ - Logout

---

### Step 2: Destinations API

- GET /api/destinations/ - List all
- POST /api/destinations/ - Create
- GET /api/destinations/{id}/ - Get one
- PUT /api/destinations/{id}/ - Update
- DELETE /api/destinations/{id}/ - Delete

---

### Step 3: Tour Packages API

- GET /api/tourpackages/ - List
- POST /api/tourpackages/ - Create
- GET /api/tourpackages/{id}/ - Get
- PUT /api/tourpackages/{id}/ - Update
- DELETE /api/tourpackages/{id}/ - Delete

---

### Step 4: Bookings API

- GET /api/bookings/ - List
- POST /api/bookings/ - Create
- GET /api/bookings/{id}/ - Get
- PUT /api/bookings/{id}/ - Update
- POST /api/bookings/{id}/confirm/ - Confirm
- POST /api/bookings/{id}/cancel/ - Cancel

---

### Step 5: Reviews API

- GET /api/reviews/ - List
- POST /api/reviews/ - Create

---

### Step 6: Payments API

- GET /api/payments/ - List
- POST /api/payments/ - Create
- POST /api/payments/{id}/update_status/ - Update status
- GET /api/payments/by-booking/{id}/ - Get by booking

---

### Testing Order

1. Register and Login
2. Destinations
3. Tour Packages
4. Bookings
5. Reviews
6. Payments
