from .tasks import longtime_add
import time

if __name__ == '__main__':
    result = longtime_add.delay(1,2)
    
    print("Task ID: " + str(result.id))
    # If you want to get result by ID: https://stackoverflow.com/a/30760142

    print("Task finished? " + str(result.ready()))
    print("Task result: " + str(result.result))

    time.sleep(10)
    print("Task finished? " + str(result.ready()))
    print("Task result: " + str(result.result))

