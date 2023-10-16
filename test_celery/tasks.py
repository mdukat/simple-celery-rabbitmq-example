from test_celery.celery import app
import time

@app.task
def longtime_add(x, y):
    print("Long time task begins")
    time.sleep(5)
    print("Long time task finished")
    return x + y

