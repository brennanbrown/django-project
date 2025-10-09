# Heroku Quick Start

Deploy your Django project to Heroku in ~5 minutes.

## Option 1: Automated Script (Easiest)

```bash
./deploy-to-heroku.sh
```

The script will:
- ✅ Check if Heroku CLI is installed
- ✅ Login to Heroku
- ✅ Create app if needed
- ✅ Add PostgreSQL database
- ✅ Set environment variables
- ✅ Deploy your app
- ✅ Offer to create superuser

## Option 2: Manual Commands

### 1. Login
```bash
heroku login
```

### 2. Create App
```bash
heroku create your-app-name
```

### 3. Add Database
```bash
heroku addons:create heroku-postgresql:essential-0
```

### 4. Set Environment Variables
```bash
# Generate SECRET_KEY
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Set config (replace with your generated key)
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set DEBUG="False"
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"
```

### 5. Deploy
```bash
git push heroku main
```

### 6. Create Superuser
```bash
heroku run python manage.py createsuperuser
```

### 7. Open App
```bash
heroku open
```

## That's It! 🎉

Your app is now live at: `https://your-app-name.herokuapp.com`

Admin panel: `https://your-app-name.herokuapp.com/admin`

## Essential Commands

```bash
# View logs
heroku logs --tail

# Restart app
heroku restart

# Run Django commands
heroku run python manage.py <command>

# Access database
heroku pg:psql
```

## Need More Help?

See `HEROKU_DEPLOYMENT.md` for complete documentation.

## Troubleshooting One-Liners

```bash
# App crashed?
heroku logs --tail

# Migrations not applied?
heroku run python manage.py migrate

# Need to check config?
heroku config

# Force rebuild?
git commit --allow-empty -m "Rebuild" && git push heroku main
```
