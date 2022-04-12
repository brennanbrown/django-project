# Personal Notes

**Table of Contents:**

- [Personal Notes](#personal-notes)
  - [Getting Started](#getting-started)
  - [Project vs. Apps](#project-vs-apps)
  - [Database Management](#database-management)
  - [Admin Dashboard](#admin-dashboard)
  - [Deployment on DigitalOcean](#deployment-on-digitalocean)
  - [Deployment on Heroku](#deployment-on-heroku)

## Getting Started

- Ensure you have both Python and Django installed on your machine.
- In order to create a new Django website, simply type the command: `django-admin startproject projectname`
- Installing each package from `requirements.txt` without errors causing halt: `requirements.txt | xargs -n 1 pip3 install`
- If having trouble with psycopg2 package: `sudo apt-get install libpq-dev`

## Project vs. Apps

- An average website has many components.
  - There's part of the website that covers events, part of it's a blog, and part of it is accounts letting people log in and out of the website.
- In the Django world, the whole website is considered the project, and then the individual pieces are the apps.
  - Eg. If you want to modify the blog, you can dive specifically into the blog app and make that change without affecting anything else.
  - So with a Django web project, you want to create a specific app for each part of the website.
  - It's common practice to name apps with a pluarlity, eg. jobs instead of job.
- To build specific apps within your existing project: `django-admin startapp jobs`

## Database Management

Installation of PostgreSQL on Ubuntu:

```bash
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get install postgresql
```

Install pgAdmin GUI:

```bash
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/
`lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
$ sudo apt-get update
$ sudo apt-get install pgadmin4 pgadmin4-apache2 -y
```

- You can now start the database server using: `pg_ctlcluster 12 main start`
- Access server from terminal: `sudo -u postgres psql postgres`
- Add the password to the posgres superuser: `ALTER USER postgres PASSWORD 'newPassword';`
- Create a new database in the server: `CREATE DATABASE portfoliodb;`
- Create a new table with the server:`CREATE TABLE jobs;`
- Create migrations from `models.py` to PostgreSQL DB: `python3 manage.py makemigrations`
  - Whenever creating or modifiyng models, run command.
- Apply migrations: `python3 manage.py migrate`
- Optimize all complete migrations: `python manage.py squashmigrations appname 000X`, where X is the latest migration.

Accessing the DB via the terminal:

- To view all of the defined databases on the server you can use the `\list` meta-command or its shortcut `\l`.
- Often, when working with servers that manage multiple databases, you’ll find the need to jump between databases frequently.
  - This can be done with the `\connect` meta-command or its shortcut `\c`.
- Once you’ve connected to a database, you will want to inspect which tables have been created there.
  - This can be done with the `\dt` meta-command. However, if there are no tables you will get no output.

## Admin Dashboard

- Access the Django Admin dashboard: `localhost:8000/admin`
  - Create admin user: `python3 manage.py createsuperuser`
- Add static files to website: `python3 manage.py collectstatic`
  - Combines all the static files from each individual app into one place.

## Deployment on DigitalOcean

- Deployment on DigitalOcean for a Django/PostgreSQL/NGINX website is well documented [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04).
- The only thing needed to be added is `location /media/` in the file `/etc/nginx/sites-avaiable/PROJECTNAME`:

```
server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /media/ {
        root /home/sammy/myprojectdir;
    }
    location /static/ {
        root /home/sammy/myprojectdir;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

- Installation of `cert-bot` to obtain encrpyted SSL is easy to install, guide [here](https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx).
  - How to point DigitalOcean Nameservers guide [here](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars).

## Deployment on Heroku

- The `Procfile` requires two lines:
  - First, `release: python manage.py migrate`, to update the database with each push.
  - Second, using gunicorn to run the `.wsgi` file: `web: gunicorn portfolio.wsgi`
- Creating a Django superuser on Heroku: `heroku run -a appname python3 manage.py createsuperuser`

**Note**: I recommend using DigitalOcean for deployment. The official documentation for connecting Heroku to S3 is [pretty lacking](https://devcenter.heroku.com/articles/s3), as it only deals with static assets, and not media files from a db for example, this [guide](https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/) is pretty good, but for some reason, whenever the Postgres db is successfully set, Heroku puts all files in `/tmp` or locally on the site instead of using S3.

AWS's Beanstalk has good documentation for [Django](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html), but requires troubleshooting for installing the pip package psycopg2 which is required for connecting with a Postgres db, this is a good solution [for that](https://stackoverflow.com/questions/17137346/psycopg2-on-amazon-elastic-beanstalk).
