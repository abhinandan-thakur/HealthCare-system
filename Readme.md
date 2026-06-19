# Healthcare Backend API

## Overview

A Healthcare Backend API built using Django, Django REST Framework (DRF), PostgreSQL, and JWT Authentication.

### Features

* User Registration
* User Authentication using JWT
* Patient Management
* Doctor Management
* Patient-Doctor Mapping
* PostgreSQL Database Integration
* Environment Variable Configuration
* Protected API Endpoints

---

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* SimpleJWT
* python-dotenv

---

## Project Setup

### Clone Repository

```bash
git clone <repository-url>
cd healthcare
```

### Create Virtual Environment

```bash
python -m venv healthcare-env
source healthcare-env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file using `.env.example`.

Example:

```env
SECRET_KEY=your-secret-key

DB_NAME=healthcare
DB_USER=healthcare_user
DB_PASSWORD=password123
DB_HOST=localhost
DB_PORT=5432
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

Server will be available at:

```text
http://127.0.0.1:8000/
```

---

## Authentication

### Register User

```http
POST /api/auth/register/
```

### Login

```http
POST /api/auth/login/
```

Returns:

```json
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
```

### Refresh Access Token

```http
POST /api/auth/refresh/
```

Request:

```json
{
    "refresh": "<refresh_token>"
}
```

Returns:

```json
{
    "access": "<new_access_token>"
}
```

### Authorization Header

All protected endpoints require:

```http
Authorization: Bearer <access_token>
```

---

## API Endpoints

### Patients

| Method | Endpoint              |
| ------ | --------------------- |
| POST   | `/api/patients/`      |
| GET    | `/api/patients/`      |
| GET    | `/api/patients/{id}/` |
| PUT    | `/api/patients/{id}/` |
| DELETE | `/api/patients/{id}/` |

Example Create Request:

```json
{
    "name": "Mr. Potato",
    "phone_number": "7896533210",
    "age": 31
}
```

---

### Doctors

| Method | Endpoint             |
| ------ | -------------------- |
| POST   | `/api/doctors/`      |
| GET    | `/api/doctors/`      |
| GET    | `/api/doctors/{id}/` |
| PUT    | `/api/doctors/{id}/` |
| DELETE | `/api/doctors/{id}/` |

Example Create Request:

```json
{
    "name": "Dr. Honey",
    "specialization": "Gynecologist",
    "work_experience": 5,
    "room_number": "A-25"
}
```

---

### Patient-Doctor Mapping

| Method | Endpoint                      |
| ------ | ----------------------------- |
| POST   | `/api/mappings/`              |
| GET    | `/api/mappings/`              |
| GET    | `/api/mappings/{id}/`         |
| GET    | `/api/mappings/patient/{id}/` |
| GET    | `/api/mappings/doctor/{id}/`  |
| DELETE | `/api/mappings/{id}/`         |

Example Create Request:

```json
{
    "patient": 1,
    "doctor": 1
}
```
---

## Database

The project uses PostgreSQL as the primary database.

Database credentials are loaded from environment variables and are not stored in source control.

---

## Screenshot of Postman Request
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/06d97241-9adb-4c6c-916e-e7949152d3b6" />
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/1502babe-199b-4917-92f9-d9a8ea67fcba" />
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/709b4037-2f67-4e0b-9f14-a1f55206020f" />

## Notes

* JWT Authentication is implemented using `djangorestframework-simplejwt`.
* Protected endpoints require a valid access token.
* Django ORM is used for all database interactions.
* Environment variables are managed through `.env`.
* API endpoints were tested using Postman.

---

## Author

Abhinandan Thakur
