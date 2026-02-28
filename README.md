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

## Testing with Postman

### Step 1: Login
```
POST http://127.0.0.1:8000/api/auth/token/
Content-Type: application/json

{"username": "your_username", "password": "your_password"}
```

### Step 2: Create Destination
```
POST http://127.0.0.1:8000/api/destinations/
Authorization: Token YOUR_TOKEN_HERE
Content-Type: application/json

{"name": "Maldives Paradise", "description": "Beautiful tropical island resort", "location": "Male", "country": "Maldives", "image_url": "https://example.com/maldives.jpg", "price_per_person": 1500, "duration_days": 7, "is_active": true}
```

### Step 3: Create Tour Package
```
POST http://127.0.0.1:8000/api/tourpackages/
Authorization: Token YOUR_TOKEN_HERE
Content-Type: application/json

{"destination": 1, "name": "Luxury Maldives Package", "description": "7 days of paradise", "price": 2500, "duration_days": 7, "available_slots": 20, "is_active": true}
```

### Step 4: Create Booking
```
POST http://127.0.0.1:8000/api/bookings/
Authorization: Token YOUR_TOKEN_HERE
Content-Type: application/json

{"package": 1, "customer_name": "John Doe", "customer_email": "john@example.com", "number_of_guests": 2, "booking_date": "2026-03-15"}
```

### Step 5: Confirm Booking
```
POST http://127.0.0.1:8000/api/bookings/1/confirm/
Authorization: Token YOUR_TOKEN_HERE
```

### Step 6: Cancel Booking
```
POST http://127.0.0.1:8000/api/bookings/1/cancel/
Authorization: Token YOUR_TOKEN_HERE
```

### Step 7: Create Payment
```
POST http://127.0.0.1:8000/api/payments/
Authorization: Token YOUR_TOKEN_HERE
Content-Type: application/json

{"booking": 1, "amount": 2500, "payment_method": "credit_card", "payment_status": "pending"}
```

### Step 8: Update Payment Status
```
POST http://127.0.0.1:8000/api/payments/1/update_status/
Authorization: Token YOUR_TOKEN_HERE
Content-Type: application/json

{"payment_status": "completed", "transaction_reference": "TXN123456789"}
```

### Step 9: Create Review
```
POST http://127.0.0.1:8000/api/reviews/
Authorization: Token YOUR_TOKEN_HERE
Content-Type: application/json

{"destination": 1, "rating": 5, "comment": "Amazing experience!"}
```

### Step 10: Get Reviews
```
GET http://127.0.0.1:8000/api/reviews/?destination=1
```

### GET Requests
```
GET http://127.0.0.1:8000/api/destinations/
GET http://127.0.0.1:8000/api/tourpackages/
GET http://127.0.0.1:8000/api/bookings/
GET http://127.0.0.1:8000/api/payments/
```

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
