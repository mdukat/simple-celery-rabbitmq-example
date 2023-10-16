FROM python:3.10

RUN pip install celery

WORKDIR /usr/src/app

COPY test_celery ./test_celery

CMD [ "celery", "-A", "test_celery", "worker", "--loglevel=info" ]
