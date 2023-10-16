from .tasks import longtime_add
from .celery import app
from celery.result import AsyncResult
import time

if __name__ == '__main__':
    result = longtime_add.delay(1,2)

    resultid = result.id
    
    print("Task ID: " + str(resultid))

    res = AsyncResult(resultid, app=app)
    print("Task finished? " + str(res.state))
    print("Task result: " + str(res.get()))

    while res.state != 'SUCCESS':
        res = AsyncResult(resultid, app=app)
        time.sleep(0.1)
    
    print("Task finished? " + str(res.state))
    print("Task result: " + str(res.get()))

