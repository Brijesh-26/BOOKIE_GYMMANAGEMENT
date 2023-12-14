# BOOKIE GYM-MANAGEMENT

### username - admin
### password - 123
### baseurl- http://127.0.0.1:8000/

# 🚀 Project Setup

Welcome to the quick-start guide for your Django project! Get up and running in no time.

## ⚙️ Prerequisites

- [Python](https://www.python.org/) installed (version 3.x recommended)
- [Django](https://www.djangoproject.com/) installed (install using `pip install django`)

## 🛠️ Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Brijesh-26/BOOKIE_GYMMANAGEMENT.git
   cd your-django-project

1. **Create a Virtual Environment:**

   ```bash
   python -m venv venv


1. **Activate the Virtual Environment:**

   ```bash
   .\venv\Scripts\activate
   
1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

1. **Apply Migrations:**

   ```bash
   python manage.py migrate

1. **Create Superuser:**

   ```bash
   python manage.py createsuperuser
   
1. **Run the Development Server:**

   ```bash
   python manage.py runserver
   
1. **Access Django Admin:**

   ```bash
   Go to http://localhost:8000/admin
   Log in with the superuser credentials created earlier.
   ```

   

# 🌈 API Endpoints

Welcome to the documentation of our vibrant Django API! Below, you'll find details about the available endpoints and their functionalities.

## 🚀 Authentication

### Get Tokens
- **Endpoint:** `/token/`
- **Method:** `POST`
- **Description:** Obtain a JSON Web Token (JWT) for authentication.

### Refresh Tokens
- **Endpoint:** `/token/refresh/`
- **Method:** `POST`
- **Description:** Refresh the JWT access token using the refresh token.

## 🚀 Gyms

### Create Zyms
- **Endpoint:** `/gyms/`
- **Method:** `POST`
- **Description:** Create a new zym.

### Get All Zym
- **Endpoint:** `/gyms/`
- **Method:** `GET`
- **Description:** Retrieve a list of all zyms.

### Get Zym by ID
- **Endpoint:** `/gyms/<int:pk>/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific zym by ID.

### Update Zym
- **Endpoint:** `/gyms/<int:pk>/`
- **Method:** `PUT`
- **Description:** Update information for a specific zym.

### Delete Zym
- **Endpoint:** `/zyms/<int:pk>/`
- **Method:** `DELETE`
- **Description:** Delete a zym by ID.

## 📦 Trainers

### Create Trainers
- **Endpoint:** `/trainers/`
- **Method:** `POST`
- **Description:** Create a new trainers.

### List All Trainers
- **Endpoint:** `/trainers/`
- **Method:** `GET`
- **Description:** Retrieve a list of all trainers.

### Get Trainers by ID
- **Endpoint:** `/trainers/<int:pk>/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific trainers by ID.

### Update Trainer
- **Endpoint:** `/trainers/<int:pk>/`
- **Method:** `PUT`
- **Description:** Update information for a specific trainer.

### Delete Trainer
- **Endpoint:** `/trainers/<int:pk>/`
- **Method:** `DELETE`
- **Description:** Delete a trainer by ID.

## 🚀 Clients

### Create Clients
- **Endpoint:** `/clients/`
- **Method:** `POST`
- **Description:** Create a new clients.

### List All Clients
- **Endpoint:** `/clients/`
- **Method:** `GET`
- **Description:** Retrieve a list of all clients.

### Get Clients by ID
- **Endpoint:** `/clients/<int:pk>/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific clients by ID.

### Update Clients
- **Endpoint:** `/clients/<int:pk>/`
- **Method:** `PUT`
- **Description:** Update information for a specific clients.

### Delete Clients
- **Endpoint:** `/clients/<int:pk>/`
- **Method:** `DELETE`
- **Description:** Delete a clients by ID.


## 🚀 Workout Sessions

### Create  Workout Sessions
- **Endpoint:** `/workouts/`
- **Method:** `POST`
- **Description:** Create a new workouts.

### List All  Workout Sessions
- **Endpoint:** `/workouts/`
- **Method:** `GET`
- **Description:** Retrieve a list of all workouts.

### Get  Workout Sessions by ID
- **Endpoint:** `/workouts/<int:pk>/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific workouts by ID.

### Update  Workout Sessions
- **Endpoint:** `/workouts/<int:pk>/`
- **Method:** `PUT`
- **Description:** Update information for a specific workouts.

### Delete  Workout Sessions
- **Endpoint:** `/workouts/<int:pk>/`
- **Method:** `DELETE`
- **Description:** Delete a workouts by ID.


Feel free to explore and test these endpoints to unleash the full power of our API! Happy coding! 🚀


