# Very simple RabbitMQ + Celery implementation

A very simple RabbitMQ + Celery implementation in Python 3.10, inspired by [tests4geeks](https://tests4geeks.com/blog/python-celery-rabbitmq-tutorial/). Modified to use Python 3 and docker, and use `AsyncResult` method.

## Run containers

```
docker-compose up -d
```

## Start task - Synchronous

```
python3 -m test_celery.run_tasks
```

## Start task - Asynchronous

```
python3 -m test_celery.run_tasks_async
```

## RabbitMQ Management Panel

RabbitMQ Management Panel is running on [http://localhost:15672/](http://localhost:15672/). User: `user`, password: `password`, as defined in `docker-compose.yml`.

## Links used to create this example:

  - [https://tests4geeks.com/blog/python-celery-rabbitmq-tutorial/](https://tests4geeks.com/blog/python-celery-rabbitmq-tutorial/)
  - [https://hub.docker.com/_/python](https://hub.docker.com/_/python)
  - [https://hub.docker.com/_/rabbitmq](https://hub.docker.com/_/rabbitmq)
  - [https://docs.docker.com/compose/compose-file/build/](https://docs.docker.com/compose/compose-file/build/)
  - [https://www.rabbitmq.com/management.html](https://www.rabbitmq.com/management.html)

