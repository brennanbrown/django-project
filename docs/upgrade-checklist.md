# Upgrade Checklist

Use this checklist to ensure a smooth upgrade process.

## Pre-Upgrade
- [ ] Backup your database
- [ ] Backup your media files
- [ ] Commit all current changes to git
- [ ] Document current Python/Django versions
- [ ] Test current version works correctly

## Installation Steps
- [ ] Install Python 3.12
- [ ] Remove old virtual environment (`rm -rf env/`)
- [ ] Create new virtual environment (`python3.12 -m venv env`)
- [ ] Activate virtual environment (`source env/bin/activate`)
- [ ] Upgrade pip (`pip install --upgrade pip`)
- [ ] Install new dependencies (`pip install -r requirements.txt`)

## Configuration
- [ ] Copy `.env.example` to `.env`
- [ ] Generate new SECRET_KEY and add to `.env`
- [ ] Set DEBUG=True in `.env` (for development)
- [ ] Configure database settings in `.env`
- [ ] Update ALLOWED_HOSTS in `.env`
- [ ] Verify `.env` is in `.gitignore`

## Database
- [ ] Run `python manage.py makemigrations`
- [ ] Run `python manage.py migrate`
- [ ] Create superuser if needed (`python manage.py createsuperuser`)
- [ ] Test database connection

## Static Files
- [ ] Run `python manage.py collectstatic --clear`
- [ ] Verify static files are collected to `staticfiles/`
- [ ] Verify media files are in `media/` directory

## Testing
- [ ] Run `python manage.py check`
- [ ] Run `python manage.py check --deploy`
- [ ] Start development server (`python manage.py runserver`)
- [ ] Test homepage loads
- [ ] Test admin panel (`/admin`)
- [ ] Test job detail pages
- [ ] Test static files load correctly
- [ ] Test media files display correctly

## Code Review
- [ ] Check for deprecation warnings in console
- [ ] Review all custom code for compatibility
- [ ] Update any hardcoded Django 3.0 references
- [ ] Check for any removed/deprecated methods

## Production Deployment (if applicable)
- [ ] Update environment variables on hosting platform
- [ ] Set DEBUG=False
- [ ] Set proper ALLOWED_HOSTS
- [ ] Set proper SECRET_KEY (unique for production)
- [ ] Configure DATABASE_URL
- [ ] Update Python runtime on server
- [ ] Test on staging environment first
- [ ] Deploy to production
- [ ] Run migrations on production
- [ ] Collect static files on production
- [ ] Monitor logs for errors

## Post-Deployment
- [ ] Verify all pages load correctly
- [ ] Test user authentication
- [ ] Test admin functionality
- [ ] Test image uploads
- [ ] Check SSL/security headers (production)
- [ ] Monitor error logs for 24 hours
- [ ] Update project documentation

## Troubleshooting Completed
- [ ] Document any issues encountered
- [ ] Update UPGRADE_GUIDE.md with solutions
- [ ] Share knowledge with team

---

**Notes Section** (add any specific notes for your deployment):
```
[Your notes here]
```
