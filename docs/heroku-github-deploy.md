# Heroku Deployment via GitHub Integration

Deploy your Django project using Heroku's GitHub integration (no CLI needed).

## ✅ Prerequisites

Before deploying, ensure you have:

- ✅ Django project with all changes committed
- ✅ Code pushed to GitHub repository
- ✅ `.env.example` file for environment variables
- ✅ `Procfile` and `runtime.txt` configured
- ✅ `requirements.txt` with all dependencies

---

## Step 1: Create Heroku App

1. Go to [Heroku Dashboard](https://dashboard.heroku.com/)
2. Click **"New"** → **"Create new app"**
3. Choose an app name (e.g., `my-django-app` or `portfolio-site`)
4. Select region (United States or Europe)
5. Click **"Create app"**

---

## Step 2: Connect to GitHub

1. In your new Heroku app, click the **"Deploy"** tab
2. Under "Deployment method", click **"GitHub"**
3. Click **"Connect to GitHub"** (authorize if needed)
4. Search for your repository (e.g., **`django-project`**)
5. Click **"Connect"** next to your repository

---

## Step 3: Add PostgreSQL Database

1. Click the **"Resources"** tab
2. Under "Add-ons", search for: **`Heroku Postgres`**
3. Select **"Heroku Postgres"**
4. Choose plan: **"Essential 0"** (free, up to 10,000 rows)
5. Click **"Submit Order Form"**

This automatically creates a `DATABASE_URL` environment variable.

---

## Step 4: Configure Environment Variables

1. Click the **"Settings"** tab
2. Click **"Reveal Config Vars"**
3. Add these variables (click "Add" for each):

### Required Variables

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Generate a new one (see below) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-app-name.herokuapp.com` |

### How to Generate SECRET_KEY

**Option A:** Use this online tool (quick):
1. Go to: https://djecrety.ir/
2. Copy the generated key
3. Paste into Heroku

**Option B:** Generate locally:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### Example Config Vars

Your Config Vars should look like this:

```
DATABASE_URL: postgres://user:pass@host:5432/dbname  (automatically added)
SECRET_KEY: django-insecure-v3ry-l0ng-r@nd0m-str1ng-h3r3
DEBUG: False
ALLOWED_HOSTS: brennan-portfolio.herokuapp.com
```

---

## Step 5: Deploy

1. Go back to the **"Deploy"** tab
2. Scroll to "Manual deploy" section
3. Select branch: **`master`**
4. Click **"Deploy Branch"**

You'll see the build log:
- ✅ Fetching from GitHub
- ✅ Installing Python 3.13.5
- ✅ Installing dependencies
- ✅ Running collectstatic
- ✅ Running migrations (via Procfile)
- ✅ Build succeeded!

---

## Step 6: Create Admin User

After deployment completes:

1. Click **"More"** (top right) → **"Run console"**
2. Type: `python manage.py createsuperuser`
3. Click **"Run"**
4. Follow prompts to create username, email, and password

---

## Step 7: View Your App!

1. Click **"Open app"** (top right)
2. Your app should load at: `https://your-app-name.herokuapp.com`
3. Admin panel: `https://your-app-name.herokuapp.com/admin`

---

## Optional: Enable Automatic Deploys

Want every GitHub push to auto-deploy?

1. **Deploy** tab
2. Scroll to "Automatic deploys"
3. Select branch: **`master`**
4. Click **"Enable Automatic Deploys"**

Now every time you `git push`, Heroku will automatically deploy! 🎉

---

## Troubleshooting

### App Shows "Application Error"

**Check logs:**
1. Click **"More"** → **"View logs"**
2. Look for error messages

**Common fixes:**
- Verify all Config Vars are set correctly
- Make sure `ALLOWED_HOSTS` includes your app name
- Check that `DATABASE_URL` exists

### Static Files Not Loading

**Solution:**
1. Go to **Settings** → **Config Vars**
2. Verify `DISABLE_COLLECTSTATIC` is NOT set
3. Redeploy the app

### Need to Run Migrations Manually

1. **More** → **Run console**
2. Type: `python manage.py migrate`
3. Click **Run**

### Reset Database

⚠️ **Warning: This deletes all data!**

1. **Resources** tab
2. Click on "Heroku Postgres"
3. **Settings** → **Reset Database**
4. After reset, run migrations:
   - **More** → **Run console**
   - `python manage.py migrate`
   - `python manage.py createsuperuser`

---

## Monitoring Your App

### View Logs (Real-time)
1. **More** → **View logs**
2. See requests, errors, and system messages

### Metrics
1. **Metrics** tab
2. View dyno load, response times, and throughput

### Set Up Alerts
1. **Metrics** tab
2. Configure email alerts for errors or downtime

---

## Managing Your App

### Restart App
1. **More** → **Restart all dynos**
2. Use if app is unresponsive

### Scale Dynos
1. **Resources** tab
2. Click edit icon next to "web"
3. Slide to scale (free tier = 1 dyno)

### Run Django Commands
1. **More** → **Run console**
2. Available commands:
   - `python manage.py migrate`
   - `python manage.py createsuperuser`
   - `python manage.py shell`
   - `python manage.py dbshell`

---

## Custom Domain (Optional)

### Add Your Domain
1. **Settings** tab → **Domains**
2. Click **"Add domain"**
3. Enter: `www.yourdomain.com`
4. Copy the DNS target

### Update DNS Records
Add to your domain registrar:
- **Type**: CNAME
- **Name**: www
- **Value**: [DNS target from Heroku]

### Update ALLOWED_HOSTS
1. **Settings** → **Config Vars**
2. Update `ALLOWED_HOSTS`: 
   ```
   your-app-name.herokuapp.com,www.yourdomain.com,yourdomain.com
   ```

### Enable SSL (Free!)
Heroku provides free SSL certificates automatically!

---

## Cost Breakdown

### Free Tier Includes:
- ✅ 1000 dyno hours/month
- ✅ PostgreSQL (10,000 rows)
- ✅ SSL certificate
- ✅ Automatic deployments
- ✅ Custom domains

### Upgrade Options:
- **Eco Dynos**: $5/month per dyno (never sleeps)
- **Basic Postgres**: $9/month (10M rows)
- **Standard Dynos**: $25+/month (auto-scaling)

---

## Quick Reference

### Your App URLs
- **App**: `https://your-app-name.herokuapp.com` (replace with your actual app name)
- **Admin**: `https://your-app-name.herokuapp.com/admin`
- **Dashboard**: `https://dashboard.heroku.com/apps/your-app-name`

### Important Tabs
- **Deploy**: Deploy and view build logs
- **Resources**: Manage add-ons and dynos
- **Settings**: Config vars and domain settings
- **Metrics**: Performance monitoring
- **Activity**: Deployment history

---

## Next Steps

1. ✅ Deploy to Heroku (steps above)
2. 📱 Add data via admin panel
3. 🎨 Customize your portfolio
4. 🔄 Set up automatic deploys
5. 📊 Monitor metrics and logs
6. 🌐 Add custom domain (optional)

---

## Need Help?

- **Heroku Status**: https://status.heroku.com/
- **Documentation**: See `heroku-deployment.md` for detailed info
- **Support**: https://help.heroku.com/

---

**Deployment Status**: ✅ Ready to deploy via GitHub!

Just follow the steps above and you'll be live in ~5 minutes! 🚀
