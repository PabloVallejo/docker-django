Using [Docker](https://www.docker.com/) with [Django](https://www.djangoproject.com/)
=======

This is a base Django project that uses [Docker](https://www.docker.com/), it can be used as a starting point for a new project.

After building the project you'll get:
* Python 3.5.1
* Django 1.9.6
* Postgres 9.5.0
* Debian Jessie

### Getting started

To get started you first have to download [Docker Toolbox](https://www.docker.com/products/docker-toolbox) and get it running. Once you get it installed open the terminal and issue the following commands.

```bash
# Clone the repo.
https://github.com/PabloVallejo/docker-django.git && cd django-docker

# Build project.
docker-compose build

# Run the project.
docker-compose up
```

### Caveats

* Make sure you have Docker Quickstart Terminal initialized
