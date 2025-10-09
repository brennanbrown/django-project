# Heroku Deployment Guide

Complete guide to deploying your Django 5.1 project to Heroku.

## Prerequisites

- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed
- Heroku account (free tier works)
- Git installed
- Project already committed to git

## Quick Deployment (5 Minutes)

### 1. Install Heroku CLI (if needed)

**macOS:**
```bash
brew tap heroku/brew && brew install heroku
```

**Ubuntu/Debian:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

**Windows:**
Download from https://devcenter.heroku.com/articles/heroku-cli

### 2. Login to Heroku
```bash
heroku login
```

### 3. Create Heroku App
```bash
# Create app with auto-generated name
heroku create

# OR create with specific name
heroku create your-app-name
```

This will output your app URL: `https://your-app-name.herokuapp.com`

### 4. Add PostgreSQL Database
```bash
# Add free PostgreSQL addon
heroku addons:create heroku-postgresql:essential-0

# Verify it was added
heroku addons
```

This automatically sets the `DATABASE_URL` environment variable.

### 5. Configure Environment Variables
```bash
# Generate a new SECRET_KEY
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Set the SECRET_KEY (use the generated key)
heroku config:set SECRET_KEY="your-generated-secret-key-here"

# Set DEBUG to False for production
heroku config:set DEBUG="False"

# Set ALLOWED_HOSTS (use your actual Heroku app name)
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"

# Verify all config vars
heroku config
```

### 6. Deploy
```bash
# Make sure all changes are committed
git add .
git commit -m "Prepare for Heroku deployment"

# Push to Heroku (this deploys your app)
git push heroku main

# Or if you're on master branch
git push heroku master
```

### 7. Create Superuser
```bash
heroku run python manage.py createsuperuser
```

### 8. Open Your App
```bash
heroku open
```

Visit `/admin` to access the admin panel with your superuser credentials.

## Complete Step-by-Step Guide

### Understanding What's Already Set Up

Your project already has these Heroku-ready files:

1. **`Procfile`** ✅
   ```
   release: python manage.py migrate
   web: gunicorn portfolio.wsgi
   ```
   - `release`: Runs migrations automatically on each deploy
   - `web`: Starts the gunicorn server

2. **`runtime.txt`** ✅
   ```
   python-3.12.7
   ```
   - Tells Heroku which Python version to use

3. **`requirements.txt`** ✅
   - All dependencies are listed with correct versions

4. **`settings.py`** ✅
   - Already configured to read `DATABASE_URL`
   - Environment variable support built-in
   - WhiteNoise for static files

### Environment Variables Reference

Set all these on Heroku:

```bash
# Required
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG="False"
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"

# Optional (if using AWS S3 for media files)
heroku config:set AWS_ACCESS_KEY_ID="your-aws-key"
heroku config:set AWS_SECRET_ACCESS_KEY="your-aws-secret"
heroku config:set AWS_STORAGE_BUCKET_NAME="your-bucket-name"
heroku config:set AWS_S3_REGION_NAME="us-east-1"
```

### Verify Deployment

```bash
# Check if app is running
heroku ps

# View recent logs
heroku logs --tail

# Run Django checks
heroku run python manage.py check --deploy
```

## Managing Your Heroku App

### Useful Commands

```bash
# View logs
heroku logs --tail

# Run Django management commands
heroku run python manage.py <command>

# Open Django shell
heroku run python manage.py shell

# Restart app
heroku restart

# Check app status
heroku ps

# View environment variables
heroku config

# Set environment variable
heroku config:set VAR_NAME="value"

# Remove environment variable
heroku config:unset VAR_NAME

# Scale dynos (increase/decrease)
heroku ps:scale web=1

# Access PostgreSQL
heroku pg:psql
```

### Database Management

```bash
# Access database
heroku pg:psql

# Create database backup
heroku pg:backups:capture

# Download latest backup
heroku pg:backups:download

# View database info
heroku pg:info

# Reset database (WARNING: deletes all data)
heroku pg:reset DATABASE_URL --confirm your-app-name
heroku run python manage.py migrate
```

### Collecting Static Files

Static files are automatically collected during deployment thanks to WhiteNoise. No manual collectstatic needed!

## Custom Domain Setup

### Add Custom Domain

```bash
# Add your domain
heroku domains:add www.yourdomain.com
heroku domains:add yourdomain.com

# View DNS targets
heroku domains
```

### Configure DNS

Add these records to your domain's DNS:

**CNAME Record:**
- Host: `www`
- Value: `your-app-name.herokuapp.com`

**ANAME/ALIAS Record** (or URL redirect):
- Host: `@`
- Value: `your-app-name.herokuapp.com`

### Update ALLOWED_HOSTS

```bash
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com,www.yourdomain.com,yourdomain.com"
```

### Enable SSL (Free)

Heroku provides free SSL for all apps:

```bash
heroku certs:auto:enable
```

## Troubleshooting

### Application Error / Crash

```bash
# Check logs
heroku logs --tail

# Common issues:
# 1. Missing environment variables
heroku config

# 2. Database not migrated
heroku run python manage.py migrate

# 3. Wrong Python version
cat runtime.txt  # Should be python-3.12.7
```

### Static Files Not Loading

```bash
# Check WhiteNoise is in MIDDLEWARE
heroku run python manage.py check

# Verify settings
heroku run python manage.py diffsettings | grep STATIC
```

### Database Connection Error

```bash
# Verify DATABASE_URL is set
heroku config:get DATABASE_URL

# Check database status
heroku pg:info

# Try restarting
heroku restart
```

### Module Not Found

```bash
# Verify requirements.txt includes all dependencies
cat requirements.txt

# Check what's installed on Heroku
heroku run pip list

# Force rebuild
git commit --allow-empty -m "Rebuild"
git push heroku main
```

### Secret Key Error

```bash
# Set a new SECRET_KEY
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
heroku config:set SECRET_KEY="paste-generated-key-here"
```

## File Upload / Media Files

By default, Heroku's filesystem is ephemeral (files are lost on restart). For user uploads:

### Option 1: AWS S3 (Recommended)

1. Create AWS S3 bucket
2. Install boto3 (already in requirements.txt)
3. Set environment variables:
   ```bash
   heroku config:set AWS_ACCESS_KEY_ID="your-key"
   heroku config:set AWS_SECRET_ACCESS_KEY="your-secret"
   heroku config:set AWS_STORAGE_BUCKET_NAME="your-bucket"
   heroku config:set AWS_S3_REGION_NAME="us-east-1"
   ```

4. Update `settings.py` to use S3 (instructions in UPGRADE_GUIDE.md)

### Option 2: Cloudinary

Alternative to AWS S3, easier setup:

```bash
heroku addons:create cloudinary:starter
```

## Cost Optimization

### Free Tier Limits

- **Dyno Hours**: 1000 hours/month (enough for 1 always-on app)
- **PostgreSQL**: 10,000 rows
- **Build Time**: 30 minutes
- **Slug Size**: 500 MB

### Tips to Stay Free

1. Use hobby/eco dynos ($5-7/month) instead of free if you need 24/7 uptime
2. Scale down when not needed: `heroku ps:scale web=0`
3. Use database row count wisely
4. Optimize slug size (remove unnecessary files)

## Monitoring

### View App Metrics

```bash
# Open metrics dashboard
heroku open --metrics
```

### Set Up Alerts

Through Heroku dashboard:
1. Go to your app
2. Click "Metrics" tab
3. Set up alerts for errors, response time, etc.

## CI/CD Setup (Optional)

### Connect to GitHub

1. Go to Heroku Dashboard
2. Select your app
3. Deploy tab → GitHub
4. Connect repository
5. Enable automatic deploys from main branch

Now every push to main automatically deploys!

## Additional Resources

- **Heroku Django Guide**: https://devcenter.heroku.com/articles/django-app-configuration
- **Heroku PostgreSQL**: https://devcenter.heroku.com/articles/heroku-postgresql
- **Heroku CLI Commands**: https://devcenter.heroku.com/articles/heroku-cli-commands
- **Django Deployment Checklist**: `python manage.py check --deploy`

## Pre-Deployment Checklist

- [ ] All changes committed to git
- [ ] SECRET_KEY generated and ready
- [ ] Requirements.txt is up to date
- [ ] Tested locally with DEBUG=False
- [ ] Database backup created (if migrating existing data)
- [ ] Custom domain DNS configured (if applicable)
- [ ] AWS S3 bucket ready (if using for media files)

## Quick Reference Card

```bash
# Deploy
git push heroku main

# View logs
heroku logs --tail

# Run command
heroku run python manage.py <command>

# Shell access
heroku run bash

# Restart
heroku restart

# Config
heroku config

# Database
heroku pg:psql
```

---

**Need help?** Check UPGRADE_GUIDE.md or open an issue on GitHub.

**Deployment Status**: ✅ Ready for Heroku!
