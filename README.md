# BookNest

A modern book discovery and recommendation platform that helps users find their next great read, track their reading journey, and connect with fellow book enthusiasts.

## Project Overview

BookNest is a full-stack web application that combines the power of Django REST Framework and React to create a seamless book discovery experience. The platform features personalized book recommendations using machine learning algorithms, user profiles, social interactions, and comprehensive book information.

### Key Features

- **Book Discovery**: Browse, search, and explore books by genre, author, or popularity
- **Personalized Recommendations**: Get book suggestions based on your reading history and preferences
- **User Profiles**: Create and customize your reading profile
- **Social Features**: Follow other readers, see their activity in your feed
- **Book Details**: Access comprehensive information about books, authors, and genres
- **Notifications**: Stay updated on social interactions and new recommendations

### Tech Stack

#### Backend
- **Django**: Web framework for building the API
- **Django REST Framework**: For creating RESTful APIs
- **PostgreSQL**: Primary database
- **Celery**: Task queue for background processing
- **Redis**: For caching and as a message broker
- **Surprise**: Machine learning library for recommendation system
- **Cloudinary**: Cloud storage for media files

#### Frontend
- **React**: JavaScript library for building the user interface
- **React Router**: For client-side routing
- **Axios**: For making HTTP requests
- **Formik & Yup**: For form handling and validation
- **TailwindCSS**: For styling
- **Vite**: Build tool and development server

## Prerequisites

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.10 or higher
- **Node.js**: Version 16.0 or higher
- **npm**: Version 8.0 or higher (comes with Node.js)
- **PostgreSQL**: Version 15 or higher
- **Docker & Docker Compose**: Latest version (optional, for containerized setup)

### Global Tools

- **virtualenv**: For creating isolated Python environments
  ```bash
  pip install virtualenv
  ```
- **Git**: For version control

## Traditional Installation (Local Development)

### Clone the Repository

```bash
git clone https://github.com/JinxX404/BookNest_fullstack.git
cd BookNest_fullstack
```

### Backend Setup

1. **Create and activate a virtual environment**

   ```bash
   cd server
   python -m virtualenv venv
   
   # On Windows
   .\venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

2. **Install Python dependencies**

   ```bash
   pip install -r req.txt
   ```

3. **Set up environment variables**

   Copy the example environment file and update it with your values:

   ```bash
   cp .env.example .env
   ```

   Edit the `.env` file with your database credentials, Cloudinary API keys, and other configuration values.

4. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Django development server**

   ```bash
   python manage.py runserver
   ```

   The backend API will be available at http://localhost:8000/

### Frontend Setup

1. **Navigate to the client directory**

   ```bash
   cd ../client
   ```

2. **Install Node.js dependencies**

   ```bash
   npm install
   ```

3. **Run the React development server**

   ```bash
   npm run dev
   ```

   The frontend application will be available at http://localhost:5173/

## Dockerized Installation

BookNest can be easily deployed using Docker and Docker Compose, which sets up the entire stack including PostgreSQL, Redis.

### Docker Compose Overview

The `docker-compose.yml` file defines several services:

- **db**: PostgreSQL database
- **web**: Django backend API
- **celery**: Background task processing
- **redis**: Caching and message broker

### Steps to Run with Docker

1. **Set up environment variables**

   Copy the example environment file and update it with your values:

   ```bash
   cd server
   cp .env.example .env
   ```

2. **Build and start the containers**

   ```bash
   docker-compose up --build
   ```

3. **Run migrations inside the container**

   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Create a superuser**

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Navigate to the client directory**

   ```bash
   cd ../client
   ```

6. **Install Node.js dependencies**

   ```bash
   npm install
   ```

7. **Run the React development server**

   ```bash
   npm run dev
   ```

   The frontend application will be available at http://localhost:5173/


### Access URLs

- **Backend API**: http://localhost:8000/
- **Frontend** (if deployed separately): http://localhost:5173/

### Shutting Down and Cleaning Up

```bash
# Stop containers
docker-compose down

# Remove volumes (caution: this will delete all data)
docker-compose down -v
```

## Usage

### Logging In

Access the application at http://localhost:5173/ (or your deployed URL) and log in with your credentials.

### API Documentation

The API documentation is available at http://localhost:8000/swagger/ when running the backend server.

### Running Tests

```bash
# Backend tests
cd server
python manage.py test

# Frontend tests
cd client
npm test
```

## Troubleshooting

### Common Issues

#### Port Conflicts

If you encounter port conflicts, you can modify the port mappings in the `docker-compose.yml` file or change the ports in your local development servers:

```bash
# For Django
python manage.py runserver 8001

# For React/Vite
npm run dev -- --port 5174
```

#### Database Migration Issues

If you encounter migration issues, try resetting the migrations:

```bash
python manage.py migrate --fake books zero
python manage.py migrate books
```
