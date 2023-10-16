from celery import Celery
import os

app = Celery('test_celery_name',
        broker='amqp://user:password@' + os.getenv('RABBITMQ_BROKER_URL', 'localhost') + '/my_vhost',
        backend='rpc://',
        include=['test_celery.tasks'])


