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

## Project vs. Apps

* An average website has many components. 
    - There's part of the website that covers events, part of it's a blog, and part of it is accounts letting people log in and out of the website. 
* In the Django world, the whole website is considered the project, and then the individual pieces are the apps.
    - Eg. If you want to modify the blog, you can dive specifically into the blog app and make that change without affecting anything else. 
    - So with a Django web project, you want to create a specific app for each part of the website.
    - It's common practice to name apps with a pluarlity, eg. jobs instead of job.
* To build specific apps within your existing project:  `django-admin startapp jobs`

## Database Management

* The database is where we save information about different things on our website that we want to have persist over time, and one of these is going to be the jobs on our site 
* You can now start the database server using: `pg_ctlcluster 12 main start`

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

* Access server from terminal: `sudo -u postgres psql postgres`
* Create a new database in the server: `CREATE DATABASE portfolioDB;`
* Create migrations from `models.py` to PostgreSQL DB: `python3 manage.py makemigrations`
    - Whenever creating or modifiyng models, run command.
* Apply migrations: `python3 manage.py migrate`

## Admin Dashboard

* Access the Django Admin dashboard: `localhost:8000/admin`
    - Create admin user: `python3 manage.py createsuperuser`