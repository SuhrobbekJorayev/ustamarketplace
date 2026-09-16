# 🛠️ UstaMarketplace

**UstaMarketplace** is a full-stack service marketplace that connects clients with skilled workers such as plumbers, electricians, and other service providers.

The platform allows clients to discover services, place orders, track their status, and leave reviews, while workers can manage their profiles, create services, and manage incoming orders.

The project is built with **Django REST Framework** on the backend and a lightweight **HTML, Bootstrap, and Vanilla JavaScript** frontend.

---

## 🌐 Live Demo

**Website:**
https://ustamarketplace.onrender.com/index.html

**Backend API:**
https://hidden_please_do_not_try 😅

**API Documentation:**
Available through the project's Swagger / OpenAPI documentation.

> The application is deployed on Render.

---

# ✨ Features

## 🔐 Authentication & Authorization

* User registration
* JWT-based authentication
* Access and refresh tokens
* Login / logout flow
* Role-based access control
* Separate permissions for clients and workers
* Protected API endpoints

---

## 👤 User Roles

UstaMarketplace has three main roles:

### 🧑 Client

Clients can:

* Register and authenticate
* Browse available services
* View service details
* View worker information
* Place orders
* View their orders
* Track order status
* Cancel orders when allowed
* Complete orders
* Leave reviews for completed orders
* Manage their account information

### 🔧 Worker

Workers can:

* Register as a worker
* Manage their worker profile
* Add and manage services
* View incoming orders
* Accept orders
* Complete orders
* Cancel orders when allowed
* View their order history
* Receive ratings and reviews from clients
* Manage their professional information

### 🛡️ Admin

Administrators have access to Django's administration interface and can manage the platform's data, including:

* Users
* Worker profiles
* Categories
* Services
* Orders
* Reviews
* Other application data

---

# 🔧 Services

Workers can create services that clients can order.

Each service can contain information such as:

* Service name
* Description
* Price
* Category
* Worker
* Rating-related information

Clients can browse available services and choose a service based on the provided information.

### Categories

Services are organized into categories to make discovery easier.

Examples include:

* Plumbing
* Electrical

---

# 📦 Orders

The order system is one of the core parts of UstaMarketplace.

### Order flow

```text
Client
   ↓
Selects a service
   ↓
Places an order
   ↓
Worker receives the order
   ↓
Worker accepts the order
   ↓
Service is completed
   ↓
Client can leave a review
```

### Order statuses

Orders can move through different states:

```text
Pending
   ↓
Accepted
   ↓
Completed
```

Orders can also be cancelled when the corresponding business rules allow it.

This provides a clear lifecycle for service requests between clients and workers.

---

# ⭐ Reviews & Ratings

After a service order is completed, clients can leave a review for the worker.

The review system includes:

* Rating
* Review text
* Connection between the review and completed order
* Worker rating information

A review is associated with an order, helping keep feedback connected to an actual service interaction.

---

# 👨‍🔧 Worker Profiles

Workers have a dedicated profile containing professional information such as:

* User information
* Bio
* Years of experience
* Location

User account information such as name and email is managed through the main `User` model rather than being duplicated inside the worker profile.

Worker profiles are automatically created when a worker account is registered.

---

# 📊 Dashboards

The application provides different experiences depending on the user's role.

### Client Dashboard

Clients can:

* View their orders
* Track order statuses
* Manage their account
* Access their service-related information

### Worker Dashboard

Workers can:

* View incoming orders
* Manage orders
* Manage services
* Manage their worker profile
* Monitor their service activity

### Admin Dashboard

Administrators can use Django Admin to manage and inspect platform data.

---

# 🔎 Filtering, Pagination & Ordering

The API supports functionality that makes working with larger datasets easier, including:

* Filtering
* Pagination
* Ordering
* Rating-related queries

These features are implemented on the backend using Django REST Framework and Django Filter.

---

# 📡 REST API

The backend follows a REST API architecture.

# 📚 API Documentation

The project uses **drf-spectacular** to generate OpenAPI documentation.

# 🧪 Testing

The backend includes API tests using Django REST Framework's testing tools.

The project currently includes tests covering important API behavior such as:

* Authentication
* Services
* Orders
* Permissions
* Worker functionality
* Client functionality
* API responses

The test suite is also integrated into the project's CI workflow.

---

# 🏗️ Tech Stack

## Backend

* Python 3.11
* Django 5.2
* Django REST Framework
* SimpleJWT
* Django Filter
* PostgreSQL
* drf-spectacular

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* Vanilla JavaScript

## DevOps & Deployment

* Docker
* GitHub Actions
* Render
* Gunicorn

---

# 🗄️ Database

The project uses **PostgreSQL** as its production database.

The application uses Django's ORM for database operations and migrations.

---

# 🔒 Security

The API uses several mechanisms for protecting application resources:

* JWT authentication
* Permission classes
* Role-based access control
* Protected endpoints
* Server-side validation
* Django's built-in security mechanisms
* Environment variables for sensitive configuration

Sensitive values such as:

* Secret keys
* Database credentials
* JWT-related configuration

are kept outside the source code through environment configuration.

---

# 🐳 Docker

The backend can be run inside a Docker container.

The Docker setup installs project dependencies, collects static files, applies database migrations, and starts the application using Gunicorn.

Example:

```bash
docker build -t ustamarketplace .
docker run -p 8000:8000 ustamarketplace
```

---

# ⚙️ Local Installation

## 1. Clone the repository

```bash
git clone https://github.com/SuhrobbekJorayev/ustamarketplace.git
cd ustamarketplace
```

---

## 2. Create a virtual environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file and configure the required environment variables.

---

## 5. Apply migrations

```bash
python manage.py migrate
```

---

## 6. Create an admin user

```bash
python manage.py createsuperuser
```

---

## 7. Run the development server

```bash
python manage.py runserver
```

The backend will be available at:

```text
http://127.0.0.1:8000/
```

---

# 🔄 CI/CD

The project uses **GitHub Actions** for automated checks.

The CI workflow is used to run backend tests and verify that changes do not break the existing API functionality.

Typical workflow:

```text
Push / Pull Request
        ↓
GitHub Actions
        ↓
Install dependencies
        ↓
Run tests
        ↓
Build / deployment workflow
```

---

# ☁️ Deployment

The project is configured for deployment on **Render**.

The deployed architecture consists of:

```text
Frontend
   ↓
Backend REST API
   ↓
PostgreSQL
```

The backend runs with Gunicorn inside a Docker container.

Database migrations are applied during container startup.

---

# 🧩 Architecture Overview

```text
                    ┌─────────────────┐
                    │     Client      │
                    │ HTML + Bootstrap│
                    │  Vanilla JS     │
                    └────────┬────────┘
                             │
                             │ HTTP / REST
                             ▼
                    ┌─────────────────┐
                    │   Django REST   │
                    │      API        │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
          PostgreSQL      JWT Auth      Django Admin
```

---

# 🎯 Project Goals

The main goal of UstaMarketplace is to provide a simple platform where:

* Clients can find suitable service providers.
* Workers can offer their services.
* Clients can place and track orders.
* Workers can manage incoming requests.
* Completed services can receive customer feedback.

The project also serves as a practical backend development project covering authentication, authorization, relational data modeling, REST APIs, testing, deployment, and database management.

---

# 🚧 Future Improvements

Potential improvements for future versions include:

* Real-time notifications
* WebSocket-based communication
* Asynchronous background tasks
* Improved search
* More advanced service filtering
* Online payment integration
* Improved messaging between clients and workers
* More detailed analytics
* Additional automated tests

These features are not part of the current core implementation.

---

# 📌 Current Status

UstaMarketplace is a functional full-stack web application with:

* JWT authentication
* Client and worker roles
* Worker profiles
* Service management
* Order management
* Order status tracking
* Reviews and ratings
* Role-specific dashboards
* PostgreSQL
* REST API
* Swagger/OpenAPI documentation
* Automated API tests
* Docker setup
* GitHub Actions CI
* Render deployment

---

# 👨‍💻 Author

**Suhrobbek Jorayev**

Backend-focused developer interested in building practical web applications and REST APIs with Python and Django.

---

## 📄 License

This project is intended for learning, portfolio, and demonstration purposes.
