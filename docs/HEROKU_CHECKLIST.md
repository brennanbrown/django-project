# Heroku Deployment Checklist

Use this checklist to ensure successful Heroku deployment.

## Pre-Deployment

- [ ] Install Heroku CLI
  ```bash
  # macOS
  brew tap heroku/brew && brew install heroku
  
  # Ubuntu/Linux
  curl https://cli-assets.heroku.com/install.sh | sh
  ```

- [ ] Verify Heroku CLI is installed
  ```bash
  heroku --version
  ```

- [ ] Login to Heroku
  ```bash
  heroku login
  ```

- [ ] All changes committed to git
  ```bash
  git status  # Should show "nothing to commit"
  ```

- [ ] Test locally with production settings
  ```bash
  export DEBUG=False
  python manage.py check --deploy
  ```

## App Setup

- [ ] Create Heroku app
  ```bash
  heroku create your-app-name
  # Note: Save your app name and URL
  ```

- [ ] Verify Heroku remote was added
  ```bash
  git remote -v  # Should show heroku remote
  ```

- [ ] Add PostgreSQL database
  ```bash
  heroku addons:create heroku-postgresql:essential-0
  ```

- [ ] Verify database was added
  ```bash
  heroku addons
  heroku config:get DATABASE_URL
  ```

## Environment Configuration

- [ ] Generate SECRET_KEY
  ```bash
  python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
  # Copy the output
  ```

- [ ] Set SECRET_KEY
  ```bash
  heroku config:set SECRET_KEY="paste-your-key-here"
  ```

- [ ] Set DEBUG
  ```bash
  heroku config:set DEBUG="False"
  ```

- [ ] Set ALLOWED_HOSTS
  ```bash
  heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"
  ```

- [ ] Verify all config vars
  ```bash
  heroku config
  ```

## Deployment

- [ ] Push to Heroku
  ```bash
  git push heroku main
  # Or: git push heroku master
  ```

- [ ] Monitor deployment logs
  ```bash
  heroku logs --tail
  ```

- [ ] Verify app is running
  ```bash
  heroku ps
  ```

- [ ] Run database migrations (if not auto-run)
  ```bash
  heroku run python manage.py migrate
  ```

- [ ] Create superuser
  ```bash
  heroku run python manage.py createsuperuser
  ```

## Verification

- [ ] Open app in browser
  ```bash
  heroku open
  ```

- [ ] Verify homepage loads

- [ ] Test admin panel
  ```bash
  heroku open /admin
  ```

- [ ] Login with superuser credentials

- [ ] Run deployment security check
  ```bash
  heroku run python manage.py check --deploy
  ```

- [ ] Check for errors in logs
  ```bash
  heroku logs --tail
  ```

## Post-Deployment

- [ ] Test all major features:
  - [ ] Homepage displays correctly
  - [ ] Job listings show
  - [ ] Job detail pages work
  - [ ] Static files load (CSS, images)
  - [ ] Admin panel accessible
  - [ ] Can create/edit jobs in admin

- [ ] Monitor app for 24 hours
  ```bash
  heroku logs --tail
  ```

- [ ] Set up monitoring alerts (optional)
  - Go to Heroku Dashboard
  - Navigate to Metrics tab
  - Configure alerts

## Optional Enhancements

- [ ] Enable automatic backups
  ```bash
  heroku pg:backups:schedule DATABASE_URL --at '02:00 America/New_York'
  ```

- [ ] Add custom domain
  ```bash
  heroku domains:add www.yourdomain.com
  heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com,www.yourdomain.com"
  ```

- [ ] Enable SSL
  ```bash
  heroku certs:auto:enable
  ```

- [ ] Set up AWS S3 for media files
  ```bash
  heroku config:set AWS_ACCESS_KEY_ID="your-key"
  heroku config:set AWS_SECRET_ACCESS_KEY="your-secret"
  heroku config:set AWS_STORAGE_BUCKET_NAME="your-bucket"
  ```

- [ ] Connect to GitHub for auto-deploy
  - Go to Heroku Dashboard
  - Deploy tab
  - Connect to GitHub
  - Enable automatic deploys

## Troubleshooting Checklist

If deployment fails, check:

- [ ] All environment variables are set correctly
  ```bash
  heroku config
  ```

- [ ] Requirements.txt is up to date
  ```bash
  cat requirements.txt
  ```

- [ ] Procfile exists and is correct
  ```bash
  cat Procfile
  ```

- [ ] runtime.txt specifies Python 3.12.7
  ```bash
  cat runtime.txt
  ```

- [ ] Database migrations are applied
  ```bash
  heroku run python manage.py showmigrations
  ```

- [ ] No syntax errors in code
  ```bash
  heroku run python manage.py check
  ```

- [ ] Review error logs
  ```bash
  heroku logs --tail
  ```

## Maintenance Tasks

### Weekly
- [ ] Check logs for errors
- [ ] Monitor app performance
- [ ] Test critical functionality

### Monthly
- [ ] Update dependencies (if security updates available)
- [ ] Review database size
- [ ] Create manual backup
  ```bash
  heroku pg:backups:capture
  ```

### As Needed
- [ ] Scale dynos if traffic increases
  ```bash
  heroku ps:scale web=2
  ```

- [ ] Clear old logs
  ```bash
  heroku logs --tail
  ```

## Quick Commands Reference

```bash
# Deployment
git push heroku main

# View logs
heroku logs --tail

# Restart
heroku restart

# Run command
heroku run python manage.py <command>

# Database
heroku pg:psql

# Config
heroku config
heroku config:set VAR="value"
heroku config:unset VAR

# Status
heroku ps

# Open app
heroku open
```

## Emergency Procedures

### App is Down
1. Check logs: `heroku logs --tail`
2. Check dyno status: `heroku ps`
3. Restart app: `heroku restart`
4. Check config: `heroku config`

### Database Issues
1. Check database status: `heroku pg:info`
2. Run migrations: `heroku run python manage.py migrate`
3. Access database: `heroku pg:psql`
4. Restore from backup: `heroku pg:backups:restore`

### Need to Rollback
```bash
# View releases
heroku releases

# Rollback to previous
heroku rollback

# Rollback to specific version
heroku rollback v123
```

---

**Deployment Complete?** ✅

Make sure all checkboxes above are complete before considering deployment successful!
