# Django Demo Site

A multi-page Django application ready for deployment to Render.com.

## Features

- Multiple pages (Home, About, Blog, Contact)
- Blog functionality with admin interface
- Production-ready configuration
- Static file handling with WhiteNoise
- PostgreSQL support

## Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Run migrations:
python manage.py migrate
Create a superuser:
python manage.py createsuperuser
Run the development server:
python manage.py runserver
Visit http://localhost:8000 to see the site.
Deployment to Render.com
Push this code to GitHub
Create a new Web Service on Render
Connect your GitHub repository
Configure the service:
Build Command: ./build.sh
Start Command: gunicorn mysite.wsgi:application
Add a PostgreSQL database
Set environment variables:
SECRET_KEY: A secure random string
DEBUG: False
ALLOWED_HOSTS: your-app.onrender.com
DATABASE_URL: (auto-populated by Render PostgreSQL)
Deploy!
Environment Variables
SECRET_KEY: Django secret key (required in production)
DEBUG: Set to False in production
ALLOWED_HOSTS: Comma-separated list of allowed hosts
DATABASE_URL: PostgreSQL connection string (auto-set by Render)
License
MIT
This is a complete Django site ready for deployment! Make sure to:
1. Give execute permissions to build.sh: `chmod +x build.sh`
2. Set a strong SECRET_KEY in Render environment variables
3. Create a superuser after deployment to access the admin panel
