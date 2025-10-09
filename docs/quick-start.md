# Quick Start Guide

> For users who just want to get the project running quickly.

## Prerequisites
- Python 3.12 installed
- PostgreSQL installed and running
- Git

## Setup Commands (Copy & Paste)

### 1. Fork and Clone Repository
```bash
# Fork the repository on GitHub first, then clone YOUR fork:
git clone https://github.com/YOUR-USERNAME/django-project.git
cd django-project

# Create virtual environment with Python 3.12
python3.12 -m venv env

# Activate virtual environment
source env/bin/activate  # On Windows: env\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
# Copy example environment file
cp .env.example .env

# Generate a secure secret key
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Now edit `.env` with your favorite editor and add:
- The generated SECRET_KEY
- Your PostgreSQL password
- Set DEBUG=True for development

### 3. Setup Database
```bash
# Create PostgreSQL database (adjust credentials as needed)
sudo -u postgres psql -c "CREATE DATABASE portfoliodb;"

# Or if you have PostgreSQL password authentication:
# createdb portfoliodb

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
```

### 4. Run Development Server
```bash
python manage.py runserver
```

Visit: http://localhost:8000

Admin panel: http://localhost:8000/admin

## One-Line Test
```bash
python manage.py check && echo "✅ All checks passed!"
```

## Common Commands

### Development
```bash
# Run server
python manage.py runserver

# Run on different port
python manage.py runserver 8080

# Make migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Open Django shell
python manage.py shell
```

### Database
```bash
# Access PostgreSQL
sudo -u postgres psql portfoliodb

# Show tables
\dt

# Exit
\q
```

### Virtual Environment
```bash
# Activate
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows

# Deactivate
deactivate

# Install new package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt
```

## Troubleshooting

### "SECRET_KEY" error
```bash
# Make sure you created .env file
cp .env.example .env
# Then add a SECRET_KEY to it
```

### "No module named 'django'"
```bash
# Make sure virtual environment is activated
source env/bin/activate
pip install -r requirements.txt
```

### "psycopg" installation error
```bash
# Install PostgreSQL development headers
# Ubuntu/Debian:
sudo apt install libpq-dev python3-dev

# macOS:
brew install postgresql
```

### Database connection error
```bash
# Make sure PostgreSQL is running
sudo systemctl status postgresql  # Linux
brew services list | grep postgres  # macOS

# Check your .env database settings
cat .env | grep DB_
```

### Port already in use
```bash
# Use different port
python manage.py runserver 8080

# Or find and kill process on port 8000
lsof -ti:8000 | xargs kill -9  # macOS/Linux
```

## Production Deployment

### Pre-deployment checklist
```bash
# Run security checks
python manage.py check --deploy

# Set production environment variables
# DEBUG=False
# SECRET_KEY=unique-production-key
# ALLOWED_HOSTS=yourdomain.com
# DATABASE_URL=postgresql://user:pass@host:port/db

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate
```

## Need More Help?

- **Detailed Guide**: See `UPGRADE_GUIDE.md`
- **Complete Checklist**: See `UPGRADE_CHECKLIST.md`
- **Security Info**: See `SECURITY.md`
- **Changes Made**: See `CHANGES_SUMMARY.md`

---

**Still stuck?** Open an issue on GitHub or check the original `NOTES.md` file.
