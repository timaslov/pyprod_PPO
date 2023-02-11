FROM python:3.11

WORKDIR /pyprod_app/pyprod/

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        git \
        python3-pip \
        python3-dev \

COPY requirements.pip requirements.pip
RUN pip install -r requirements.pip
