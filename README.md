# 🐍 Basic Blog Application

Basic Django Application where users can sign in and create blog posts.

---

## 📦 Features

- ✅ Django backend
- ✅ Basic Authentication
- ✅ Gunicorn for production server
- ✅ Docker support
- ✅ Static files collection ready for production
- ✅ Environment variable configuration via `.env`

---

## 🚀 Getting Started

### 1. Clone the Repository

```
git clone https://github.com/ArmandleRoux98/Blog-app.git
cd blog_project
```
### 2. Create .env File

Create a .env file in the root directory with the following environment variables:
```
DEBUG=1
SECRET_KEY=your-secret-key
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

# MySQL settings
DB_NAME=mydatabase
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=localhost or db (for container)
DB_PORT=5432
```

### 3. Build and Run Docker Containers

Make sure [Docker](https://www.docker.com/products/docker-desktop/) and [Docker Compose](https://docs.docker.com/compose/install/) are installed. Ensure you are in the blog_project directory and run:
```
docker-compose build
```
followed by
```
docker-compose up
```
You can apply migrations to the database in the container use:
```
docker-compose exec web python manage.py migrate
```
Your app will be accessible at: http://localhost 

To stop your containers run:
```
docker-compose stop
```

**or**

### Run in Virtual Environment
Ensure that all dependencies are installed if you have not yet created a virtual environment now would be a good time.
```
python -m venv venv
```
Once we have a virtual environment we can install dependencies.
```
pip install -r requirements.txt
```
First we need to apply migrations to the database.  Ensure you are in the blog_project directory and run:
```
python manage.py migrate
```
Now we can run the server.
```
python manage.py runserver
```
Your app will be accessible at: http://localhost:8000 

### 🗃️ Project Structure
```
.
├── Dockerfile
├── compose.yml
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
├── blog_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── authenticate/
│   ├── __init__.py
│   ├── apps.py
│   ├── urls.py
│   ├── views.py
│   └── templates
│       └── authenticate
│           ├── login.html
│           └── registration.html
│── blog_app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates
│       ├── base.html
│       ├── create_post.html
│       ├── home.html
│       └── view_post.html
│   └── static
│       └── create_blog.css
```

### 🧰 Tech Stack

- Python 3.12
- Django 4+
- PostgreSQL
- Gunicorn
- Docker
- Docker compose

### 👨‍💻 Author
- Armand le Roux
- GitHub: @ArmandleRoux98
