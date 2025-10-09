# Django Project Upgrade Guide

## Overview
This project has been upgraded from Django 3.0.3 (Python 3.9) to Django 5.1.3 (Python 3.12) with all dependencies updated to secure, modern versions.

## Major Changes

### 1. Python Version
- **Old**: Python 3.9.0
- **New**: Python 3.12.7
- **Action Required**: Update your local Python installation

### 2. Django Version
- **Old**: Django 3.0.3 (February 2020)
- **New**: Django 5.1.3 (October 2024 - LTS)
- **Breaking Changes**: See Django upgrade notes below

### 3. Database Driver
- **Old**: `psycopg2` (version 2.x)
- **New**: `psycopg` (version 3.x)
- **Change**: Modern async-ready PostgreSQL adapter

### 4. Dependencies Updated

#### Security-Critical Updates
- **Pillow**: 7.0.0 → 11.0.0 (multiple CVE fixes)
- **urllib3**: 1.25.10 → (removed, now via boto3)
- **gunicorn**: 20.0.4 → 23.0.0
- **whitenoise**: 5.2.0 → 6.8.2

#### Removed/Replaced
- ❌ `django-heroku` (deprecated) → ✅ `dj-database-url` + manual config
- ❌ Development dependencies in production → ✅ Separated concerns
- ✅ Added `python-dotenv` for environment variable management

### 5. Settings.py Security Improvements

#### Fixed Security Issues
1. **Secret Key**: No longer hardcoded fallback
2. **DEBUG**: Now properly controlled via environment variable
3. **Database Password**: Removed hardcoded password
4. **ALLOWED_HOSTS**: Now configurable via environment
5. **Static Root**: Fixed duplicate `STATIC_ROOT` (was overwriting with media path)

#### Added Security Headers (Production)
```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
```

#### New Configuration System
Now uses `.env` file with `python-dotenv` for environment variables.

### 6. Code Changes

#### Views (jobs/views.py)
```python
# Old (inefficient)
jobs = Job.objects

# New (proper query)
jobs = Job.objects.all()
```

## Installation & Setup

### 1. Update Python

**macOS (using Homebrew)**:
```bash
brew install python@3.12
```

**Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install python3.12 python3.12-venv
```

### 2. Create Virtual Environment
```bash
# Remove old virtual environment
rm -rf env/

# Create new virtual environment with Python 3.12
python3.12 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file:
```bash
cp .env.example .env
```

Edit `.env` with your settings:
```bash
# Generate a new secret key
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Add it to `.env`:
```
SECRET_KEY=your-generated-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=portfoliodb
DB_USER=postgres
DB_PASSWORD=your-postgres-password
```

### 5. Database Setup

The database configuration has changed. If using a local PostgreSQL:

```bash
# Create database (if not exists)
sudo -u postgres psql -c "CREATE DATABASE portfoliodb;"

# Run migrations
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (if needed)
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 8. Run Development Server
```bash
python manage.py runserver
```

## Django 5.x Migration Notes

### Breaking Changes to Address

1. **DEFAULT_AUTO_FIELD**: Now required (already added to settings)
   ```python
   DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
   ```

2. **USE_L10N**: Deprecated in Django 4.0 (can be removed)
   - It's now always `True` by default

3. **Path Objects**: Now using `pathlib.Path` instead of `os.path.join`
   ```python
   # Old
   BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
   
   # New
   BASE_DIR = Path(__file__).resolve().parent.parent
   ```

### PostgreSQL Adapter Changes

The new `psycopg` (version 3) has different connection parameters:
- Auto-reconnection with `conn_health_checks=True`
- Connection pooling with `conn_max_age=600`
- Better async support

## Production Deployment

### Heroku

Update your Heroku environment variables:
```bash
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG="False"
heroku config:set ALLOWED_HOSTS="your-app.herokuapp.com"
```

The `Procfile` remains the same and still works.

### DigitalOcean

1. Update Python on your droplet:
```bash
sudo apt update
sudo apt install python3.12 python3.12-venv
```

2. Update your virtual environment:
```bash
cd /path/to/your/project
python3.12 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. Update your gunicorn/systemd service file if needed

4. Restart services:
```bash
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

## Testing

Run Django's built-in checks:
```bash
python manage.py check
python manage.py check --deploy
```

## Common Issues & Solutions

### Issue: `psycopg` installation fails
**Solution**: Install PostgreSQL development headers
```bash
# Ubuntu/Debian
sudo apt install libpq-dev python3-dev

# macOS
brew install postgresql
```

### Issue: `SECRET_KEY` errors
**Solution**: Ensure you've copied `.env.example` to `.env` and generated a new secret key

### Issue: Static files not loading
**Solution**: 
```bash
python manage.py collectstatic --clear --noinput
```

### Issue: Database connection errors
**Solution**: Check your `.env` database settings and ensure PostgreSQL is running
```bash
sudo systemctl status postgresql  # Linux
brew services list | grep postgresql  # macOS
```

## Rollback Instructions

If you need to rollback to the old version:

1. Checkout the previous commit:
```bash
git log  # Find the commit before the upgrade
git checkout <commit-hash>
```

2. Reinstall old dependencies:
```bash
pip install -r requirements.txt
```

3. Restore old database if needed (make backups before upgrading!)

## Security Recommendations

1. ✅ **Never commit `.env` files** - Already in `.gitignore`
2. ✅ **Use strong secret keys** - Generate unique keys for each environment
3. ✅ **Keep DEBUG=False in production** - Now enforced via environment variables
4. ✅ **Use HTTPS in production** - Security headers now automatically enabled
5. ✅ **Regularly update dependencies** - Check for security updates monthly

## Next Steps

1. **Test thoroughly**: Test all functionality in development before deploying
2. **Update documentation**: Update any project-specific docs
3. **Deploy to staging**: Test in a staging environment first
4. **Monitor logs**: Watch for any deprecation warnings
5. **Update CI/CD**: Update any CI/CD pipelines with new Python version

## Resources

- [Django 5.1 Release Notes](https://docs.djangoproject.com/en/5.1/releases/5.1/)
- [Django 4.2 to 5.0 Upgrade Guide](https://docs.djangoproject.com/en/5.0/releases/5.0/)
- [psycopg3 Documentation](https://www.psycopg.org/psycopg3/docs/)
- [WhiteNoise Documentation](http://whitenoise.evans.io/en/stable/)

## Changelog

### 2024-10-09
- Upgraded Django 3.0.3 → 5.1.3
- Updated Python 3.9.0 → 3.12.7
- Updated all dependencies to latest secure versions
- Fixed security vulnerabilities in settings.py
- Added environment variable management with python-dotenv
- Fixed database configuration
- Fixed static files configuration
- Added production security headers
- Improved code quality in views
- Created comprehensive documentation
