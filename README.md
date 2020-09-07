<h1 align="center">Brennan's Django Showcase</h1>

<!-- NEW BADGES-->
<p align="center">
<img alt="GitHub code size in bytes"
src="https://img.shields.io/github/languages/code-size/brennanbrown/django-project"> <img alt="GitHub repo size"
src="https://img.shields.io/github/repo-size/brennanbrown/django-project"> <img alt="GitHub top language"
src="https://img.shields.io/github/languages/top/brennanbrown/django-project"> <img alt="GitHub issues" src="https://img.shields.io/github/issues/brennanbrown/django-project"> <img alt="GitHub last commit"
src="https://img.shields.io/github/last-commit/brennanbrown/django-project"> <img alt="GitHub" src="https://img.shields.io/github/license/brennanbrown/django-project"> <img alt="Website"
src="https://img.shields.io/website?down_color=red&down_message=Offline%21&label=Status&up_color=darkgreen&up_message=Online%21&url=https%3A%2F%2Fdjango.life">
<br />
<img alt="GitHub followers"
src="https://img.shields.io/github/followers/brennanbrown?label=Follow%20Me%21&style=social"> <img alt="GitHub watchers"
src="https://img.shields.io/github/watchers/brennanbrown/django-project?label=Watch%21&style=social"> <img alt="GitHub stars"
src="https://img.shields.io/github/stars/brennanbrown/django-project?label=Star%21&style=social"> <img alt="GitHub forks"
src="https://img.shields.io/github/forks/brennanbrown/django-project?label=Fork%21&style=social">
</p>

**Table of Contents:**

- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
    - [Python installation on Ubuntu](#python-installation-on-ubuntu)
    - [PostgreSQL installation on Ubuntu](#postgresql-installation-on-ubuntu)
- [Installation](#installation)
  - [Virtual Environment (`venv`)](#virtual-environment-venv)
  - [Running the project](#running-the-project)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

<!-- ABOUT THE PROJECT -->
## About The Project

View project **[here!](http://django.life/)**

Django—an open-source web framework that's designed on top of Python—can help you quickly bring your website ideas to life. This project utilizes Bootstrap 4 and vanilla JavaScript for the front-end, and a PostgresSQL database, with GraphQL used for API functionality. It also uses Selenium for test-driven development. Finally, this is will be deployed on a [DigitalOcean](https://digitalocean.com/) Droplet under their smallest plan, so I apologize for any issues regarding speed or connectivity!

For more information about specific areas of this project, please refer to my **[personal notes](https://github.com/brennanbrown/django-project/blob/master/NOTES.md)**.

<!-- GETTING STARTED -->
## Getting Started

For development, you will need Python 3.6 or higher, pip, venv, and PostgeSQL installed in your environment.

### Prerequisites

* A good understanding of web development (HTML, CSS, JavaScript)
* Basic knowledge of Python and SQL database systems
* Familar with Django framework for front-end and back-end development
* Object-oriented Programming (OOP) paradigm
* Model-View-Controller (MVC) paradigm
* Model-View-ViewMode (MVVM) paradigm
* Knowledge and use of the Command-line Interface (CLI)

#### Python installation on Ubuntu

On Ubuntu 20.04 and later, Python 3 comes pre-installed. Check first to see if you have the tools required already installed:

    $ python3 --version
    $ pip3 --version

Head over to the [official Python website](https://www.python.org/downloads/) and download the installer
Also, be sure to have `git` donwloaded and available in your PATH as well.

You can install Python and pip easily with apt install, just run the following commands:

    $ sudo apt install python3
    $ sudo apt install python3-pip

There are a few more packages and development tools to install to ensure that we have a robust setup for our programming environment:

    $ sudo apt install -y build-essential libssl-dev libffi-dev python3-dev

If you need to update `pip`, you can make it using `pip`! Cool right? After running the following command, just open again the command line and be happy.

    $ python3 -m pip install --upgrade pip

#### PostgreSQL installation on Ubuntu

Installation of PostgreSQL via CLI:

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

Installation of the pgAdmin GUI:

```bash
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/
`lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
$ sudo apt-get update
$ sudo apt-get install pgadmin4 pgadmin4-apache2 -y
```

Please note for sake of ease, this project is set to work with the default configurations of PostgreSQL on a local installation.


## Installation

    $ git clone https://github.com/brennanbrown/django-project.git
    $ cd django-project

### Virtual Environment (`venv`)

While there are a few ways to achieve a programming environment in Python, we’ll be using the venv module here, which is part of the standard Python 3 library. Let’s install venv by typing:

    $ sudo apt install python3-venv

Creating and entering a new virtual environment:

    $ python3 -m venv env
    $ . env/bin/activate
    $ pip install -r requirements.txt

You can ensure that you're in your new virutal Environment if you see `(env)` prepend your bash shell:

    (env) user@ubuntu:~/django_project$ 

### Running the project

    $ python3 manage.py runserver

Once the server has started up, you can visit it at [localhost:8000/](localhost:8000/), or [127.0.0.1:8000/](127.0.0.1:8000/).

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/brennanbrown/django-project/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Brennan K. Brown - [@brennankbrown](https://twitter.com/brennanbrown) - [mail@brennanbrown.ca](mailto:mail@brennanbrown.ca)

Project Link: [https://github.com/brennanbrown/django-project](https://github.com/brennanbrown/django-project)