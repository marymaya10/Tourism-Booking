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

### Filtering and Searching

- **Destinations**: Filter by `country`, `is_active`, `duration_days`. Search by `name`, `description`, `location`, `country`
- **Tour Packages**: Filter by `destination`, `is_active`. Search by `name`, `description`
- **Bookings**: Filter by `status`, `booking_date`, `package`. Search by `customer_name`, `customer_email`
- **Reviews**: Filter by `destination`. Search by `user__username`, `destination__name`, `comment`. Order by `rating`, `created_at`

### Booking Actions

- `POST /api/bookings/{id}/confirm/` - Confirm a booking
- `POST /api/bookings/{id}/cancel/` - Cancel a booking

## Testing with Postman

Follow these steps in order to test the API:

### Step 1: Login (Get Authentication Token)

```http
POST http://127.0.0.1:8000/api/auth/token/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**
```json
{
  "token": "your_token_here"
}
```

Copy this token for all subsequent requests.

---

### Step 2: Create a Destination

```http
POST http://127.0.0.1:8000/api/destinations/
Authorization: Token your_token_here
Content-Type: application/json

{
  "name": "Maldives Paradise",
  "description": "Beautiful tropical island resort",
  "location": "Male",
  "country": "Maldives",
  "image_url": "https://example.com/maldives.jpg",
  "price_per_person": 1500.00,
  "duration_days": 7,
  "is_active": true
}
```

---

### Step 3: Create a Tour Package

```http
POST http://127.0.0.1:8000/api/tourpackages/
Authorization: Token your_token_here
Content-Type: application/json

{
  "destination": 1,
  "name": "Luxury Maldives Package",
  "description": "7 days of paradise with all-inclusive",
  "price": 2500.00,
  "duration_days": 7,
  "available_slots": 20,
  "is_active": true
}
```

---

### Step 4: Create a Booking

```http
POST http://127.0.0.1:8000/api/bookings/
Authorization: Token your_token_here
Content-Type: application/json

{
  "package": 1,
  "customer_name": "John Doe",
  "customer_email": "john.doe@example.com",
  "number_of_guests": 2,
  "booking_date": "2026-03-15"
}
```

---

### Step 5: Confirm a Booking

```http
POST http://127.0.0.1:8000/api/bookings/1/confirm/
Authorization: Token your_token_here
Content-Type: application/json
```

---

### Step 6: Cancel a Booking (Optional)

```http
POST http://127.0.0.1:8000/api/bookings/1/cancel/
Authorization: Token your_token_here
Content-Type: application/json
```

---

### Step 7: Create a Payment

```http
POST http://127.0.0.1:8000/api/payments/
Authorization: Token your_token_here
Content-Type: application/json

{
  "booking": 1,
  "amount": 2500.00,
  "payment_method": "credit_card",
  "payment_status": "pending"
}
```

---

### Step 8: Update Payment Status

```http
POST http://127.0.0.1:8000/api/payments/1/update_status/
Authorization: Token your_token_here
Content-Type: application/json

{
  "payment_status": "completed",
  "transaction_reference": "TXN123456789"
}
```

---

### Step 9: Create a Review

```http
POST http://127.0.0.1:8000/api/reviews/
Authorization: Token your_token_here
Content-Type: application/json

{
  "destination": 1,
  "rating": 5,
  "comment": "Amazing experience! The beaches were beautiful."
}
```

---

### Step 10: Get All Reviews for a Destination

```http
GET http://127.0.0.1:8000/api/reviews/?destination=1
```

---

### Step 11: Get All Reviews (Ordered by Date)

```http
GET http://127.0.0.1:8000/api/reviews/?ordering=-created_at
```

---

### Additional GET Requests

**Get All Destinations:**
```http
GET http://127.0.0.1:8000/api/destinations/
```

**Get All Tour Packages:**
```http
GET http://127.0.0.1:8000/api/tourpackages/
```

**Get All Bookings:**
```http
GET http://127.0.0.1:8000/api/bookings/
```

**Get All Payments:**
```http
GET http://127.0.0.1:8000/api/payments/
```

## Push to GitHub

Follow these commands to push your code to GitHub:

1. Initialize git (if not already initialized):
```bash
git init
```

2. Configure your identity (if not set):
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

3. Add all files to staging:
```bash
git add .
```

4. Check the status:
```bash
git status
```

5. Commit your changes:
```bash
git commit -m "Your commit message here"
```

6. Add remote repository (if not already added):
```bash
git remote add origin https://github.com/marymaya10/Tourism-Booking.git
```

7. Push to GitHub:
```bash
git push -u origin main
```

**Note:** If your branch is named `master` instead of `main`, use:
```bash
git push -u origin master
```

**To push subsequent changes:**
```bash
git add .
git commit -m "Your new commit message"
git push
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
- `payment_status` - Status (pending, completed, failed, refunded)
- `transaction_reference` - External transaction ID
- `created_at` - Creation timestamp

### Review
- `user` - ForeignKey to User
- `destination` - ForeignKey to Destination
- `rating` - Rating (1-5)
- `comment` - Review comment
- `created_at` - Creation timestamp

## License

MIT License
