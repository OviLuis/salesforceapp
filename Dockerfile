FROM python:3.6
MAINTAINER logonzalez <logoz471@gmailcom.com>
ENV PYTHONUNBUFFERED=1

RUN mkdir /salesforceapp

WORKDIR /salesforceapp

COPY requirements.txt /salesforceapp/ 

RUN python -m pip install -r requirements.txt


COPY . /salesforceapp/






