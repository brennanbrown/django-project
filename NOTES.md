# Personal Notes

**Table of Contents:**

- [Personal Notes](#personal-notes)
  - [Getting Started](#getting-started)
  - [Project vs. Apps](#project-vs-apps)
  - [Database Management](#database-management)
  - [Admin Dashboard](#admin-dashboard)

## Getting Started

* Ensure you have both Python and Django installed on your machine.
* In order to create a new Django website, simply type the command: `django-admin startproject projectname`
* Installing each package from `requirements.txt` without errors causing halt: `requirements.txt | xargs -n 1 pip3 install`
* If having trouble with psycopg2 package: `sudo apt-get install libpq-dev`

## Project vs. Apps

* An average website has many components. 
    - There's part of the website that covers events, part of it's a blog, and part of it is accounts letting people log in and out of the website. 
* In the Django world, the whole website is considered the project, and then the individual pieces are the apps.
    - Eg. If you want to modify the blog, you can dive specifically into the blog app and make that change without affecting anything else. 
    - So with a Django web project, you want to create a specific app for each part of the website.
    - It's common practice to name apps with a pluarlity, eg. jobs instead of job.
* To build specific apps within your existing project:  `django-admin startapp jobs`

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

* You can now start the database server using: `pg_ctlcluster 12 main start`
* Access server from terminal: `sudo -u postgres psql postgres`
* Add the password to the posgres superuser: `ALTER USER postgres PASSWORD 'newPassword';`
* Create a new database in the server: `CREATE DATABASE portfoliodb;`
* Create a new table with the server:`CREATE TABLE jobs;`
* Create migrations from `models.py` to PostgreSQL DB: `python3 manage.py makemigrations`
    - Whenever creating or modifiyng models, run command.
* Apply migrations: `python3 manage.py migrate`
* Optimize all complete migrations: `python manage.py squashmigrations appname 000X`, where X is the latest migration.

Accessing the DB via the terminal:

* To view all of the defined databases on the server you can use the `\list` meta-command or its shortcut `\l`.
* Often, when working with servers that manage multiple databases, you’ll find the need to jump between databases frequently. 
    - This can be done with the `\connect` meta-command or its shortcut `\c`.
* Once you’ve connected to a database, you will want to inspect which tables have been created there. 
    - This can be done with the `\dt` meta-command. However, if there are no tables you will get no output.

## Admin Dashboard

* Access the Django Admin dashboard: `localhost:8000/admin`
    - Create admin user: `python3 manage.py createsuperuser`
* Add static files to website: `python3 manage.py collectstatic`
    - Combines all the static files from each individual app into one place.

## Deployment on Heroku

* The `Procfile` requires two lines:
    - First, `release: python manage.py migrate`, to update the database with each push.
    - Second, using gunicorn to run the `.wsgi` file: `web: gunicorn portfolio.wsgi`
* Creating a Django superuse on Heroku: `heroku run -a appname python3 manage.py createsuperuser`