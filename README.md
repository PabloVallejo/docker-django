Using [Docker](https://www.docker.com/) with [Django](https://www.djangoproject.com/)
=======

This is a base Django project that uses [Docker](https://www.docker.com/), it can be used as a starting point for a new project.

![Screenshot](https://s3.amazonaws.com/uploads.hipchat.com/50553/714369/X4OX9RcXAGkBZci/photo.png)

After building the project you'll get:
* [Python 3.5.1](https://www.python.org/downloads/release/python-351/)
* [Django 1.9.6](https://docs.djangoproject.com/en/1.9/releases/1.9.6/)
* [Postgres 9.5.0](http://www.postgresql.org/docs/9.5/static/release-9-5.html)
* [Debian Jessie](https://www.debian.org/releases/jessie/)


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
