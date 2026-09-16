# 🛠️ UstaMarketplace

**UstaMarketplace** is a full-stack service marketplace that connects clients with skilled workers such as plumbers, electricians, and other service providers.

Clients can discover services, place and track orders, and leave reviews. Workers can manage their profiles, offer services, and handle incoming orders.

The project is built with **Django REST Framework** and a lightweight **HTML, Bootstrap, and Vanilla JavaScript** frontend.

---

## 🌐 Live Demo

**Website:**
https://ustamarketplace.onrender.com/index.html

> Deployed on Render.

---

## ✨ Features

### 🔐 Authentication & Authorization

* JWT authentication with access and refresh tokens
* User registration and login
* Role-based access control
* Separate permissions for clients and workers
* Protected API resources

### 👤 User Roles

**Client**

* Browse and view services
* View worker information
* Place and track orders
* Cancel orders when allowed
* Review completed orders
* Manage account information

**Worker**

* Manage worker profile
* Create and manage services
* View and manage incoming orders
* Accept, complete, or cancel orders when allowed
* Receive ratings and reviews

**Admin**

* Manage users, workers, categories, services, orders, and reviews through **Django Admin**

---

## 📦 Orders

Orders follow a simple lifecycle:

```text
Client
  ↓
Selects a service
  ↓
Places an order
  ↓
Worker accepts
  ↓
Service is completed
  ↓
Client leaves a review
```

Supported statuses:

```text
Pending → Accepted → Completed
```

Orders can also be cancelled when the corresponding business rules allow it.

---

## ⭐ Reviews & Ratings

Clients can review a worker after completing an order.

Each review contains:

* Rating
* Review text
* Related completed order
* Worker rating information

---

## 🔧 Services & Worker Profiles

Workers can create services with:

* Name
* Description
* Price
* Category
* Worker information

Services are organized into categories such as **Plumbing** and **Electrical**.

Worker profiles include professional information such as:

* Bio
* Years of experience
* Location

Worker profiles are automatically created when a worker account is registered.

---

## 📊 API Features

The REST API includes:

* Filtering
* Pagination
* Ordering
* Rating-related queries
* Role-based permissions
* Server-side validation

The API is documented using **OpenAPI / Swagger** through `drf-spectacular`.

---

## 🧪 Testing

The backend includes automated API tests covering important functionality such as:

* Authentication
* Services
* Orders
* Permissions
* Client and worker functionality

The test suite is integrated into **GitHub Actions**.

---

## 🏗️ Tech Stack

### Backend

* Python 3.11
* Django 5.2
* Django REST Framework
* SimpleJWT
* Django Filter
* PostgreSQL
* drf-spectacular

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* Vanilla JavaScript

### DevOps

* Docker
* GitHub Actions
* Render
* Gunicorn

---

## 🔒 Security

The application uses:

* JWT authentication
* Role-based permissions
* Protected API resources
* Server-side validation
* Environment variables for sensitive configuration

Secrets such as database credentials and secret keys are kept outside the source code.

---

## 🐳 Docker

The backend can be run using Docker.

```bash
docker build -t ustamarketplace .
docker run -p 8000:8000 ustamarketplace
```

The container applies Django migrations and starts the application with Gunicorn.

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/SuhrobbekJorayev/ustamarketplace.git
cd ustamarketplace
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file with the required configuration.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an admin user

```bash
python manage.py createsuperuser
```

### 7. Run the server

```bash
python manage.py runserver
```

The backend will be available at:

```text
http://127.0.0.1:8000/
```

---

## 🔄 Continuous Integration

GitHub Actions automatically runs the project's backend tests when changes are pushed or submitted through a pull request.

```text
Push / Pull Request
        ↓
GitHub Actions
        ↓
Install dependencies
        ↓
Run tests
```

---

## 🏗️ Architecture

```text
┌─────────────────────────┐
│  HTML + Bootstrap + JS  │
│        Frontend         │
└────────────┬────────────┘
             │ HTTP / REST
             ▼
┌─────────────────────────┐
│    Django REST API      │
│ Authentication & RBAC   │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       PostgreSQL        │
└─────────────────────────┘
```

---

## 🚧 Future Improvements

Possible future additions include:

* Real-time notifications
* WebSocket-based communication
* Background task processing
* Advanced search and filtering
* Online payments
* Client-worker messaging
* More automated tests
* Analytics

These features are **not part of the current implementation**.

---

## 📌 Project Status

UstaMarketplace is a functional full-stack application covering:

* JWT authentication
* Client and worker roles
* Worker profiles
* Service management
* Order management
* Reviews and ratings
* REST API
* PostgreSQL
* Automated testing
* Docker
* GitHub Actions
* Render deployment

---

## 👨‍💻 Author

**Suhrobbek Jorayev**

Backend-focused developer interested in building practical web applications and REST APIs with Python and Django.

---

## 📄 License

This project is intended for learning, portfolio, and demonstration purposes.
