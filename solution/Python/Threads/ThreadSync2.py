"""
this is regarding the blocking attribute in lock.acquire
"""
from threading import Thread , Lock
import time
lock = Lock()

def person_one(lock):
    while True:
        if lock.acquire(blocking=True) is True:
            break
        else:
            print("Lock is not Free")
    print("1 enters the room")
    time.sleep(5)
    print("1 exits the room")
    lock.release()

def person_two(lock):
    while True:
        if lock.acquire(blocking=False) is True:
            break
        else:
            print("Lock is not Free")
    print("2 enters the room")
    time.sleep(5)
    print("2 exits the room")
    lock.release()

t1 = Thread(target=person_one,args = (lock,))
t2 = Thread(target=person_two,args = (lock,))
t1.start()
t2.start()
t1.join()
t2.join()
