FROM python:3.5.1

RUN apt-get update
RUN easy_install -U pip

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
