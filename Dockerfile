FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /menuVote

ADD ./ .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
