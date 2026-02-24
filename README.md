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
# or
source venv/bin/activate  # On Linux/Mac
```

3. Install dependencies:
```bash
pip install django djangorestframework django-filter
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
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

### Filtering and Searching

- **Destinations**: Filter by `country`, `is_active`, `duration_days`. Search by `name`, `description`, `location`, `country`
- **Tour Packages**: Filter by `destination`, `is_active`. Search by `name`, `description`
- **Bookings**: Filter by `status`, `booking_date`, `package`. Search by `customer_name`, `customer_email`
- **Reviews**: Filter by `destination`. Search by `user__username`, `destination__name`, `comment`. Order by `rating`, `created_at`

### Booking Actions

- `POST /api/bookings/{id}/confirm/` - Confirm a booking
- `POST /api/bookings/{id}/cancel/` - Cancel a booking

## Authentication

The API supports token authentication. To obtain a token:

```bash
POST /api/auth/token/
Body: {"username": "your_username", "password": "your_password"}
```

Include the token in requests:
```
Authorization: Token your_token_here
```

## Testing with Postman

### Create a Review

```http
POST /api/reviews/
Authorization: Token your_token_here
Content-Type: application/json

{
  "destination": 1,
  "rating": 5,
  "comment": "Amazing experience! The beaches were beautiful."
}
```

### Get Reviews for a Destination

```http
GET /api/reviews/?destination=1
```

### Get All Reviews (with ordering)

```http
GET /api/reviews/?ordering=-created_at
```

## Models

### Destination
- `name` - Destination name
- `description` - Description text
- `location` - Location details
- `country` - Country
- `image_url` - URL to image
- `price_per_person` - Price per person
- `duration_days` - Duration in days
- `rating` - Average rating (0-5)
- `is_active` - Active status

### TourPackage
- `destination` - ForeignKey to Destination
- `name` - Package name
- `description` - Description
- `price` - Package price
- `duration_days` - Duration in days
- `available_slots` - Available slots
- `is_active` - Active status

### Booking
- `package` - ForeignKey to TourPackage
- `customer_name` - Customer name
- `customer_email` - Customer email
- `number_of_guests` - Number of guests
- `booking_date` - Date of booking
- `status` - Status (pending, confirmed, cancelled)
- `total_price` - Total price (auto-calculated)

### Payment
- `booking` - ForeignKey to Booking
- `amount` - Payment amount
- `payment_method` - Method (credit_card, debit_card, paypal, bank_transfer)
- `status` - Status (pending, completed, failed, refunded)
- `transaction_id` - External transaction ID
- `payment_date` - Date of payment

### Review
- `user` - ForeignKey to User
- `destination` - ForeignKey to Destination
- `rating` - Rating (1-5)
- `comment` - Review comment
- `created_at` - Creation timestamp

## License

MIT License
