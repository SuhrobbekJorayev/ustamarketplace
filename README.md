# UstaMarketplace

UstaMarketplace is a marketplace platform where clients can find services and place orders, while workers can publish services and manage incoming orders.

## Features

### Authentication

* User registration
* User login with JWT authentication
* Logout

### Roles

* Client
* Worker

### Services

* Create services (workers only)
* Update services
* Delete services
* Search services
* Filter services by price
* Ordering and pagination

### Orders

* Clients can place orders
* Workers can manage incoming orders
* Order statuses:

  * Pending
  * Accepted
  * Completed
  * Canceled

### Reviews

* One review per order
* Ratings and comments
* Average rating per service
* Review count per service

## Tech Stack

### Backend

* Python
* Django
* Django REST Framework
* PostgreSQL
* JWT Authentication
* Swagger / OpenAPI

### Frontend

* HTML
* CSS
* JavaScript
* Bootstrap

## Project Structure

```
UstaMarketplace/
│
├── Backend/
│
├── Frontend/
│
└── README.md
```

## Installation

### Backend

```bash
cd Backend

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

### Frontend

Open the frontend files in your browser or serve them with a local development server.

## API Documentation

Swagger documentation is available at:

```
/swagger/
```

## User Roles

### Client

* Browse services
* Place orders
* Cancel orders
* Leave reviews

### Worker

* Create services
* Manage services
* Accept orders
* Complete orders
* Cancel orders

## Learning Goals

This project was built to practice:

* Django REST Framework
* Authentication and Authorization
* Permissions
* API Design
* Business Logic Implementation
* Frontend Integration

## Future Improvements

* Deployment
* Better dashboard UI
* Worker verification
* Notifications
* Advanced filtering
* Profile pages

---

Built as a learning project using Django REST Framework.
