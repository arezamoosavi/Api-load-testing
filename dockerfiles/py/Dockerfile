FROM python:3.7.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PIP_FORMAT=legacy

RUN apt-get -y update && apt-get install -y python-pip python-dev libzbar-dev bash \
    gcc python3-dev git libc-dev

RUN echo 'deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main' >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends apt-utils

RUN apt-get install -y netcat && apt-get autoremove -y

RUN adduser --disabled-password --gecos '' myuser

# RUN groupadd -r xuzer && useradd -r -g xuzer xuzer

RUN pip install --upgrade pip

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir -p /main

WORKDIR /main

# Faust
COPY ./dockerfiles/py/faustRun.sh /faustRun.sh
RUN chmod +x /faustRun.sh

# App
COPY ./dockerfiles/py/appRun.sh /appRun.sh
RUN chmod +x /appRun.sh

# App Builder
COPY ./dockerfiles/py/builder.sh /builder.sh
RUN chmod +x /builder.sh

CMD ["/builder.sh"]
