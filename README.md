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
